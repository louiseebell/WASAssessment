import datetime
from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    content = models.CharField(max_length=1500)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Meta:
        verbose_name_plural = 'News Stories'

        def __str__(self):
            return self.title


