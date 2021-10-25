from django.http import HttpResponse
from service_management.dtos.search_dto import SearchDTO
from service_management.serializers.service_serializer import ServiceSearchSerializer
from service_management.services.service_service import ServiceService


def get_all_services(request) -> HttpResponse:
    data = ServiceSearchSerializer(request.GET).data

    service_search = SearchDTO(**data)
    service_service = ServiceService()

    return service_service.get_services(service_search)
