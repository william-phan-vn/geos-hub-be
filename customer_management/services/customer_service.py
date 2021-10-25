import json

from django.http import HttpResponse
from http import HTTPStatus
from customer_management.repositories.customer_repository import CustomerRepository


class CustomerService:
    def __init__(self):
        pass

    def get_paid_services(self, email: str, password: str):
        try:
            customer_repository = CustomerRepository(email)

            customer = customer_repository.find_customer()
            if customer is not None:
                if password == customer.password:
                    services = customer_repository.get_paid_services()

                    paid_services = []
                    for service in services:
                        service_details = {
                            'name': service.service.service.name,
                            'os_platform': service.service.os_platform.name,
                            'price': service.service.price,
                            'description': service.service.service.description
                        }
                        paid_services.append(service_details)
                        return HttpResponse(json.dumps(paid_services), content_type='application/json')
                else:
                    return HttpResponse(status=HTTPStatus.FORBIDDEN)
            else:
                return HttpResponse(status=HTTPStatus.NOT_FOUND)
        except Exception as ex:
            response = ex.__str__()
            return HttpResponse(json.dumps(response), status=HTTPStatus.INTERNAL_SERVER_ERROR)
