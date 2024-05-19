from django.db import models

class vGame(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)
    release_year = models.IntegerField()
    rating = models.FloatField()

    def __str__(self):
        return self.title