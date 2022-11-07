from django.shortcuts import render
from admin_panel.models import *
from django.core.paginator import Paginator

def aboutView(request):
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
    context={
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
    return render(request,'front/about.html',context=context)


def serviceView(request):
    header_contacts = HeaderContact.objects.get()

    address = Address.objects.all()
    phone = Phone.objects.all()
    email = Email.objects.all()
    context={
        'header_contacts': header_contacts,
        'address': address,
        'phone': phone,
        'email': email,
    }
    return render(request,'front/services.html',context=context)


def projectsView(request):
    header_contacts = HeaderContact.objects.get()
    projects = Project.objects.all()
    project_image = ProjectImages.objects.all()
    paginator = Paginator(projects, 10)

    address = Address.objects.all()
    phone = Phone.objects.all()
    email = Email.objects.all()
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''
    context={
        'header_contacts': header_contacts,
        'projects': projects,
        'project_image': project_image,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
        'page':page,
        'page_number':page_number,
        'address': address,
        'phone': phone,
        'email': email,
    }
    return render(request,'front/projects.html',context=context)

def contactsView(request):
    header_contacts = HeaderContact.objects.get()
    address = Address.objects.all()
    phone = Phone.objects.all()
    email = Email.objects.all()
    context={
        'header_contacts': header_contacts,
        'address': address,
        'phone': phone,
        'email': email,
    }
    return render(request,'front/contact.html',context=context)


def thanksPage(request):
    header_contacts = HeaderContact.objects.get()
    address = Address.objects.all()
    phone = Phone.objects.all()
    email = Email.objects.all()
    context={
        'header_contacts': header_contacts,
        'address': address,
        'phone': phone,
        'email': email,
    }
    return render(request,'front/thanks.html',context=context)

