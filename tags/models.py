from django.db import models
from common import utilities


class Tag(models.Model):
    title = models.CharField(max_length=20, default='unnamed')
    description = models.TextField(default='')
    created_date = models.DateField(auto_now=True)
    questions_count = models.IntegerField(default=0)
    followers_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.title

    def get_short_followers_count(self):
        return utilities.format_number_to_present(self.followers_count)

    def get_questions_count(self):
        return utilities.format_number_to_present(self.questions_count)
