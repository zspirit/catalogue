from django import forms
import datetime

class PostForm(forms.Form):
    title = forms.CharField(label='Title', max_length = 255, required=True)
    description = forms.CharField(widget=forms.Textarea , required=True)
    prix = forms.FloatField(label='Prix', required=True)
    poids = forms.FloatField(label='Poids', required=True)
    visible = forms.BooleanField(label='Visible', required=True)
    created = forms.DateField(initial=datetime.date.today)
    updated = forms.DateField(initial=datetime.date.today)