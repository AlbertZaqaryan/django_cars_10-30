from django.shortcuts import render
from django.views.generic import ListView
from .models import Car
# Create your views here.

class CarListView(ListView):
    template_name = 'home.html'

    def get(self, request):
        cars = Car.objects.all()
        return render(request,self.template_name, {'cars':cars})