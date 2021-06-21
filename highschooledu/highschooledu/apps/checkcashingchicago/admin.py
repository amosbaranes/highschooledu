from django.contrib import admin
from .models import CheckCashingWeb, Location, Currency, Partner, Service


@admin.register(CheckCashingWeb)
class CheckCashingWebAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'name', 'domain_name',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'location_heading', 'location_info',)


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'currency_header', 'currency_description',)


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'partner_description',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'title', 'description')