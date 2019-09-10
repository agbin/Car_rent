from django.db import models
from datetime import datetime




class Car(models.Model):
    model = models.CharField(max_length=20, blank=True)
    color = models.CharField(max_length=20, blank=True)
    engine_identifier = models.CharField(max_length=20)
    price_for_a_day = models.IntegerField(null=True)

    def __str__(self):
        return self.model



class Lender(models.Model):
    lender_name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.lender_name



class Trip(models.Model):
    client_name = models.CharField(max_length=50, blank=True)
    car = models.ManyToManyField(Car, blank=True, default=1, related_name="trips")
    how_many_days = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.price_for_one_day:
            self.price_for_one_day = self.car.price_for_a_day
        super(Trip, self).save(*args, **kwargs)

    price_for_one_day = models.IntegerField()

    @property
    def to_pay(self):
        return self.how_many_days * self.price_for_one_day

    start_date = models.DateTimeField(default=datetime.now, null=True)
    end_date = models.DateTimeField(default=datetime.now, null=True)
    lender = models.ForeignKey(Lender, blank=True, null= True, default=1, related_name="case", on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name





