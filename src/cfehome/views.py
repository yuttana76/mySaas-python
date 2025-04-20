
from django.shortcuts import render
from django.http import HttpResponse

from visits.models import PageVisit
def home_page_view(request,* args, **kwargs):

    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    
    my_title = "Welcome to CFE Home"
    my_context = {
        "page_title": my_title,
        "qs": qs,
        "page_visit_count": page_qs.count(),
        "total_page_visit_count": qs.count(),
    }
    html_template = "home.html"

    path = request.path
    print(path)


    PageVisit.objects.create(path=request.path)
    return render(request,html_template,my_context)