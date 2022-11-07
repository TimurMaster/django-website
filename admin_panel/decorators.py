from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404 , HttpResponse
from .models import Card
from django.http import Http404


def user_is_admin(function):
    def wrap(request, *args, **kwargs):
        try:
            card = request.user.card
        except Card.DoesNotExist:
            card = Card(owner=request.user)
            card.save()
        if (
                card.status == Card.StatusChoices.ACTIVE and
                card.role == Card.RoleChoices.ADMINISTRATOR
        ):
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def user_is_moder(function):
    def wrap(request, *args, **kwargs):
        try:
            card = request.user.card
        except Card.DoesNotExist:
            card = Card(owner=request.user)
            card.save()
        if (
                card.status == Card.StatusChoices.ACTIVE and
                (
                        card.role == Card.RoleChoices.MODERATOR or
                        card.role == Card.RoleChoices.ADMINISTRATOR
                )
        ):
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap