from django.contrib.auth.decorators import login_required
from django.db import models


class Board(models.Model):
    no = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=30)
    hits = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    def board_save(self):
        self.save()
