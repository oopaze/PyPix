from django.db.models.query_utils import Q
from rest_framework import serializers
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_406_NOT_ACCEPTABLE

from transactions.models import Key, Transction
from .serializers import KeySerializer, TransctionSerializer


class KeyListAPIView(ListAPIView):
    model = Key
    serializer_class = KeySerializer
    permissions_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)


class KeyCreateAPIView(CreateAPIView):
    model = Key
    serializer_class = KeySerializer
    permissions_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def create(self, *args, **kwargs):
        if self.request.user.keys.all().count() > 2:
            return Response(
                {"error": "It's allowed just 3 keys for each user."},
                status=HTTP_406_NOT_ACCEPTABLE,
            )

        return super().create(*args, **kwargs)


class TransctionCreateAPIView(CreateAPIView):
    model = Transction
    serializer_class = TransctionSerializer
    permissions_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(sender=self.request.user)


class TransctionListAPIView(ListAPIView):
    model = Transction
    serializer_class = TransctionSerializer
    permissions_classes = [IsAuthenticated]

    def get_queryset(self):
        keys = self.request.user.keys.all().values_list("key", flat=True)
        return self.model.objects.filter(
            Q(sender=self.request.user) | Q(receiver__key__in=keys)
        )
