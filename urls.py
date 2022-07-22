from django.contrib import admin
from .import views
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('', views.index, name='index'),
    path('question/<int:num>', views.get_question, name='question'),
    #path('', RedirectView.as_view(url='/heart/')),
]