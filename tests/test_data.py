from service_management.dtos.service_dto import ServiceDTO, ServiceListDTO

GET_SERVICE_DATA = {
    'search_by': 'name',
    'search_value': '',
    'sort_by': 'name',
    'page_size': 25
}

SERVICE_RESPONSE_DATA = {
    'name': 'Test service',
    'os_platform': 'Test platform',
    'price': 500,
    'description': 'Test service description'

}
SERVICE_MOCK = ServiceDTO(**SERVICE_RESPONSE_DATA)
SERVICE_LIST_MOCK = ServiceListDTO([SERVICE_MOCK])
SERVICE_LIST_MOCK_JSON = SERVICE_LIST_MOCK.to_json()
