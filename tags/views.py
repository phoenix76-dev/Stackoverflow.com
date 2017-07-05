from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseNotFound
from .models import Tag


def get_tag_list(request):
    pass


def ajax_get_tag_sticker(request, tag_id):
    tag_obj = Tag.objects.get(id=tag_id)
    if tag_obj:
        followers = str(tag_obj.followers_count)
        questions = str(tag_obj.questions_count)
        description = tag_obj.description
        description = description.replace("'", "\'")
        response_text = ('<div class="js-hidden-tag-info">'
                         '<div class="hidden-tag-info-header">'''
                         '<p>{0} followers, {1} questions</p></div>'
                         '<p class="hidden-tag-info-description">{2)</p>'
                         '<ul class="hidden-tag-info-refs">'
                         '<li><a href="#">frequent</a></li>'
                         '<li><a href="#">info</a></li>'
                         '<li><a href="#">top users</a></li>'
                         '<li><a href="#">jobs</a></li></ul></div>')
        response_text.format(followers, questions, description)
        return HttpResponse(response_text, content_type='text/html')
    else:
        # If tag id not exists - return not found response
        return HttpResponseNotFound()
