from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class InstitutionWeb(models.Model):

    class Meta:
        verbose_name = _('institution')
        verbose_name_plural = _('institutions')
        ordering = ['order']

    order = models.IntegerField(default=1000, blank=True)
    institution_name = models.CharField(max_length=100, null=True)
    institution_short_description = models.CharField(max_length=500, null=True)
    youtube_video_address = models.CharField(max_length=500, null=True)

    address1 = models.CharField(max_length=100, null=True)
    address2 = models.CharField(max_length=100, null=True)

    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.institution_name


class Course(models.Model):

    class Meta:
        verbose_name = _('course')
        verbose_name_plural = _('courses')
        ordering = ['order']

    order = models.IntegerField(default=1000, blank=True)
    course_name = models.CharField(max_length=100, null=True)
    course_description = models.CharField(max_length=200, null=True)
    course_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    is_popular = models.BooleanField(default=True)

