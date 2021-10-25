from customer_management.services.customer_service import CustomerService


def customer_login(request):
    email = request.GET['email']
    password = request.GET['password']
    customer_service = CustomerService()

    return customer_service.get_paid_services(email, password)
