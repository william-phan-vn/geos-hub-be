from typing import List
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass
@dataclass_json
class ServiceDTO:
    name: str
    os_platform: str
    price: int
    description: str

    def __init__(self, name: str, os_platform: str, price: int, description: str):
        self.name = name
        self.os_platform = os_platform
        self.price = price
        self.description = description


@dataclass
@dataclass_json
class ServiceListDTO:
    services: List[ServiceDTO]

    def __init__(self, services: List[ServiceDTO]):
        self.services = services
