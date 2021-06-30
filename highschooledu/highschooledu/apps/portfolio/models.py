from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from cms.models.fields import PlaceholderField


class PortfolioWeb(models.Model):
    class Meta:
        verbose_name = _('portfolio')
        verbose_name_plural = _('portfolios')
        ordering = ['order']

    order = models.IntegerField(default=1000, null=True, blank=True)
    portfolio_name = models.CharField(max_length=100, null=True, blank=True)
    domain_name = models.CharField(max_length=100, null=True, blank=True)
    welcome_phrase1 = models.CharField(max_length=100, null=True, blank=True)
    welcome_phrase2 = models.CharField(max_length=100, null=True, blank=True)
    main_image = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    logo_name = models.CharField(max_length=100, null=True, blank=True)
    footer_phrase = models.CharField(max_length=100, null=True, blank=True)
    Short_description = models.CharField(max_length=200, null=True, blank=True)
    portfolio_link = models.CharField(max_length=100, null=True)

    copyright_year = models.CharField(max_length=100, null=True, blank=True)
    copyright_phrase = models.CharField(max_length=100, null=True, blank=True)

    service_title = models.CharField(max_length=100, null=True, blank=True)
    service_phrase = models.CharField(max_length=100, null=True, blank=True)

    project_title = models.CharField(max_length=100, null=True, blank=True)

    about_title = models.CharField(max_length=100, null=True, blank=True)
    about_phrase = models.CharField(max_length=100, null=True, blank=True)
    about_subtitle = models.CharField(max_length=100, null=True, blank=True)
    about_link = models.CharField(max_length=100, null=True, blank=True)
    about_image = models.ImageField(upload_to='about/', blank=True, null=True)

    contact_title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.portfolio_name


class Service(models.Model):
    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')
        ordering = ['order']

    portfolio_web = models.ForeignKey(PortfolioWeb, on_delete=models.CASCADE, default=1, related_name='services')
    order = models.IntegerField(default=1000, blank=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    heading = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)


class Project(models.Model):
    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')
        ordering = ['order']

    portfolio_web = models.ForeignKey(PortfolioWeb, on_delete=models.CASCADE, default=1, related_name='projects')
    order = models.IntegerField(default=1000, blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    heading = models.CharField(max_length=100, null=True)
    sub_heading = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)


class Contact(models.Model):
    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
        ordering = ['order']

    portfolio_web = models.ForeignKey(PortfolioWeb, on_delete=models.CASCADE, default=1, related_name='contacts')
    order = models.IntegerField(default=1000, blank=True)
    image = models.ImageField(upload_to='contacts/', blank=True, null=True)
    phone1 = models.CharField(max_length=100, null=True)
    phone2 = models.CharField(max_length=100, null=True)
    email1 = models.CharField(max_length=100, null=True)
    email2 = models.CharField(max_length=100, null=True)
    address1 = models.CharField(max_length=100, null=True)
    address2 = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
