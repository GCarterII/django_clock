from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.word),
    url(r'^clear$', views.clear),
    url(r'^(?P<len>\d+)/$', views.word)
]