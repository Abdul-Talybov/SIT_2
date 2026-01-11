from django.shortcuts import render
from django.db.models import Sum
from .models import Driver, Constructor, Circuit, Event, Result

def index(request):

    drivers = Driver.objects.all()
    circuits = Circuit.objects.all()
    events = Event.objects.all()
    results = Result.objects.select_related(
        "driver", "event", "constructor"
    )

    points_by_driver = (
        Result.objects
        .values("driver__surname")
        .annotate(total_points=Sum("points"))
        .order_by("-total_points")
    )

    points_by_constructor = (
        Result.objects
        .values("constructor__constructor_name")
        .annotate(total_points=Sum("points"))
        .order_by("-total_points")
    )

    drivers_table = [[d.id, d.forename, d.surname, d.nationality] for d in drivers]
    circuits_table = [[c.id, c.circuit_name, c.lat, c.lng] for c in circuits]
    points_by_driver_table = [[p["driver__surname"], p["total_points"]] for p in points_by_driver]
    points_by_constructor_table = [[p["constructor__constructor_name"], p["total_points"]] for p in points_by_constructor]

    context = {
        "drivers_table": drivers_table,
        "circuits_table": circuits_table,
        "points_by_driver_table": points_by_driver_table,
        "points_by_constructor_table": points_by_constructor_table,
    }

    return render(request, "index.jinja", context)
