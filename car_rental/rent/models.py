from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from rent.validators import validate_model_name


class Car(models.Model):
    model = models.CharField(
        max_length=20,
        validators=[validate_model_name],
        null=False,
    )
    color = models.CharField(max_length=20, blank=True)
    engine_identifier = models.CharField(max_length=20)
    price_for_a_day = models.PositiveIntegerField()

    def __str__(self):
        return self.model


class Lender(models.Model):
    lender_name = models.CharField(max_length=20)

    def __str__(self):
        return self.lender_name



class Trip(models.Model):
    client_name = models.CharField(max_length=50)
    car = models.ManyToManyField(Car, related_name="trips")
    how_many_days = models.PositiveIntegerField()
    price_for_one_day = models.PositiveIntegerField()
    start_date = models.DateTimeField(default=datetime.now, null=True)
    end_date = models.DateTimeField(default=datetime.now, null=True)
    lender = models.ForeignKey(Lender, related_name="case", on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if not self.price_for_one_day:
            self.price_for_one_day = self.car.price_for_a_day
        super().save(*args, **kwargs)



    @property
    def to_pay(self):
        return self.how_many_days * self.price_for_one_day

    def __str__(self):
        return self.client_name





