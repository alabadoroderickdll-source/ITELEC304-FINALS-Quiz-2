from django.db import models


class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    price = models.FloatField()

    def vehicle_info(self):
        return f"{self.brand} costs {self.price:.0f}"

    def __str__(self):
        return self.vehicle_info()

    class Meta:
        abstract = False   


class Car(Vehicle):
    doors = models.IntegerField(default=4)

    def vehicle_info(self):
        return f"{self.brand} Car with {self.doors} doors costs {self.price:.0f}"

    def __str__(self):
        return self.vehicle_info()


class Motorcycle(Vehicle):
    helmet_included = models.BooleanField(default=False)

    def vehicle_info(self):
        return f"{self.brand} Motorcycle costs {self.price:.0f}"

    def __str__(self):
        return self.vehicle_info()
