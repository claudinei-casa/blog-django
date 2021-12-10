from django.db import models

# Create your models here.

YEAR_CHOICES = [
    (2018, 2018),
    (2017, 2017),
    (2016, 2016),
    (2015, 2015),
    (2014, 2014),
    (2013, 2013),
    (2012, 2012),
    (2011, 2011),
    (2010, 2010),
]


class Cars(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=30)
    slug = models.SlugField(max_length=255, unique=True)
    year = models.IntegerField(choices=YEAR_CHOICES)
    color = models.CharField(max_length=30)
    price = models.IntegerField()
    mileage = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.make + ' ' + self.model
