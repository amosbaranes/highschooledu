from django.contrib import admin
from .models import InstitutionWeb


@admin.register(InstitutionWeb)
class InstitutionWebAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'institution_name', 'email', 'phone', )


