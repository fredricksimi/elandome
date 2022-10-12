from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'mainapp/index.html')

def contact_view(request):
    return render(request, 'mainapp/contact.html')

def portfolio_view(request):
    return render(request, 'mainapp/portfolio.html')