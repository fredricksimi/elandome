from django.shortcuts import render
from .forms import ContactPageForm, VolunteerApplicationForm
from datetime import datetime, timezone
from django.utils.translation import gettext as _
# Create your views here.

def home_view(request):
    active = 'active'
    context = {'active':active}
    return render(request, 'mainapp/index.html', context)

def about_view(request):
    active = 'active'
    context = {'active':active}
    return render(request, 'mainapp/about.html', context)

def history_view(request):
    return render(request, 'mainapp/history.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactPageForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = ContactPageForm()
    active = 'active'
    context = {
        'active':active,
        'form':form
        }
    return render(request, 'mainapp/contact.html', context)

def portfolio_view(request):
    active = 'active'
    context = {'active':active}
    return render(request, 'mainapp/portfolio.html', context)

def programs_view(request):
    active = 'active'
    context = {'active':active}
    return render(request, 'mainapp/programs.html', context)

def edc_community_view(request):
    return render(request, 'mainapp/edc-community.html')

def services_view(request):
    active = 'active'
    context = {'active':active}
    return render(request, 'mainapp/services.html', context)

def application_view(request):
    if request.method == 'POST':
        form = VolunteerApplicationForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = VolunteerApplicationForm()
    active = 'active'
    context = {
        'active':active,
        'form':form
    }
    return render(request, 'mainapp/application-form.html', context)