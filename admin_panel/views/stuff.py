from django.shortcuts import render,redirect, get_object_or_404
from admin_panel.models import Category, FAQ, Contact, Project, Partner, Client, Address, Phone, Email, ProjectImages, HeaderContact
from admin_panel.decorators import *
from django.contrib.auth.decorators import login_required
from search.users import *


@login_required
@user_is_moder
def faqView(request):
    fq = FAQ.objects.all()
    if request.method == 'POST':
        question = request.POST['question']
        answer = request.POST['answer']
        FAQ.objects.create(question=question, answer=answer)

    context ={
        'faq': fq,
    }
    return render(request, 'admin_panel/admin-faq.html',context=context)

@login_required
@user_is_moder
def faqEditView(request,faq_id):
    fq = get_object_or_404(FAQ,pk=faq_id)
    if request.method == 'POST':
        type = request.POST['form']
        if type == 'edit':
            question = request.POST['question']
            answer = request.POST['answer']
            fq.question = question
            fq.answer = answer
            fq.save()
            return redirect('faq')
        if type == 'delete':
            fq.delete()
            return redirect('faq')
    context ={
        'faq': fq,
    }
    return render(request, 'admin_panel/admin-faq.html',context=context)

@login_required
@user_is_moder
def ContactsView(request):
    contacts = Contact.objects.all()
    address = Address.objects.all()
    phone = Phone.objects.all()
    email = Email.objects.all()
    if request.method == 'POST':
        type = request.POST['type']
        if type == 'address':
            address = request.POST['address']
            Address.objects.create(address=address)
            return redirect('admin-contacts')
        if type == 'phone':
            phone = request.POST['phone']
            Phone.objects.create(phone=phone)
            return redirect('admin-contacts')
        if type == 'email':
            email = request.POST['email']
            Email.objects.create(email=email)
            return redirect('admin-contacts')
    context = {
        'contacts': contacts,
        'address': address,
        'email': email,
        'phone': phone,
    }
    return render(request, 'admin_panel/admin-contacts.html', context=context)

@login_required
@user_is_moder
def ConctacsEditView(request,contact_id):
    if request.method == 'POST':
        type = request.POST['form']
        if type == 'address-edit':
            address = request.POST['address']
            ad_obj = get_object_or_404(Address,pk=contact_id)
            ad_obj.address=address
            ad_obj.save()
            return redirect('admin-contacts')
        if type == 'phone-edit':
            phone = request.POST['phone']
            ad_obj = get_object_or_404(Phone,pk=contact_id)
            ad_obj.phone=phone
            ad_obj.save()
            return redirect('admin-contacts')
        if type == 'email-edit':
            email = request.POST['email']
            ad_obj = get_object_or_404(Email,pk=contact_id)
            ad_obj.email=email
            ad_obj.save()
            return redirect('admin-contacts')
        if type == 'address-delete':
            address_pk = request.POST['address_pk']
            address = get_object_or_404(Address,pk=address_pk)
            address.delete()
        if type == 'phone-delete':
            phone_pk = request.POST['phone_pk']
            phone = get_object_or_404(Phone,pk=phone_pk)
            phone.delete()
        if type == 'email-delete':
            email_pk = request.POST['email_pk']
            email = get_object_or_404(Email,pk=email_pk)
            email.delete()

    context = {
    }
    return redirect('admin-contacts')

@login_required
@user_is_moder
def PartnerView(request):
    partners = Partner.objects.all()
    if request.method == 'POST':
        type = request.POST['type']
        if type == 'partner-add':
            img = request.FILES.get('img')
            if img is None:
                return redirect('admin-partners')
            else:
                Partner.objects.create(img=img)
                return redirect('admin-partners')
        if type == 'partner-delete':
            partner_pk = request.POST['partner_pk']
            partner = get_object_or_404(Partner,pk=partner_pk)
            partner.delete()
            return redirect('admin-partners')
    context = {
        'partners': partners,
    }
    return render(request,'admin_panel/admin-partners.html',context=context)

@login_required
@user_is_moder
def ClientsView(request):
    clients = Client.objects.all()
    if request.method == 'POST':
        type = request.POST['type']
        if type == 'client-add':
            img = request.FILES.get('img')
            if img is None:
                return redirect('admin-clients')
            else:
                Client.objects.create(img=img)
                return redirect('admin-clients')
        if type == 'client-delete':
            client_pk = request.POST['client_pk']
            client = get_object_or_404(Client,pk=client_pk)
            client.delete()
            return redirect('admin-clients')
    context = {
        'clients': clients,
    }
    return render(request,'admin_panel/admin-clients.html',context=context)


@login_required
@user_is_moder
def ProjectsView(request):
    projects = Project.objects.all()
    project_image = ProjectImages.objects.all()
    if request.method == 'POST':
        type = request.POST['type']
        if type == 'project-add':
            img = request.FILES.get('img')
            main = request.FILES.get('main')
            text = request.POST['text']
            descript = request.POST['descript']
            if img is None and main is None:
                return redirect('admin-projects')
            else:
                proj = Project.objects.create(Text=text,descript=descript)
                ProjectImages.objects.create(project=proj,img=img,main=main)
                return redirect('admin-projects')
        if type == 'project-delete':
            project_pk = request.POST['project_pk']
            project = get_object_or_404(Project,pk=project_pk)
            project.delete()
            return redirect('admin-projects')
    context = {
        'projects': projects,
        'project_image': project_image,
    }
    return render(request,'admin_panel/admin-projects.html',context=context)


@login_required
@user_is_moder
def HeaderInfoView(request):
    contacts = HeaderContact.objects.get()
    if request.method == 'POST':
        type = request.POST['form']
        if type == 'add':
            worktime = request.POST['worktime']
            adress = request.POST['adress']
            city = request.POST['city']
            phone = request.POST['phone']
            email = request.POST['email']
            holidaytime = request.POST['holidaytime']
            try:
                header = HeaderContact.objects.get(pk=1)
                header.worktime=worktime
                header.adress=adress
                header.city=city
                header.phone=phone
                header.email=email
                header.holidaytime=holidaytime
                header.save()
            except HeaderContact.DoesNotExist:
                HeaderContact(worktime=worktime,adress=adress,city=city,email=email,phone=phone,holidaytime=holidaytime).save()
            return redirect('header')
    context ={
        'contacts': contacts,
    }
    return render(request,'admin_panel/admin-header-info.html',context=context)

def sosView(request):
    if request.method == 'POST':
        cat_id = int(request.POST['sos'])
        cat = Category.objects.get(pk=cat_id)
        cat.delete()
    context={

    }
    return render(request,'admin_panel/kosyak.html',context=context)

def UsersView(request):
    search_query = request.GET.get('search', None)
    users = search_users(
        search_text=search_query,
    )

    context ={
        'users':users
    }
    return render(request,'admin_panel/admin-users.html',context)