from django.test import TestCase, TransactionTestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError, DataError
from django.db import transaction

# import unittest

from rent.models import Trip, Lender, Car


class CarModelTest(TestCase):
    def test_model_properties(self):
        values = [
            dict(model="mazda", color="blue", engine_identifier="xxx", price_for_a_day=10),
            dict(model="Mazda Super", color="red", engine_identifier="xxx yyy", price_for_a_day=10010),
            dict(model="model name", color="czerwony", engine_identifier="test", price_for_a_day=210),
        ]

        for value in values:
            car = Car.objects.create(**value)
            car.refresh_from_db()
            self.assertEqual(car.model, value["model"])
            self.assertEqual(car.color, value["color"])
            self.assertEqual(car.engine_identifier, value["engine_identifier"])
            self.assertEqual(car.price_for_a_day, value["price_for_a_day"])

    def test_model_invalid(self):
        invalid = [
            dict(model="", color="blue", engine_identifier="xxx", price_for_a_day=10),
        ]

        for value in invalid:
            with self.assertRaises(ValidationError):
                car = Car.objects.create(**value)
                car.full_clean()

    def test_model_empty_fields(self):
        empty = [
            dict(model=None, color="red", engine_identifier="xxx yyy", price_for_a_day=10010),
            dict(model="ok", color=None, engine_identifier=None, price_for_a_day=10010),
            dict(model="ok", color="qwe", engine_identifier="xx", price_for_a_day=None),
        ]

        for value in empty:
            with transaction.atomic():
                with self.assertRaises(IntegrityError):
                    car = Car.objects.create(**value)
                    car.full_clean()

    def test_price_valid(self):
        values = [
            dict(model="xxx", color="blue", engine_identifier="xxx", price_for_a_day=0),
            dict(model="xxx", color="blue", engine_identifier="xxx", price_for_a_day=1001.18),
            dict(model="xxx", color="blue", engine_identifier="xxx", price_for_a_day=678),
            dict(model="xxx", color="blue", engine_identifier="xxx", price_for_a_day=10),
        ]
        for value in values:
            car = Car.objects.create(**value)
            car.save()
            car.refresh_from_db()
            self.assertEqual(car.price_for_a_day, int(value["price_for_a_day"]))

    def test_model_name(self):
        with self.assertRaises(DataError):
            car = Car.objects.create(
                model="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                color="blue",
                engine_identifier="xxx",
                price_for_a_day=10,
            )

    def test_engine_identifier_invalid(self):
        with self.assertRaises(DataError):
            car = Car.objects.create(
                model="xxx",
                engine_identifier="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                color="blue",
                price_for_a_day=10,
            )

    def test_price_invalid(self):
        values = [
            dict(model="xxx", color="blue", engine_identifier="xxx", price_for_a_day=-10),
            dict(model="xxx", color="blue", engine_identifier="xxx", price_for_a_day=None),
            # dict(model="xxx", color="blue", engine_identifier="xxx", price_for_a_day=10),
        ]
        for value in values:
            with transaction.atomic():
                with self.assertRaises(IntegrityError):
                    car = Car.objects.create(**value)


#    def test_model_validation(self):


class TripModelTest(TestCase):
    def setUp(self):
        self.test_lender = Lender.objects.create(lender_name="employee 1")
        self.test_lender.save()
        self.test_car = Car.objects.create(model="Mazda", color="blue", engine_identifier="xx34df", price_for_a_day=24)
        self.test_car.save()

    def test_create_tip(self):
        value = {
                "lender": self.test_lender,
                "client_name": "client 1",
                "how_many_days": 45,
                "price_for_one_day": 20,
                "start_date": "2019-01-01",
                "end_date": "2019-01-10",
        }

        trip = Trip.objects.create(**value)
        self.assertGreater(trip.id, 0)
        trip.save()

        second_car = Car.objects.create(model="second", color="blue", engine_identifier="xx34df", price_for_a_day=24)
        second_car.save()
        trip.car.add(self.test_car, second_car)
        trip.save()

        trip = Trip.objects.prefetch_related('car').filter(id=trip.id).first()
        self.assertEqual(trip.car.count(), 2)

        # Trip.objects.create(
        #     lender=self.test_lender.id,
        # )

#     # def test_invalid_lender(self):
#     #     invalid_lender = [None, "", 8127364, {}, [], (), -123]
#     #     for value in invalid_lender:
#     #         with self.assertRaises(Exception):
#     #             Trip.objects.create(
#     #                 lender=value,
#     #             )
