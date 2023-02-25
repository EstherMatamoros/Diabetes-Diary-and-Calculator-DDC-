from django.db import models


class PredResults(models.Model):
    # datetimepicker1 = models.DateTimeField()
    glucose_sp = models.FloatField()
    insulin = models.FloatField()
    meals = models.FloatField()
    glucose = models.CharField(max_length=30)
    namemeals = models.CharField(max_length=255, default='No meal')
    exeint = models.CharField(max_length=255, default='0')

    def __str__(self):
        return self.insulin