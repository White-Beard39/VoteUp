from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
import requests
from unicodedata import category
from rest_framework import status
from rest_framework.response import Response

from .models import Category, Entity, Voted
from .serializer import (
    EntitiesForCategoriesSerializer,
    CategorySerializer,
    VoteUpSerializer,
)


class EntitiesForCategoriesView(APIView):

    def get(self, request):
        category = self.request.GET["category"]
        results = self.request.GET.get("results")
        try:
            category_obj = Category.objects.get(name=category)
        except Category.DoesNotExist:
            return Response(
                {"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND
            )

        if results and int(results) > 0:
            queryset = Entity.objects.filter(category=category_obj).order_by("-glory")[
                : int(results)
            ]
        else:
            queryset = Entity.objects.filter(category=category_obj).order_by("-glory")

        serializer = EntitiesForCategoriesSerializer(
            queryset, many=True
        )  # Serialize the queryset
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoriesViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class VoteUpView(APIView):

    def post(self, request):

        # TODO: need to add authentication and also the request should contain the user
        user = self.request.data["user"]
        category = self.request.data["category"]
        category_name = self.request.data["category_name"]

        serializer = VoteUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj, bool_created = Voted.objects.get_or_create(
            user=serializer.validated_data["user"],
            category=serializer.validated_data["category"],
        )

        if obj and (bool_created == False):
            return Response(
                {"message": "Updated the object"}, status=status.HTTP_201_CREATED
            )
        elif obj and (bool_created == True):
            return Response(
                {"message": "Created the response"}, status=status.HTTP_200_OK
            )
