from enum import Enum
from typing import Optional
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
    sort_by: str
    page_size: int
    search_by: Optional[str]
    search_value: Optional[str]

    def __post_init__(self):
        self.sort_by = MAP_CRITERIA[self.sort_by]
        if self.search_value not in [None, '']:
            self.search_by = MAP_CRITERIA[self.search_by]
        else:
            self.search_by = None
