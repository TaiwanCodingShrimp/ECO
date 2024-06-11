from datetime import date
from typing import List

import pydantic


class CommuteData(pydantic.BaseModel):
    date: date
    carbon_footprint: float


class Commutechart(pydantic.BaseModel):
    method: str
    commute_datasets: List[CommuteData]


class CommuteCharts(pydantic.BaseModel):
    charts: List[Commutechart] = []
