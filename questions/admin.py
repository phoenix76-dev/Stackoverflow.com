from django.contrib import admin
from .models import *


admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionComment)
admin.site.register(AnswerComment)