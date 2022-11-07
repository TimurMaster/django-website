from django.shortcuts import render, redirect, get_object_or_404 , HttpResponse
from admin_panel.models import News
from admin_panel.decorators import *
from django.contrib.auth.decorators import login_required

@login_required
@user_is_moder
def newsView(request):
    New = News.objects.all()
    context = {
        'New': New,
    }
    return render(request, 'admin_panel/admin-news.html', context=context)

@login_required
@user_is_moder
def newsEditView(request, news_id):
    new = get_object_or_404(News, pk=news_id)
    context = {
        'new': new,
    }
    if request.method == 'POST':
        type = request.POST['form']
        if type == 'edit':
            title = request.POST['title']
            description = request.POST['description']
            text = request.POST['text']
            image = request.FILES.get('img')
            New = new
            New.title = title
            New.description = description
            New.img = image
            New.text = text
            New.save()
        if type == 'delete':
            new.delete()
            return redirect('admin-news')
    return render(request, 'admin_panel/admin-news-edit.html', context=context)

@login_required
@user_is_moder
def newsAddView(request):
    context = {
    }
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        text = request.POST['text']
        image = request.FILES.get('img')
        New = News.objects.create(title=title, description=description, text=text, img=image)
        New.title = title
        New.description = description
        New.text = text
        New.save()
        context['error'] = 0
        return render(request, 'admin_panel/admin-news-add.html', context=context)
    return render(request, 'admin_panel/admin-news-add.html', context=context)
