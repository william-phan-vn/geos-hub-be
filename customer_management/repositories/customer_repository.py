from customer_management.models import Customer, PaidCustomer


class CustomerRepository:
    email: str

    def __init__(self, email: str):
        self.email = email

    def find_customer(self):
        return Customer.objects.get(email=self.email)

    def get_paid_services(self):
        return PaidCustomer.objects.filter(customer__email=self.email)
