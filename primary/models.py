from django.db import models
from django.contrib.auth.models import User
import uuid


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id}-{self.name}"


class Entity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    image_url = models.URLField(max_length=2048)
    category = models.ManyToManyField(Category, related_name="entity_category")
    glory = models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.id}-{self.name}"


class Voted(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="voted_user")
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="voted_category"
    )

    def __str__(self):
        return self.id
