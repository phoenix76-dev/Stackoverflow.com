from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^ajax_get_tag_sticker/', ajax_get_tag_sticker),
    url(r'^', get_tag_list, name='tags_list'),
]
