from django.contrib import admin
from .models import InstitutionWeb, Course


@admin.register(InstitutionWeb)
class InstitutionWebAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'institution_name', 'email', 'phone', )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'course_name', 'course_date', 'is_popular', )


