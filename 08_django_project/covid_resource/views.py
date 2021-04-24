from django.http import HttpResponse
from django.shortcuts import render

from covid_resource.models import CovidResource


# def index(request):
#     return HttpResponse('Hello World!!!')

#
# def home(request):
#     return render(request, template_name="temp/a/materialize.html")


def home(request):

    # ORM queries
    # covid_resources = CovidResource.objects.filter(content__icontains="oxygen")
    covid_resources = CovidResource.objects.all()
    return render(
        request,
        "index.html",
        {'resources': covid_resources}
    )


def about_us(request):
    return render(request, template_name="about_us.html")