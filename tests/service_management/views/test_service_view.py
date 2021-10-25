from django.http import HttpResponse
from http import HTTPStatus
from unittest import TestCase
from unittest.mock import MagicMock, patch
from service_management.views import service_view


TARGET_PATH = 'service_management.views.service_view'


class ServiceViewTestCase(TestCase):
    def setUp(self) -> None:
        self.service_service_patcher = patch(f'{TARGET_PATH}.ServiceService')
        self.service_service_mock = self.service_service_patcher.start()
        self.service_service_mock.return_value.get_services.return_value = HttpResponse(status=HTTPStatus.OK)

    def tearDown(self) -> None:
        self.service_service_patcher.stop()

    def test_get_all_services_success(self):
        request = MagicMock()
        request.GET = {
            'search_by': 'name',
            'search_value': '',
            'sort_by': 'name',
            'page_size': 25
        }

        result = service_view.get_all_services(request)
        self.assertEqual(result.status_code, HTTPStatus.OK)
