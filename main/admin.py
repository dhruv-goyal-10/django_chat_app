from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ("group_name", "author", "timestamp")


admin.site.register(Message, MessageAdmin)
