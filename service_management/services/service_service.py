import json
from http import HTTPStatus
from service_management.dtos.search_dto import SearchDTO
from django.http import HttpResponse

from service_management.repositories.service_repository import ServiceRepository


class ServiceService:
    def __init__(self):
        pass

    def get_services(self, search: SearchDTO) -> HttpResponse:
        try:
            service_repo = ServiceRepository()
            services = service_repo.get_services(search)
            if services is not None:
                return HttpResponse(services.to_json(), content_type='application/json')
            else:
                return HttpResponse(status=HTTPStatus.NOT_FOUND)
        except Exception as ex:
            response = ex.__str__()
            return HttpResponse(json.dumps(response), status=HTTPStatus.INTERNAL_SERVER_ERROR)
