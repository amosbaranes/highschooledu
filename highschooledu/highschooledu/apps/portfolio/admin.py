from django.contrib import admin
from .models import (Service, Project, Contact,  PortfolioWeb)


@admin.register(PortfolioWeb)
class PortfolioWebAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'portfolio_name',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'description', 'heading',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'heading', 'sub_heading', 'description')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'phone1', 'phone2',)

