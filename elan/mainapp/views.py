from django.shortcuts import render

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
    active = 'active'
    context = {'active':active}
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

def volunteer_application_view(request):
    active = 'active'
    context = {'active':active}
    return render(request, 'mainapp/volunteer-application.html', context)