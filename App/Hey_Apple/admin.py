from django.contrib import admin

# Register your models here.
from .models import Documento

@admin.register(Documento)
class MyClientFeatures(admin.ModelAdmin):
    search_fields = ("nome", "tipo")
    list_display = ("nome", "tipo")