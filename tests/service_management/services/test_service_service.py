import json
from unittest import TestCase
from unittest.mock import patch

from service_management.dtos.search_dto import SearchDTO
from service_management.services.service_service import ServiceService
from tests.test_data import GET_SERVICE_DATA, SERVICE_LIST_MOCK, SERVICE_RESPONSE_DATA

TARGET_PATH = 'service_management.services.service_service'


class ServiceServiceTestCase(TestCase):
    def setUp(self) -> None:
        self.service_repo_patcher = patch(f'{TARGET_PATH}.ServiceRepository')
        self.service_repo_mock = self.service_repo_patcher.start()

    def tearDown(self) -> None:
        self.service_repo_patcher.stop()

    def test_get_service_success(self):
        search = SearchDTO(**GET_SERVICE_DATA)
        self.service_repo_mock.return_value.get_services.return_value = SERVICE_LIST_MOCK

        response = ServiceService().get_services(search)
        services_result = json.loads(response.content.decode('utf-8'))['services']
        self.assertEqual(len(services_result), len(SERVICE_LIST_MOCK.services))
        self.assertEqual(services_result[0]['name'], SERVICE_RESPONSE_DATA['name'])
        self.assertEqual(services_result[0]['os_platform'], SERVICE_RESPONSE_DATA['os_platform'])
        self.assertEqual(services_result[0]['price'], SERVICE_RESPONSE_DATA['price'])
        self.assertEqual(services_result[0]['description'], SERVICE_RESPONSE_DATA['description'])
