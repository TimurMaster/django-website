from django.shortcuts import render
from admin_panel.models import *

# Create your views here.

def FrontPageView(request):
    header_contacts = HeaderContact.objects.get()
    partners = Partner.objects.all()
    projects = Project.objects.all()
    project_image = ProjectImages.objects.all()
    news = News.objects.all()
    categories = Category.objects.filter(parent__isnull=True)
    clients = Client.objects.all()
    address = Address.objects.all()
    phone = Phone.objects.all()
    email = Email.objects.all()
    context = {
        'header_contacts': header_contacts,
        'partners': partners,
        'projects': projects,
        'project_image': project_image,
        'clients': clients,
        'news': news,
        'categories': categories,
        'address': address,
        'phone': phone,
        'email': email,
    }
    return render(request,'front/index.html',context=context)