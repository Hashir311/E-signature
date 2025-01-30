from django.db import models
from django.contrib.auth.models import User


class Drawing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="drawings")
    image = models.ImageField(upload_to="drawings/", blank=True, null=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Drawing by {self.user.username} - {self.name}"
