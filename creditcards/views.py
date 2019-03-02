from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse

from . import forms, models


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = forms.CardForm()
        context = {
            'form': form
        }

        return render(request, self.template_name, context)


# Create your views here.
def index(request):
    cards = models.Card.objects.all().order_by('issuer__name', 'name')

    template_name = 'index.html'
    context = {
        'name': 'Nathan',
        'cards': cards
    }

    return render(request, template_name, context)


def redirect_view(request):
    response = redirect('/cards/')
    return response

