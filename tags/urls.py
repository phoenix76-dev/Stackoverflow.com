from django.conf.urls import url
from .views import render_tags_list

urlpatterns = [
    url(r'^', render_tags_list, name='tags_list'),
]
