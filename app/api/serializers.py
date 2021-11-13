from uuid import uuid4
from django.core.exceptions import ValidationError

from rest_framework import serializers

from transactions.models import Key, Transction


class KeySerializer(serializers.ModelSerializer):
    type = serializers.CharField(required=False, write_only=True)
    _type = serializers.CharField(source="get_type_display", read_only=True)

    def validate_key(self, data, *args, **kwargs):
        type = self.initial_data.get("type", "")
        if type != Key.RANDOM and not data:
            raise serializers.ValidationError("Key parameter is required")

        if type == Key.RANDOM:
            self.initial_data['key'] = data = str(uuid4())

        return data

    def validate(self, attrs):
        self.validate_key(attrs.get("key"))
        return super().validate(attrs)

    class Meta:
        model = Key
        fields = ("key", "type", "_type")


class TransctionSerializer(serializers.ModelSerializer):
    key = serializers.CharField(source="receiver.key")
    sender = serializers.CharField(source="sender.username", read_only=True)
    receiver = serializers.CharField(source="receiver.owner.username", read_only=True)

    def validate_key(self, data, *args, **kwargs):
        if not Key.objects.filter(key=data).exists():
            raise serializers.ValidationError("Key not found.")

        return data

    def create(self, validated_data):
        receiver = Key.objects.get(**validated_data['receiver'])
        validated_data['receiver'] = receiver
        return super().create(validated_data)

    class Meta:
        model = Transction
        fields = ("value", "key", "sender", "receiver")
