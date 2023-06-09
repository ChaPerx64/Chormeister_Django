# from typing import Any, Mapping, Optional, Type, Union
from django.forms import ModelForm, Form
from django import forms
from django.forms.utils import ErrorList
from .models import Song, SongPropertyName, SongPropertyValue, SongPerformance, Chor


class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['name']


def SongCreationFormConstructor(fieldnames: list[str]):
    attr = {'name': forms.CharField(label='Name', max_length=255)}
    for fieldname in fieldnames:
        attr.update({
            fieldname: forms.CharField(
                label=fieldname, max_length=255, required=False)
        })
    return type('SongCreationForm', (Form,), attr)


class SongPropertyNameForm(ModelForm):
    class Meta:
        model = SongPropertyName
        fields = ['name']


class SongPropertyValueForm(ModelForm):
    class Meta:
        model = SongPropertyValue
        fields = '__all__'


class SongPerformanceForm(ModelForm):
    class Meta:
        model = SongPerformance
        fields = ['dtofperformance']


class ChorForm(ModelForm):
    class Meta:
        model = Chor
        fields = '__all__' #['name', 'description']
