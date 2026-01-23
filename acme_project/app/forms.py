from django import forms
from .models import Result

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = [
            "event",
            "driver",
            "constructor",
            "grid",
            "position",
            "points",
            "laps",
            "status",
        ]
