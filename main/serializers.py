from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["timestamp"] = instance.timestamp.strftime("%Y-%m-%d %H:%M")
        return data
