from django.contrib import admin
from .models import *


@admin.register(FormTemplate)
class FormTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(FormField)
class FormTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'template_name', 'field_name', 'field_type')
