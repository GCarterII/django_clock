from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.clock),
    url(r'^time_display$', views.clock)
]