from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^', get_tag_list, name='tags_list'),
    url(r'^ajax_get_min_tags_sticker?tag_id=(?P<tag_id>\s)', ajax_get_tag_sticker)
]
