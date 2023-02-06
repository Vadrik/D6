from datetime import datetime
from django.db import models


class News(models.Model):
    date = models.DateTimeField(default=datetime.now)
    name = models.CharField(max_length=50,unique=True)
    description = models.TextField(default = "News post")

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'
