from django.db import models

# Create your models here.
class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    date = models.DateField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()

    def __str__(self):
        return f"{self.city} - {self.date}"
