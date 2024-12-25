from rest_framework import serializers
from .models import Entity, Category
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class EntitiesForCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ["id", "name", "image_url"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class VoteUpSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
