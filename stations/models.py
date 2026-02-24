from django.db import models
from django.contrib.auth.models import User


class RailTrip(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Station(models.Model):

    STATUS_CHOICES = [
        ("N", "Never visited"),
        ("PASS", "Train stopped, stayed on"),
        ("ALIGHT", "Got off train"),
    ]

    crs_code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=200)
    toc = models.CharField(max_length=200)

    visited_status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="N"
    )

    date_first_pass = models.DateField(null=True, blank=True)
    date_first_alight = models.DateField(null=True, blank=True)

    latitude = models.FloatField()
    longitude = models.FloatField()

    network_rail_region = models.CharField(max_length=200)
    county = models.CharField(max_length=200)

    rail_trip = models.ForeignKey(
        RailTrip,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.name} ({self.crs_code})"


class Amendment(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    field_changed = models.CharField(max_length=100)
    old_value = models.CharField(max_length=200)
    new_value = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Amendment for {self.station}"
