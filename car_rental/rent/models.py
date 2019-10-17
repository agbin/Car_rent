from django.db import models
from datetime import datetime
from .validators import validate_model, validate_model_is_not_digit, validate_client_name, \
    validate_client_name_is_not_digit, validate_color, validate_color_is_not_digit




class Car(models.Model):
    model = models.CharField(max_length=100, validators=[validate_model, validate_model_is_not_digit])
    color = models.CharField(max_length=20, blank=True, validators=[validate_color, validate_color_is_not_digit])
    engine_identifier = models.CharField(max_length=20)
    price_for_a_day = models.IntegerField()

    def __str__(self):
        return self.model



class Lender(models.Model):
    lender_name = models.TextField(max_length=20)


    def __str__(self):
        return self.lender_name



class Trip(models.Model):
    client_name = models.TextField(max_length=50, validators=[validate_client_name, validate_client_name_is_not_digit])
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





