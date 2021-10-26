from django.db.models import Q
from service_management.dtos.search_dto import SearchDTO
from service_management.dtos.service_dto import ServiceDTO, ServiceListDTO
from service_management.models import ServicePrice


class ServiceRepository:
    def __init__(self):
        pass

    def get_services(self, search: SearchDTO):
        if search.search_by is not None:
            q = Q(**{"%s__contains" % search.search_by: search.search_value})
            query_set = ServicePrice.objects.filter(q).order_by(search.sort_by)[:search.page_size]
        else:
            query_set = ServicePrice.objects.all().order_by(search.sort_by)[:search.page_size]

        if query_set is not None:
            services = []
            for query in query_set:
                service_details = ServiceDTO(query.service.name,
                                             query.os_platform.name,
                                             query.price,
                                             query.service.description)
                services.append(service_details)
            return ServiceListDTO(services)
        else:
            return None
