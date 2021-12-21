from django.db import models
from django.contrib.auth.models import User

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
    (2009, 2009),
    (2008, 2008),
    (2007, 2007),
]


class Opt(models.Model):
    opt = models.CharField(max_length=30)

    def __str__(self):
        return self.opt


class Brands(models.Model):
    brand = models.CharField(max_length=30)

    def __str__(self):
        return self.brand


class Cars(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    brand = models.ForeignKey("Brands", on_delete=models.CASCADE, related_name='brands')
    model = models.CharField(max_length=25)
    year = models.IntegerField(choices=YEAR_CHOICES)
    color = models.CharField(max_length=30)
    price = models.IntegerField(blank=True, null=True)
    mileage = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    opt = models.ManyToManyField(Opt, related_name='opt_cars')
    usr = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/cars/{self.id}"

    def get_brands_admin(self):
        brands = Brands.objects.filter(id=self.brand.id)
        return list(brands)
