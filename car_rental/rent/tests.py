from django.test import TestCase
from .models import Trip, Lender, Car
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
import unittest


class CarModelTest(TestCase):
    def test_model(self):
        car = Car.objects.create(model="Mazda", color="blue", engine_identifier="xx34df", price_for_a_day=24)
        self.assertEqual(car.model, "Mazda")

    def test_model_None(self):
        with self.assertRaises(IntegrityError) as e:
            Car.objects.create(model=None, color="blue", engine_identifier="xx34df", price_for_a_day=24)
            self.assertIn("model", e.fields)




class TripModelTest(TestCase):
    def setUp(self):
        self.test_lender = Lender.objects.create(lender_name="employee 1")
        self.test_lender.save()
        self.test_car = Car.objects.create(model="Mazda", color="blue", engine_identifier="xx34df", price_for_a_day=24)
        self.test_car.save()


    # @unittest.skip('skipped')
    def test_invalid_start_date(self):
        with self.assertRaises(ValidationError) as e:
            Trip.objects.create(**{
                "lender": self.test_lender,
                # "car": self.test_car,
                "client_name": "client 1",
                "how_many_days": 45,
                "price_for_one_day": 20,
                "start_date": '2019-19-10',
                "end_date": '2019-09-12',
            })
            self.assertIn("start_date", e.fields)


    def test_invalid_end_date(self):
        with self.assertRaises(ValidationError) as e:
            Trip.objects.create(**{
                "lender": self.test_lender,
                # "car": self.test_car,
                "client_name": "client 1",
                "how_many_days": 45,
                "price_for_one_day": 20,
                "start_date": '2019-09-10',
                "end_date": '2019-19-12',
            })
            self.assertIn("end_date", e.fields)


    def test_invalid_client_name(self):
        invalid_lender = [None, "", 8127364, {}, [], (), -123]
        for value in invalid_lender:
            with self.assertRaises(Exception) as e:
                Trip.objects.create(
                    lender=self.test_lender,
                    # "car"=self.test_car,
                    client_name=value,
                    how_many_days=45,
                    price_for_one_day=20,
                    start_date='2019-09-10',
                    end_date='2019-10-12',
                )
                self.assertIn("client_name", e.fields)


class LenderModelTest(TestCase):
    def test_lender_name(self):
        lender = Lender.objects.create(lender_name="employee 1")
        self.assertEqual(lender.lender_name, "employee 1")


    def test_invalid_lender(self):
        invalid_lender = [None, "", {}, [], (), -123, 1234]
        for value in invalid_lender:
            with self.assertRaises(Exception) as e:
                Lender.objects.create(
                    lender_name=value,
                )

                self.assertIn("lender_name", e.fields)



     # Trip.objects.create(
        #     lender=self.test_lender.id,
        # )

    # def test_invalid_lender(self):
    #     invalid_lender = [None, "", 8127364, {}, [], (), -123]
    #     for value in invalid_lender:
    #         with self.assertRaises(Exception) as e:
    #             Trip.objects.create(
    #                 lender=value,
    #             )