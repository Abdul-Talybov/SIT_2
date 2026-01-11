from django.db import models

class Driver(models.Model):
    code = models.CharField(max_length=10, null=True, blank=True)
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    dob = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    driver_number = models.IntegerField(null=True, blank=True)

class Constructor(models.Model):
    constructor_name = models.CharField(max_length=100)
    constructor_nationality = models.CharField(max_length=50, null=True, blank=True)

class Circuit(models.Model):
    circuit_name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

class Event(models.Model):
    year = models.IntegerField()
    round = models.IntegerField()
    event_name = models.CharField(max_length=100)
    event_date = models.DateField(null=True, blank=True)
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)

class Result(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    constructor = models.ForeignKey(Constructor, on_delete=models.CASCADE)

    grid = models.IntegerField(null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)
    positionOrder = models.IntegerField(null=True, blank=True)
    points = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    laps = models.IntegerField(null=True, blank=True)
    time = models.CharField(max_length=20, null=True, blank=True)
    milliseconds = models.IntegerField(null=True, blank=True)
    fastestLap = models.IntegerField(null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)
    fastestLapTime = models.CharField(max_length=20, null=True, blank=True)
    fastestLapSpeed = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)