from django.shortcuts import render, redirect, get_object_or_404 , HttpResponse
from admin_panel.models import Tovar, TovarCategory , Category, TovarChar, TovarImages,CategoryTable,CategoryTableValue
from admin_panel.decorators import *
from django.contrib.auth.decorators import login_required

@login_required
@user_is_moder
def TovarPageView(request):
    tovars = Tovar.objects.all()
    context = {
    "tovars":tovars,
    }
    return render(request, 'admin_panel/admin-tovars.html', context=context)

@login_required
@user_is_moder
def TovarAddPageView(request):
    tovars = Tovar.objects.all()
    categories = Category.objects.filter(parent__isnull=False)
    context = {
        "categories": categories,
        "tovars": tovars,
    }
    if request.method =='POST':
        name = request.POST['name']
        description = request.POST['description']
        categories_id = request.POST.getlist('categories')
        img = request.FILES.get('img')
        tovar = Tovar.objects.create(name=name,description=description)
        for category_id in categories_id:
            category = Category.objects.get(pk=category_id)
            TovarCategory(tovar=tovar, category=category).save()
        TovarImages(tovar=tovar,img=img).save()
        context['error'] = 0
        return render(request, 'admin_panel/admin-tovars-add.html', context=context)

    return render(request, 'admin_panel/admin-tovars-add.html', context=context)

@login_required
@user_is_moder
def TovarEditPageView(request, tovar_id):
    tovar = get_object_or_404(Tovar, pk=tovar_id)
    categories = Category.objects.filter(parent__isnull=False)
    tovar_chars = TovarChar.objects.filter(tovar=tovar)
    tovar_images = TovarImages.objects.filter(tovar=tovar)
    company_categories = Category.objects.filter(
        pk__in=TovarCategory.objects.filter(tovar=tovar).values_list('category'))
    try:
        tovar_category = TovarCategory.objects.get(tovar=tovar)
    except TovarCategory.DoesNotExist:
        tovar_category = None

    table_value = CategoryTableValue.objects.all()
    context = {
        "tovar": tovar,
        'categories': categories,
        'company_categories': company_categories,
        'tovar_chars': tovar_chars,
        'tovar_images': tovar_images,
        'tovar_category': tovar_category,
        'table_value': table_value,
    }
    if request.method =='POST':
        type = request.POST['form']
        if type == 'info':
            name =  request.POST['name']
            description =   request.POST['description']
            short_description = request.POST['short_description']
            tovar.name = name
            tovar.description = description
            tovar.short_description = short_description
            tovar.save()
            context['error'] = 0
            return render(request, 'admin_panel/admin-tovars-add.html', context=context)
        if type == 'category':
            categories_id = request.POST.getlist('categories')
            company_categories = TovarCategory.objects.filter(tovar=tovar)
            for company_category in company_categories:
                company_category.delete()
            for category_id in categories_id:
                category = Category.objects.get(pk=category_id)
                TovarCategory(tovar=tovar, category=category).save()
            return redirect('tovars-edit', tovar_id)
        if type == 'char':
            char = request.POST['name']
            value = request.POST['value']
            TovarChar(tovar=tovar,key=char,value=value).save()
            return redirect('tovars-edit',tovar_id)
        if type == 'char_edit':
            char = request.POST['name']
            char_value = request.POST['value']
            char_pk = request.POST['char_pk']
            chara = TovarChar.objects.get(pk=char_pk)
            print(chara)
            chara.key= char
            chara.value = char_value
            chara.save()
            return redirect('tovars-edit',tovar_id)
        if type == 'char_delete':
            char_pk = request.POST['char_pk']
            char = TovarChar.objects.get(pk=char_pk)
            char.delete()
        if type == 'files':
            img = request.FILES.get('img')
            TovarImages(tovar=tovar,img=img).save()
            return redirect('tovars-edit',tovar_id)
        if type == 'files_delete':
            img_pk = request.POST['img_pk']
            img = TovarImages.objects.get(pk=img_pk)
            img.delete()
            return redirect('tovars-edit',tovar_id)
        if type == 'delete':
            tovar.delete()
            return redirect('tovars')
    return render(request, 'admin_panel/admin-tovars-edit.html', context=context)
