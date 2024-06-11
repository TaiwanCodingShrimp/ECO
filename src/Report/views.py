# Create your views here.
import json
from datetime import date, datetime, timedelta
from functools import cached_property
from typing import Any

import pandas as pd
from django.utils import timezone
from django.views.generic import TemplateView

from Users.models import FootPrint, Leftover
from Users.schema import CommuteMethod

from .schema import (
    AllCommuteChart,
    Commutechart,
    CommuteCharts,
    CommuteData,
    DailyData,
    LeftoverAllCommuteChart,
    LeftoverDailyData,
)


class ReportView(TemplateView):
    template_name = "report.html"

    class DataFrameColumns:
        DATE = "date"
        METHOD = "method"
        CARBON_FOOTPRINT = "carbon_footprint"

    @cached_property
    def end_date(self) -> date:
        return timezone.now().date()

    @cached_property
    def start_date(self) -> date:
        return self.end_date - timedelta(days=6)

    def get_footprint_origin_pd(self, end_date: date, start_date: date) -> pd.DataFrame:
        footprint_data_pd = pd.DataFrame(
            FootPrint.objects.filter(
                date__gte=start_date,
                date__lte=end_date,  # Ensure this filter includes the end date
            ).values("date", "method", "distance", "carbon_footprint")
        )
        return footprint_data_pd

    def get_commute_method_charts(self, report_data: pd.DataFrame) -> CommuteCharts:
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
        self, method: str, method_data: pd.DataFrame
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

    def _get_all_method_chart(self, report_data: pd.DataFrame) -> AllCommuteChart:
        grouped_by_date_data = (
            report_data.groupby([self.DataFrameColumns.DATE])[
                self.DataFrameColumns.CARBON_FOOTPRINT
            ]
            .sum()
            .reset_index()
        )
        datas = []
        for index, row in grouped_by_date_data.iterrows():
            data = DailyData(
                date=row[self.DataFrameColumns.DATE],
                carbon_footprint=row[self.DataFrameColumns.CARBON_FOOTPRINT],
            )
            datas.append(data)
        chart = AllCommuteChart(
            title="Daily Total Commute Footprint",
            dataset=datas,
        )
        return chart

    def get_leftover_pd(self, end_date: date, start_date: date) -> pd.DataFrame:
        leftover_pd = pd.DataFrame(
            Leftover.objects.filter(
                date_put_in__gte=start_date,
                date_put_in__lte=end_date,  # Ensure this filter includes the end date
            ).values("date_put_in", "food_carbon_footprint")
        )
        if not leftover_pd.empty:
            leftover_pd.rename(
                columns={
                    "date_put_in": self.DataFrameColumns.DATE,
                    "food_carbon_footprint": self.DataFrameColumns.CARBON_FOOTPRINT,
                },
                inplace=True,
            )
            leftover_pd = (
                leftover_pd.groupby([self.DataFrameColumns.DATE])[
                    self.DataFrameColumns.CARBON_FOOTPRINT
                ]
                .sum()
                .reset_index()
            )
        return leftover_pd

    def get_leftover_daily_chart(
        self, report_data: pd.DataFrame
    ) -> LeftoverAllCommuteChart:
        datas = []
        for index, row in report_data.iterrows():
            data = LeftoverDailyData(
                date=row[self.DataFrameColumns.DATE],
                carbon_footprint=row[self.DataFrameColumns.CARBON_FOOTPRINT],
            )
            datas.append(data)
        chart = LeftoverAllCommuteChart(
            title="Daily Total Leftover Donate Saving Carbon Footprint",
            dataset=datas,
        )
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
        leftover_data = self.get_leftover_pd(end_date=end_date, start_date=start_date)
        context["start_date"] = start_date.strftime("%Y-%m-%d")
        context["end_date"] = end_date.strftime("%Y-%m-%d")

        if commute_data.empty:
            context["commute_metrics"] = json.dumps({"charts": []})
            context["daily_commute_matrics"] = json.dumps({"dataset": []})
        else:
            commute_time_charts = self.get_commute_method_charts(
                report_data=commute_data
            )
            daily_total_chart = self._get_all_method_chart(report_data=commute_data)
            commute_time_charts_dict = commute_time_charts.dict()
            daily_total_chart_dict = daily_total_chart.dict()
            for dataset in daily_total_chart_dict["dataset"]:
                dataset["date"] = dataset["date"].isoformat()

            for chart in commute_time_charts_dict["charts"]:
                for dataset in chart["commute_datasets"]:
                    dataset["date"] = dataset["date"].isoformat()

            context["commute_metrics"] = json.dumps(commute_time_charts_dict)
            context["daily_commute_matrics"] = json.dumps(daily_total_chart_dict)

        if leftover_data.empty:
            context["leftover_matrics"] = json.dumps({"dataset": []})
        else:
            daily_leftover_chart = self.get_leftover_daily_chart(
                report_data=leftover_data
            )
            daily_leftover_chart_dict = daily_leftover_chart.dict()
            for dataset in daily_leftover_chart_dict["dataset"]:
                dataset["date"] = dataset["date"].isoformat()
            context["leftover_matrics"] = json.dumps(daily_leftover_chart_dict)
        return context
