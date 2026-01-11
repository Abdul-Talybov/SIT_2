import pandas as pd
from django.core.management.base import BaseCommand
from app.models import Driver, Constructor, Circuit, Event, Result

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        df = pd.read_excel("F1 data.xlsx")

        for _, row in df.iterrows():

            driver, _ = Driver.objects.get_or_create(
                forename=row["Driver's forename"],
                surname=row["Driver's surname"],
                defaults={
                    "code": row.get("code"),
                    "dob": row.get("dob"),
                    "nationality": row.get("Driver's nationality"),
                    "driver_number": row.get("Driver's  number"),
                }
            )

            constructor, _ = Constructor.objects.get_or_create(
                constructor_name=row["Constructor name"],
                defaults={
                    "constructor_nationality": row.get("constructor's nationality")
                }
            )

            circuit, _ = Circuit.objects.get_or_create(
                circuit_name=row["circuit name"],
                defaults={
                    "lat": row.get("lat"),
                    "lng": row.get("lng"),
                }
            )

            event, _ = Event.objects.get_or_create(
                year=row["year"],
                round=row["round"],
                defaults={
                    "event_name": row["Event name"],
                    "event_date": row.get("Event date"),
                    "circuit": circuit,
                }
            )

            Result.objects.create(
                event=event,
                driver=driver,
                constructor=constructor,
                grid=row.get("grid"),
                position=row.get("position"),
                positionOrder=row.get("positionOrder"),
                points=row.get("points"),
                laps=row.get("laps"),
                time=row.get("time"),
                milliseconds=row.get("milliseconds") or 0,
                fastestLap=row.get("fastestLap"),
                rank=row.get("rank"),
                fastestLapTime=row.get("fastestLapTime"),
                fastestLapSpeed=row.get("fastestLapSpeed"),
                status=row.get("status"),
            )