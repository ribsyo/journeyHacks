from dataclasses import dataclass, field


@dataclass
class Location:
    longitude: float
    latitude: float


@dataclass
class RequestData:
    location: Location
    radius: int  # in meters
    keyword: str = None
    language: str = "en"
    min_price: int = None
    max_price: int = None
    open_now: bool = None
    rank_by: str = None

    def toDict(self) -> dict:
        return self.__dict__
