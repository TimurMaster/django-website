from admin_panel.models.tovar import *
import re
from operator import or_
from functools import reduce
from django.db.models import Q, F
from django.contrib.auth.models import User
search_fields = [
    'id',
    'username',
]


def search_users(
        search_text=None,
):
    qs = User.objects.all()
    if search_text:
        words = re.sub("[^\w]", "", search_text).split()
        q = Q()
        for search_field in search_fields:
            for word in words:
                q |= Q(**{f'{search_field}__contains': word.lower()})
        qs = qs.filter(q)

    return qs
