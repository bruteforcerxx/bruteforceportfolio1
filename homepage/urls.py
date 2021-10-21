from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('contact', views.contact, name='contact'),
    path('newsletter', views.news_letter, name='news'),
    path('sitemap', views.sitemap, name='sitemap'),
    path('google', views.google, name='google'),
]
