from django.conf.urls import url, include
from . import views

urlpatterns = [
    #url(r'^$', views.home, name='home'),
    #url(r'^en/$', views.home_en, name='home_en'),
    url(r'^$', views.home_hmd, name='home_hmd'),
]
