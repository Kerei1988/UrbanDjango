from django.db.backends.utils import names_digest
from django.urls import path
from . import views

app_name = 'task5'

urlpatterns = [
    path('', views.sign_up_by_html, name='by_html'),
    path('django_sign_up/', views.sign_up_by_django, name='by_django')
]