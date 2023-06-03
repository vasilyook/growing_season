from django.forms import ModelForm
from .models import Seed
from django import forms


class SeedForm(ModelForm):
    stratification = forms.BooleanField(required=False)

    class Meta:
        model = Seed
        fields = ['name', 'sow_way', 'type', 'stratification', 'sow_start', 'sow_end', 'expired_on', 'image']
