from django.urls import path
from .views import *

urlpatterns = [
    path('', FrontPageView, name='FrontPage'),
    path('catalog', CatalogView, name='Catalog'),
    path('catalog-search', CatalogSearchView, name='Catalog-search'),
    path('catalog-item/<int:category_id>', CatalogItemView, name='Catalog-item'),

    path('about', aboutView, name='about'),
    path('service', serviceView, name='service'),
    path('projects', projectsView, name='projects'),
    path('contacts', contactsView, name='contacts'),

    path('news', newsPage, name='news'),
    path('news-item/<int:news_id>', newsItemPage, name='news-item'),
    path('thanks', thanksPage, name='thanks'),
]