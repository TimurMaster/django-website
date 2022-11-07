from django.shortcuts import render, redirect, get_object_or_404 , HttpResponse
from admin_panel.models import Category, CategoryTable
from admin_panel.decorators import *
from django.contrib.auth.decorators import login_required
@login_required
@user_is_moder
def CategoryPageView(request):
    categories = Category.objects.all()
    parents = categories.filter(parent__isnull=True)
    context = {
        'categories': categories,
        'parents': parents,
    }
    if request.method == 'POST':
        name = request.POST['name']
        parent_id = int(request.POST['parent_id'])
        img = request.FILES.get('img')
        if parent_id:
            parent = Category.objects.get(pk=parent_id)
        else:
            parent = None
        if Category.objects.filter(name=name).count():
            context['error'] = 1
        elif not name:
            context['error'] = 2
        else:
            category = Category(name=name, parent=parent,img=img)
            category.save()
            context['error'] = 0
    return render(request, 'admin_panel/admin-category.html',context=context)

@login_required
@user_is_moder
def CategoryEditPageView(request,category_id):
    category = get_object_or_404(Category,pk=category_id)
    categories = Category.objects.all()
    parents = categories.filter(parent__isnull=True)
    table = CategoryTable.objects.filter(category=category)
    context = {
    'category': category,
    'parents': parents,
    'table': table,
    }
    if request.method == 'POST':
        type = request.POST['form']
        if type == 'edit':
            name = request.POST['name']
            img = request.FILES.get('img')
            if int(request.POST['parent_id']) > 0:
                parent_id = int(request.POST['parent_id'])
                if parent_id:
                    parent = Category.objects.get(pk=parent_id)
            else:
                parent = None
            if category.name != name and Category.objects.filter(name=name).count():
                context['error'] = 1
            elif not name:
                context['error'] = 2
            else:
                category.name = name
                category.parent = parent
                category.img = img
                category.save()
                context['error'] = 0
                return redirect('category')
            return redirect('category')
        if type == 'delete':
            category.delete()
            return redirect('category')


    return render(request, 'admin_panel/admin-category-edit.html',context=context)

