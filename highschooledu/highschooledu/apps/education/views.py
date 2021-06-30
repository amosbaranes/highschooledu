from django.shortcuts import render
from ..webcompanies.models import WebCompanies
from django.core.mail import EmailMessage
from django.http import JsonResponse
from ..webcompanies.WebCompanies import WebSiteCompany
from django.http import JsonResponse
from .models import Phrase, AdditionalTopic, Course


def home(request):
    wsc = WebSiteCompany(request, web_company_id=7)
    company_obj = wsc.site_company()
    phrases_ = wsc.site_company('phrases')
    topics_ = wsc.site_company('topics')
    return render(request, 'education/home.html', {'institution_obj': company_obj,
                                                   'phrases': phrases_,
                                                   'topics': topics_
                                                   })


def course_description(request, pk):
    wsc = WebSiteCompany(request, web_company_id=7)
    company_obj = wsc.site_company()
    course = Course.objects.get(id=pk)
    return render(request, 'education/course_description.html',
                  {'course': course,
                   'institution_obj': company_obj,
                   })


def get_courses(request):
    wsc = WebSiteCompany(request, web_company_id=7)
    courses = wsc.site_company('courses')
    rr = {}
    for course in courses:
        rr[str(course.id)] = {
                                'course_name': course.course_name,
                                'order': course.order,
                                'course_date': course.course_date,
                                'is_popular': course.is_popular,
                                'image_url': course.image.url,
                                'short_description': course.short_description
                                }

    return JsonResponse(rr)


def get_news(request):
    wsc = WebSiteCompany(request, web_company_id=7)
    news = wsc.site_company('news')
    rr = {}
    for new in news:
        if new.is_active:
            rr[str(new.id)] = {
                'news_title': new.news_title,
                'news_type': new.news_type,
                'order': new.order,
                'news_description': new.news_description,
                'news_type_description': new.news_type_description,
                'news_date': new.news_date,
                'is_popular': new.is_popular,
                'image_url': new.image.url
            }
    return JsonResponse(rr)


def get_program(request):
    wsc = WebSiteCompany(request, web_company_id=7)
    programs = wsc.site_company('programs')
    rr = {}
    for program in programs:
        print('-' * 50)
        rr[str(program.id)] = {
            'program_title': program.program_title,
            'order': program.order,
            'program_description': program.program_description,
            'is_popular': program.is_popular,
            'image_url': program.image.url
        }
    return JsonResponse(rr)


def get_subject(request):
    wsc = WebSiteCompany(request, web_company_id=7)
    subjects = wsc.site_company('subjects')
    rr = {}
    for subject in subjects:
        print('-' * 50)
        rr[str(subject.id)] = {
            'subject_name': subject.subject_name,
            'order': subject.order,
            'is_popular': subject.is_popular,
            'image_url': subject.image.url
        }
    return JsonResponse(rr)


def get_person(request):
    wsc = WebSiteCompany(request, web_company_id=7)
    persons = wsc.site_company('persons')
    rr = {}
    for person in persons:
        print('-' * 50)
        rr[str(person.id)] = {
            'persons_name': person.persons_name,
            'persons_duty': person.persons_duty,
            'persons_description': person.persons_description,
            'order': person.order,
            'is_popular': person.is_popular,
            'image_url': person.image.url
        }
    return JsonResponse(rr)
