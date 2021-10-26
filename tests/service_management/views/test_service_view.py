from django.http import HttpResponse
from http import HTTPStatus
from unittest import TestCase
from unittest.mock import MagicMock, patch
from service_management.views import service_view
from tests.test_data import GET_SERVICE_DATA

TARGET_PATH = 'service_management.views.service_view'


class ServiceViewTestCase(TestCase):
    def setUp(self) -> None:
        self.service_service_patcher = patch(f'{TARGET_PATH}.ServiceService')
        self.service_service_mock = self.service_service_patcher.start()

    def tearDown(self) -> None:
        self.service_service_patcher.stop()

    def test_get_all_services_success(self):
        request = MagicMock()
        request.GET = GET_SERVICE_DATA
        self.service_service_mock.return_value.get_services.return_value = HttpResponse(status=HTTPStatus.OK)

        result = service_view.get_all_services(request)
        self.assertEqual(result.status_code, HTTPStatus.OK)
