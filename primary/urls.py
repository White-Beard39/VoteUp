from os.path import basename

from django.shortcuts import render
from django.urls import path, include

from .models import Entity
from .views import EntitiesForCategoriesView, CategoriesViewSet, VoteUpView

urlpatterns = [
    path("entity/", EntitiesForCategoriesView.as_view()),
    path("category/", CategoriesViewSet.as_view({"get": "list"})),
    path("voteup/", VoteUpView.as_view()),
]
