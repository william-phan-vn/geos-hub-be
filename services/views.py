import json

from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse

from customer.models import Customer, PaidCustomer
from services.models import ServicePrice

CRITERIA = {
    'os_platform': 'os_platform__name',
    'name': 'service__name',
    'price': 'price'
}


def all_services(request):
    search_criteria = CRITERIA[request.GET['search']]
    search_value = request.GET['search_value']
    q = Q(**{"%s__contains" % search_criteria: search_value})

    sort_criteria = CRITERIA[request.GET['sort']]

    services = ServicePrice.objects.filter(q).order_by(sort_criteria)

    response = []
    for service in services:
        service_details = {
            'name': service.service.name,
            'os_platform': service.os_platform.name,
            'price': service.price,
            'description': service.service.description
        }
        response.append(service_details)

    return HttpResponse(json.dumps(response), content_type='application/json')


def customer_login(request):
    email = request.GET['email']
    customer = Customer.objects.get(email=email)
    if request.GET['password'] == customer.password:
        services = PaidCustomer.objects.filter(customer__email=email)

        response = []
        for service in services:
            service_details = {
                'name': service.service.service.name,
                'os_platform': service.service.os_platform.name,
                'price': service.service.price,
                'description': service.service.service.description
            }
            response.append(service_details)

        return HttpResponse(json.dumps(response), content_type='application/json')
    else:
        return HttpResponse(status=403)
