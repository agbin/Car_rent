from django.test import TestCase
from rent.models import Trip, Lender, Car
from django.core.exceptions import ValidationError
import unittest


class CarModelTest(TestCase):
    def test_model(self):
        car = Car.objects.create(model="Mazda", color="blue", engine_identifier="xx34df", price_for_a_day=24)
        self.assertEqual(car.model, "Mazda")

    def test_model_None(self):
        car = Car.objects.create(model=None, color="blue", engine_identifier="xx34df", price_for_a_day=24)
        # self.assert()



class TripModelTest(TestCase):
    def setUp(self):
        self.test_lender = Lender.objects.create(lender_name="employee 1")
        self.test_lender.save()
        self.test_car = Car.objects.create(model="Mazda", color="blue", engine_identifier="xx34df", price_for_a_day=24)
        self.test_car.save()


    @unittest.skip('skipped')
    def test_invalid_start_date(self):
        with self.assertRaises(ValidationError) as e:
            Trip.objects.create({
                "lender": self.test_lender,
                "car": self.test_car,
                "client_name": "client 1",
                "how_many_days": 45,
                "price_for_one_day": 20,
                "start_date": "2019-10-12",
                "end_date": "2019-10-10",
            })
            self.assertIn("start_date", e.fields)

        # Trip.objects.create(
        #     lender=self.test_lender.id,
        # )

    # def test_invalid_lender(self):
    #     invalid_lender = [None, "", 8127364, {}, [], (), -123]
    #     for value in invalid_lender:
    #         with self.assertRaises(Exception):
    #             Trip.objects.create(
    #                 lender=value,
    #             )