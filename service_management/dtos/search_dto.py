from enum import Enum
from dataclasses import dataclass

MAP_CRITERIA = {
    'os_platform': 'os_platform__name',
    'name': 'service__name',
    'price': 'price'
}


class SearchCriteriaEnum(Enum):
    OS_PLATFORM = 'os_platform'
    name = 'name'
    price = 'price'


@dataclass
class SearchDTO:
    search_by: str
    search_value: str
    sort_by: str
    page_size: int

    def __post_init__(self):
        self.search_by = MAP_CRITERIA[self.search_by]
        self.sort_by = MAP_CRITERIA[self.sort_by]
