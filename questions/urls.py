from django.conf.urls import url
from.views import render_questions_list

urlpatterns = [
    url(r'^', render_questions_list, name='questions_list'),

]
