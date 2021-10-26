from unittest import TestCase
from unittest.mock import patch, MagicMock

from service_management.dtos.search_dto import SearchDTO
from service_management.repositories.service_repository import ServiceRepository
from tests.test_data import GET_SERVICE_DATA, SERVICE_LIST_MOCK, SERVICE_RESPONSE_DATA

TARGET_PATH = 'service_management.repositories.service_repository'


class ServiceRepositoryTestCase(TestCase):
    def setUp(self) -> None:
        self.service_price_patcher = patch(f'{TARGET_PATH}.ServicePrice')
        self.service_price_mock = self.service_price_patcher.start()
        self.query_mock = MagicMock()
        self.query_mock.service.name = SERVICE_RESPONSE_DATA['name']
        self.query_mock.os_platform.name = SERVICE_RESPONSE_DATA['os_platform']
        self.query_mock.price = SERVICE_RESPONSE_DATA['price']
        self.query_mock.service.description = SERVICE_RESPONSE_DATA['description']

    def tearDown(self) -> None:
        self.service_price_patcher.stop()

    def test_get_all_services(self):
        search = SearchDTO(**GET_SERVICE_DATA)
        self.service_price_mock.objects.all.return_value.order_by.return_value = [self.query_mock]

        result = ServiceRepository().get_services(search)
        self.assertEqual(result, SERVICE_LIST_MOCK)

    def test_get_services_by_name(self):
        search = SearchDTO(**GET_SERVICE_DATA)
        search.search_by = 'search_value'
        self.service_price_mock.objects.filter.return_value.order_by.return_value = [self.query_mock]

        result = ServiceRepository().get_services(search)
        self.assertEqual(result, SERVICE_LIST_MOCK)
