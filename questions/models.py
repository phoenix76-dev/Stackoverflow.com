from django.db import models
from django.contrib.auth.models import User
from common import utilities


class Question(models.Model):
    title = models.CharField(max_length=200, default='')
    content = models.TextField(default='')
    tags = models.ManyToManyField(Tag)
    creator = models.ForeignKey(User, on_delete=models.SET(utilities.get_null_user), null=True)
    created = models.DateTimeField(auto_now=True)
    # Last activity for this question (edited, commented)
    activity = models.DateTimeField(auto_now=True)
    # Last date of edited (important!) this question
    edited = models.DateTimeField(blank=True, null=True, default=None)
    # Displays was it edited this question
    # if question was edited - we display edited field on page, else not
    is_edited = models.BooleanField(default=False)
    question_rep = models.IntegerField(default=0)
    answers_count = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/questions/' + str(self.id) + '/'


class Answer(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET(utilities.get_null_user), null=True)
    created = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Last date of edited (important!) this answer
    edited = models.DateTimeField(blank=True, null=True, default=None)
    # Displays was it edited this answer
    # if answer was edited - we display edited field on page, else not
    is_edited = models.BooleanField(default=False)
    answer_rep = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):
        return 'Answer to question id ' + str(self.question.id)


class QuestionComment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET(utilities.get_null_user), null=True)
    created = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Displays was it edited this comment
    # if comment was edited - we display marker on page, else not
    is_edited = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Question comment'
        verbose_name_plural = 'Question comments'

    def __str__(self):
        return 'Comment id ' + str(self.id) + ' to question id ' + str(self.question.id)


class AnswerComment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET(utilities.get_null_user), null=True)
    created = models.DateTimeField(auto_now=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    # Displays was it edited this comment
    # if comment was edited - we display marker on page, else not
    is_edited = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Answer comment'
        verbose_name_plural = 'Answer comments'

    def __str__(self):
        return 'Comment id ' + str(self.id) + ' to answer id ' + str(self.answer.id)
