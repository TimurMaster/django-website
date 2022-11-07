from django.shortcuts import render, redirect, get_object_or_404 , HttpResponse
from admin_panel.decorators import *
from django.contrib.auth.decorators import login_required

@login_required
@user_is_moder
def adminPanelView(request):
    context = {

    }

    return render(request, 'admin_panel/admin-panel.html', context=context)