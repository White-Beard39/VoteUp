from rest_framework import serializers
from .models import Entity, Category
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class EntitiesForCategoriesSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Entity
        fields = ["id", "name", "image_url"]

    def get_image_url(self, obj):

        if obj.image:
            return settings.MEDIA_URL + str(obj.image)
        return None


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]


class VoteUpSerializer(serializers.Serializer):

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
