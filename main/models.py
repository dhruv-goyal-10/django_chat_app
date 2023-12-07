from django.db import models


class Message(models.Model):
    group_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
