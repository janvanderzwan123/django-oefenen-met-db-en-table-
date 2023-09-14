from django.shortcuts import render
from django.http import HttpResponse
from .models import Events

# Create your views here.

def page(request):
        events = Events.objects.all()
        return render(request, 'index.html', {'events_list': events})
    
def search_events(request):
        query = request.GET.get('event')
        events_list = Events.objects.filter(event__icontains=query)
        return render(request, 'index.html', {'events_list': events_list})