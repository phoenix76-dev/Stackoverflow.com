from django.shortcuts import render_to_response
from .models import Question


def render_questions_list(request):
    return render_to_response('questions_block.html', {'questions': Question.objects.all()})


def render_question_detail(request, question_id):
    pass
