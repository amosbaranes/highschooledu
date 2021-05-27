from django.shortcuts import render
from ..webcompanies.models import WebCompanies
from django.core.mail import EmailMessage
from django.http import JsonResponse
from ..webcompanies.WebCompanies import WebSiteCompany


def home(request):
    wsc = WebSiteCompany(request)
    if wsc.is_registered_domain():
        web_company_id = wsc.web_site_company['web_company_id']
        web_company = WebCompanies.objects.get(id=web_company_id)
    else:
        web_company = WebCompanies.objects.get(id=7)

    institution = web_company.target
    return render(request, 'education/home.html', {'institution_obj': institution})

