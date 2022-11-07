from django.shortcuts import render,get_object_or_404,redirect
from admin_panel.models import *
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from search.tovar import search_tovar
from django.db.models import Q

def CatalogView(request):
    header_contacts = HeaderContact.objects.get()
    categories = Category.objects.filter(parent__isnull=True)
    search_query = request.GET.get('search', None)
    tovars = search_tovar(
        search_text=search_query,
    )
    address = Address.objects.all()
    phone = Phone.objects.all()
    email = Email.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email_form = request.POST['email']
        email = EmailMessage(
            'Заявка с сайта renkaz',
            '1. ' + str(name) + '\n' +
            '2. ' + str(phone) + '\n' +
            '3. ' + str(email_form) + '\n'
            ,
            'renkaz_mailer@mail.ru',
            ['sales@renkaz.kz']
        )
        email.send()
        return redirect('thanks')
    context = {
        'header_contacts': header_contacts,
        'categories': categories,
        'address': address,
        'phone': phone,
        'email': email,
        'tovars': tovars,
    }
    return render(request,'front/catalog.html',context=context)

def CatalogItemView(request,category_id):
    header_contacts = HeaderContact.objects.get()
    categories = Category.objects.filter(parent__isnull=True)
    category = get_object_or_404(Category,pk=category_id)
    category_tables = CategoryTableValue.objects.all()
    tovar_images = TovarImages.objects.all()
    tovars = Tovar.objects.all()

    address = Address.objects.all()
    phone = Phone.objects.all()
    email = Email.objects.all()
    context = {
        'header_contacts': header_contacts,
        'categories': categories,
        'category': category,
        'tovars': tovars,
        'category_tables': category_tables,
        'tovar_images': tovar_images,
        'address': address,
        'phone': phone,
        'email': email,
    }
    return render(request, 'front/catalog-item.html', context=context)

def CatalogSearchView(request):
    header_contacts = HeaderContact.objects.get()
    categories = Category.objects.filter(parent__isnull=True)
    search_query = request.GET.get('search', None)
    tovars = search_tovar(
        search_text=search_query,
    )
    address = Address.objects.all()
    phone = Phone.objects.all()
    email = Email.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email_form = request.POST['email']
        email = EmailMessage(
            'Заявка с сайта renkaz',
            '1. ' + str(name) + '\n' +
            '2. ' + str(phone) + '\n' +
            '3. ' + str(email_form) + '\n'
            ,
            'renkaz_mailer@mail.ru',
            ['sales@renkaz.kz']
        )
        email.send()
        return redirect('thanks')
    context = {
        'header_contacts': header_contacts,
        'categories': categories,
        'address': address,
        'phone': phone,
        'email': email,
        'tovars': tovars,
    }
    return render(request,'front/catalog-search.html',context=context)
