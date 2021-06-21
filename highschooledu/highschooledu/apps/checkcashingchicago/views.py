from django.shortcuts import render
from ..webcompanies.models import WebCompanies
from django.core.mail import EmailMessage
from django.http import JsonResponse
from ..webcompanies.WebCompanies import WebSiteCompany
from django.http import JsonResponse
from .models import CheckCashingWeb
from .models import Currency, Partner, Location


def check_cashing(request, model=''):
    try:
        wsc = WebSiteCompany(request)
        if wsc.is_registered_domain():
            web_company_id = wsc.web_site_company['web_company_id']
            web_company = WebCompanies.objects.get(id=web_company_id)
        else:
            web_company = WebCompanies.objects.get(id=8)
    except Exception as ex:
        print(ex)

    if model != '':
        s = "objs = web_company.target."+model+".filter(is_active=True).all()"
        dic_ = {'web_company': web_company}
        exec(s, dic_)
        objs = dic_['objs']
    else:
        objs = web_company.target
    return objs


def home(request):
    company_obj = check_cashing(request)
    locations = check_cashing(request, 'locations')
    currencies = Currency.objects.all()
    partners = Partner.objects.all()
    return render(request, 'checkcashingchicago/home.html', {'company_obj': company_obj,
                                                             'currencies': currencies,
                                                             'locations': locations,
                                                             'partners': partners,
                                                             })


def location_detail(request, slug):
    company_obj = check_cashing(request)
    partners = Partner.objects.all()
    location = Location.objects.get(slug=slug)
    return render(request, 'checkcashingchicago/location_detail.html', {'location': location,
                                                                        'company_obj': company_obj,
                                                                        'partners': partners,
                                                                        })


# not used we should delete it
def get_location(request):
    locations = check_cashing(request, 'locations')
    rr = {}
    print(locations)
    for location in locations:
        print(location.image)
        rr[str(location.id)] = {
                                'location_heading': location.location_heading,
                                'order': location.order,
                                'image_url': location.image.url,
                                'location_info': location.location_info,
                                'data_ajax_id': location.data_ajax_id,
                                'grid_loop': location.grid_loop,
                                'grid_parity': location.grid_parity,
                                'south_suburbs_sort': location.south_suburbs_sort
                                }

    return JsonResponse(rr)


