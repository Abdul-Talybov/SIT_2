from django.urls import path
from .views import (
    result_create,
    result_update,
    result_delete,
)

urlpatterns = [
    path("results/add/", result_create, name="result_add"),
    path("results/<int:pk>/edit/", result_update, name="result_edit"),
    path("results/<int:pk>/delete/", result_delete, name="result_delete"),
]
