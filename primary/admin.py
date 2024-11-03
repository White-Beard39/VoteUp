from django.contrib import admin
from primary.models import Category, Entity, Voted


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin) :
    list_display = ["id", "name"]

@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin) :
    list_display = ["id", "name", "image"]
    raw_id_fields = ("category",)

@admin.register(Voted)
class VotedAdmin(admin.ModelAdmin) :
    raw_id_fields = ("user", "category")
