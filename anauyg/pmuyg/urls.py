from django.urls import path
from .import views

#1. aşamada url patterns oluşturulur

urlpatterns = [
    path("", views.index, name="home"),
    path("isprogramı", views.isprogramı, name = "isprogramı"),
    path("fiyatlandırma", views.fiyatlandırma, name = "fiyatlandırma"),
    path("hizmetler", views.hizmetler, name ="hizmetler"),
    path("hizmetler/<slug:slug>", views.hizmetler_detay), # hizmetlerin detayına gitmek için hizmet/slug olması gerekiyor.

]
