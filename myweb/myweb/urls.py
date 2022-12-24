from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('contak/', include ('contak.urls')),
    path('blok/', include ('blok.urls')),
    path('bisnis/', include ('bisnis.urls')),
]
