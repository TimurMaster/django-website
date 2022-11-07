from django.shortcuts import render,get_object_or_404,redirect
from admin_panel.models import *
from django.core.paginator import Paginator
# Create your views here.

def newsPage(request):
    header_contacts = HeaderContact.objects.get()
    news = News.objects.all()

    address = Address.objects.all()
    phone = Phone.objects.all()
    email = Email.objects.all()
    #paginator start
    paginator = Paginator(news, 10)
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
    #paginator end
    context = {
        'header_contacts': header_contacts,
        'news': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
        'page_number': page_number,
    }
    return render(request,'front/news.html',context=context)

def newsItemPage(request,news_id):
    header_contacts = HeaderContact.objects.get()
    new = get_object_or_404(News,pk=news_id)

    address = Address.objects.all()
    phone = Phone.objects.all()
    email = Email.objects.all()
    context = {
        'header_contacts': header_contacts,
        'new': new,
        'address': address,
        'phone': phone,
        'email': email,
    }
    return render(request,'front/news-item.html',context=context)