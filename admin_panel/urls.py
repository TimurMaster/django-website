from django.urls import path
from .views import *


urlpatterns = [
    path('', adminPanelView, name='panel'),

    path('tovars', TovarPageView, name='tovars'),
    path('tovars-add', TovarAddPageView, name='tovars-add'),
    path('tovars-edit/<int:tovar_id>', TovarEditPageView, name='tovars-edit'),

    path('category', CategoryPageView, name='category'),
    path('category-edit/<int:category_id>', CategoryEditPageView, name='category-edit'),

    path('news', newsView, name='admin-news'),
    path('news-edit/<int:news_id>', newsEditView, name='news-edit'),
    path('news-add', newsAddView, name='news-add'),

    path('faq', faqView, name='admin-faq'),
    path('faq-edit/<int:faq_id>', faqEditView, name='faq-edit'),

    path('contacts', ContactsView, name='admin-contacts'),
    path('contacts-edit/<int:contact_id>', ConctacsEditView, name='contacts-edit'),

    path('partners', PartnerView, name='admin-partners'),
    path('clients', ClientsView, name='admin-clients'),
    path('projects', ProjectsView, name='admin-projects'),
    path('header-info', HeaderInfoView, name='header'),

    path('login', loginView, name='login'),
    path('logout', logoutView, name='logout'),

    path('users',UsersView,name='users'),

    path('sos', sosView,name='sos'),
]