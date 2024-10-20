from django.shortcuts import render, redirect

from .models import Service

# Create your views here.


def service_index(request):
    services = Service.objects.all().order_by('-id')
    context = {"services": services}
    return render(request, "service_page/service.html", context)

def service_details(request, service_id):
    service_obj = Service.objects.get(id=service_id)
    context = {"obj": service_obj}
    return render(request, "service_page/service_details.html", context)

def service_delete(request, service_id):
    service_obj = Service.objects.get(id=service_id)
    service_obj.delete()
    return redirect("services")
