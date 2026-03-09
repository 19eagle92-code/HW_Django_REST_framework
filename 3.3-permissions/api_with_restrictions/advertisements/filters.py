from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = filters.DateFromToRangeFilter()
    status = filters.ChoiceFilter(
        choices=Advertisement._meta.get_field("status").choices
    )

    class Meta:
        model = Advertisement
        fields = ["created_at", "status"]
