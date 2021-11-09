from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

from .models import Model


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

    def post(self, request, **kwargs):
        if request.method == "POST":
            pass
        return render(request, 'index.html')
