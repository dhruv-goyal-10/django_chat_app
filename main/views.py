from django.shortcuts import render
from .models import Message
from .serializers import MessageSerializer
from rest_framework.generics import ListCreateAPIView


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name, user_name):
    return render(
        request, "chat/room.html", {"room_name": room_name, "user_name": user_name}
    )


class MessageAPIView(ListCreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(group_name=self.kwargs["room_name"]).order_by(
            "timestamp"
        )
