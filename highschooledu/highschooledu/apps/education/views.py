from django.shortcuts import render
from ..webcompanies.models import WebCompanies
from django.core.mail import EmailMessage
from django.http import JsonResponse
from ..webcompanies.WebCompanies import WebSiteCompany
from django.http import JsonResponse
from .models import Course


def home(request):
    wsc = WebSiteCompany(request)
    if wsc.is_registered_domain():
        web_company_id = wsc.web_site_company['web_company_id']
        web_company = WebCompanies.objects.get(id=web_company_id)
    else:
        web_company = WebCompanies.objects.get(id=7)

    institution = web_company.target
    return render(request, 'education/home.html', {'institution_obj': institution})


def get_courses(request):
    # course_id = request.POST.get('course_id')
    #
    # print('course_id')
    # print(course_id)
    # print('course_id')

    courses = Course.objects.all()

    rr = {}
    for course in courses:
        print('-'*50)
        rr[str(course.id)] = {
                                'course_name': course.course_name,
                                'order': course.order,
                                'course_description': course.course_description,
                                'course_date': course.course_date,
                                'is_popular': course.is_popular,
                                'image_url': course.image.url
                                }
    return JsonResponse(rr)
