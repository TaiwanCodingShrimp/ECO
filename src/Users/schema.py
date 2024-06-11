import math
import typing
from enum import Enum

import pydantic


class CommuteMethod(str, Enum):
    Car = ("car",)
    Electric_car = "electric_car"
    Motorcycle = "motorcycle"
    Electric_motorcycle = "electric_motorcycle"
    Bus = "bus"
    Train = "train"
    High_speed_rail = "high_speed_rail"


class CommuteFootprints(pydantic.BaseModel):
    car: float
    electric_car: float
    motorcycle: float
    electric_motorcycle: float
    bus: float
    train: float
    high_speed_rail: float


COMMUTE_CARBON_FACTOR_DICT: typing.Dict[str, float] = {
    CommuteMethod.Car.value: 0.173,
    CommuteMethod.Electric_car.value: 0.078,
    CommuteMethod.Motorcycle.value: 0.046,
    CommuteMethod.Electric_motorcycle.value: 0.025,
    CommuteMethod.Bus.value: 0.04,
    CommuteMethod.Train.value: 0.06,
    CommuteMethod.High_speed_rail.value: 0.032,
}


class CarbonFootprintReportData(pydantic.BaseModel):
    commute_distance: typing.Optional[float]

    def _calculate_commute_footprint(self, factor: float) -> typing.Optional[float]:
        if self.commute_distance is None:
            return None
        carbon_footprint = self.commute_distance * factor
        if isinstance(carbon_footprint, float) and not (
            math.isnan(carbon_footprint) or math.isinf(carbon_footprint)
        ):
            return carbon_footprint
        else:
            return None

    def commute_carbon_footprints(self) -> typing.Optional[CommuteFootprints]:
        results = {}
        for commute_method, factor in COMMUTE_CARBON_FACTOR_DICT.items():
            carbon_footprint = self._calculate_commute_footprint(factor=factor)
            if carbon_footprint is not None:
                results[commute_method] = round(carbon_footprint, 3)
            else:
                return None
        return CommuteFootprints(**results)
