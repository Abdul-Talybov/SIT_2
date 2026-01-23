from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Driver, Constructor, Circuit, Event, Result
from .forms import ResultForm

def index(request):

    drivers = Driver.objects.all()
    circuits = Circuit.objects.all()
    events = Event.objects.all()
    results_list = Result.objects.select_related(
        "driver", "event", "constructor"
    )
    last_result = Result.objects.order_by('-id').first()

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
        "results": results_list,
        "r": last_result,
    }

    return render(request, "index.jinja", context)

def result_create(request):
    if request.method == "POST":
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ResultForm()

    return render(request, "result_form.jinja", {"form": form})


def result_update(request, pk):
    result = get_object_or_404(Result, pk=pk)

    if request.method == "POST":
        form = ResultForm(request.POST, instance=result)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ResultForm(instance=result)

    return render(request, "result_form.jinja", {"form": form})


def result_delete(request, pk):
    result = get_object_or_404(Result, pk=pk)

    if request.method == "POST":
        result.delete()
        return redirect("index")

    return render(request, "result_confirm_delete.jinja", {"result": result})


