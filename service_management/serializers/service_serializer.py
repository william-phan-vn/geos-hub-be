from rest_framework import serializers
from rest_enumfield import EnumField
from service_management.dtos.search_dto import SearchCriteriaEnum


class ServiceSearchSerializer(serializers.Serializer):
    search_by = EnumField(
        required=False, default=None,
        choices=SearchCriteriaEnum,
        to_choice=lambda x: (x.value, x.name),
        to_repr=lambda x: x)
    search_value = serializers.CharField(
        required=False, default=None, max_length=200)
    sort_by = EnumField(
        required=False, default=SearchCriteriaEnum.name.value,
        choices=SearchCriteriaEnum,
        to_choice=lambda x: (x.value, x.name),
        to_repr=lambda x: x)
    page_size = serializers.IntegerField(
        required=False, default=25)
