from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView
from rest_framework import viewsets

from .models import *
from .serializers import *


# Create your views here.
def default_view(request):
    return render(request, "jv_dj_app/index.html")

# Voyages

class VoyageViewSet(viewsets.ModelViewSet):
    queryset = Voyage.objects.all()
    serializer_class = VoyageSerializer

class VoyageListView(ListView):
    model = Voyage
    context_object_name = "voyages"
    template_name = "jv_dj_app/voyage_list_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ships'] = Ship.objects.all()
        context['captains'] = Captain.objects.all()
        context['sources'] = Source.objects.all()
        return context


class VoyageDetailView(DetailView):
    model = Voyage
    template_name = "jv_dj_app/voyage_detail_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ships'] = Ship.objects.all()
        context['captains'] = Captain.objects.all()
        context['sources'] = Source.objects.all()
        context['ports'] = Port.objects.all()
        return context

# Ships

class ShipViewSet(viewsets.ModelViewSet):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer

class ShipListView(ListView):
    model = Ship
    context_object_name = "ships"


# Port Visits

class PortVisitViewSet(viewsets.ModelViewSet):
    queryset = PortVisit.objects.all()
    serializer_class = PortVisitSerializer

class PortVisitListView(ListView):
    model = PortVisit
    context_object_name = "port_visits"

class PortDetailView(DetailView):
    model = PortVisit

# Transactions

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionListView(ListView):
    model = Transaction
    context_object_name = "transactions"

class TransactionDetailView(DetailView):
    model = Transaction

# Sources

class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

class SourceListView(ListView):
    model = Source
    context_object_name = "sources"

class SourceDetailView(DetailView):
    model = Source

# Items

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemListView(ListView):
    model = Item
    context_object_name = "items"

class ItemDetailView(DetailView):
    model = Item

# Locations

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationListView(ListView):
    model = Location
    context_object_name = "locations"

class LocationDetailView(DetailView):
    model = Location

# END OF FILE