# Create your views here.
import json
from datetime import date, datetime, timedelta
from functools import cached_property
from typing import Any

import pandas as pd
from django.utils import timezone
from django.views.generic import TemplateView

from Users.models import FootPrint
from Users.schema import CommuteMethod

from .schema import Commutechart, CommuteCharts, CommuteData


class ReportView(TemplateView):
    template_name = "report.html"

    class DataFrameColumns:
        DATE = "date"
        METHOD = "method"
        CARBON_FOOTPRINT = "carbon_footprint"

    @cached_property
    def end_date(self) -> date:
        return timezone.now() - timedelta(days=1)

    @cached_property
    def start_date(self) -> date:
        return self.end_date - timedelta(days=6)

    def get_footprint_origin_pd(self, end_date: date, start_date: date) -> pd.DataFrame:
        footprint_data_pd = pd.DataFrame(
            FootPrint.objects.filter(
                date__gte=start_date,
                date__lte=end_date,
            ).values("date", "method", "distance", "carbon_footprint")
        )
        if not footprint_data_pd.empty:
            # Convert time format
            footprint_data_pd[self.DataFrameColumns.DATE] = pd.to_datetime(
                footprint_data_pd[self.DataFrameColumns.DATE].dt.date
            )
        return footprint_data_pd

    def get_commute_method_charts(
        self,
        report_data: pd.DataFrame,
    ) -> CommuteCharts:
        charts = []
        if report_data.empty:
            return CommuteCharts(charts=charts)

        grouped_by_method_data = (
            report_data.groupby(
                [self.DataFrameColumns.DATE, self.DataFrameColumns.METHOD]
            )[self.DataFrameColumns.CARBON_FOOTPRINT]
            .sum()
            .reset_index()
        )

        for method in CommuteMethod:
            method_df = grouped_by_method_data[
                grouped_by_method_data[self.DataFrameColumns.METHOD] == method.value
            ]
            if not method_df.empty:
                chart = self._get_commute_method_chart(method, method_df)
                charts.append(chart)
        return CommuteCharts(charts=charts)

    def _get_commute_method_chart(
        self,
        method: str,
        method_data: pd.DataFrame,
    ) -> Commutechart:
        datas = []
        for index, row in method_data.iterrows():
            data = CommuteData(
                date=row[self.DataFrameColumns.DATE],
                carbon_footprint=row[self.DataFrameColumns.CARBON_FOOTPRINT],
            )
            datas.append(data)
        chart = Commutechart(method=method, commute_datasets=datas)
        return chart

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        start_date_str = self.request.GET.get("start_date", str(self.start_date))
        end_date_str = self.request.GET.get("end_date", str(self.end_date))

        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
        except ValueError:
            start_date = self.start_date

        try:
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
        except ValueError:
            end_date = self.end_date

        commute_data = self.get_footprint_origin_pd(
            end_date=end_date, start_date=start_date
        )
        context["start_date"] = start_date.strftime("%Y-%m-%d")
        context["end_date"] = end_date.strftime("%Y-%m-%d")

        if commute_data.empty:
            context["commute_metrics"] = json.dumps({"charts": []})
        else:
            commute_time_charts = self.get_commute_method_charts(
                report_data=commute_data
            )
            commute_time_charts_dict = commute_time_charts.dict()

            # Convert date objects to strings
            for chart in commute_time_charts_dict["charts"]:
                for dataset in chart["commute_datasets"]:
                    dataset["date"] = dataset["date"].isoformat()

            context["commute_metrics"] = json.dumps(commute_time_charts_dict)

        return context
