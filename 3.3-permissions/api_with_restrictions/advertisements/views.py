from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from advertisements.filters import AdvertisementFilter
from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.permissions import CustomDeleteAdvertisement
from rest_framework.response import Response


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    permission_classes = [CustomDeleteAdvertisement]

    def list(self, request, *args, **kwargs):
        filter_queryset = []
        for adv in Advertisement.objects.all():
            if (adv.draft is False) or adv.creator == request.user:
                filter_queryset.append(adv)
        serializer = AdvertisementSerializer(filter_queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.request.user.is_staff:
            return [IsAdminUser()]
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in ["destroy", "update", "partial_update"]:
            return [CustomDeleteAdvertisement()]
        return []

