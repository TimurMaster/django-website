from admin_panel.models.tovar import *
import re
from operator import or_
from functools import reduce
from django.db.models import Q, F

search_fields = [
    'id',
    'name',
    'description',
    'short_description',
]


def search_tovar(
        search_text=None,
        categories=None,
        properties=None,
):
    qs = Tovar.objects.all().prefetch_related(
        'categories',
    ).all()

    if categories:
        for category in categories:
            if category.parent:
                qs = qs.filter(Q(categories__category=category) | Q(categories__category=category.parent))
            else:
                qs = qs.filter(categories__category=category)

    if properties:
        qs = qs.filter(categories__category__properties__in=properties)

    if search_text:
        words = re.sub("[^\w]", "", search_text).split()
        q = Q()
        for search_field in search_fields:
            for word in words:
                q |= Q(**{f'{search_field}__contains': word.lower()})
        qs = qs.filter(q)

    return qs
