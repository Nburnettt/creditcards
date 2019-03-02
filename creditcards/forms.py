from django import forms
from .models import Card


class CardForm(forms.Form):

    class Meta:
        model = Card
        fields = ('issuer', 'name')
