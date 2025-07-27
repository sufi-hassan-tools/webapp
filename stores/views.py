from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import StoreProfile, Product
from .serializers import StoreProfileSerializer, ProductSerializer
from .models import Store

# Placeholder view for creating a store
def create_store(request):
    """Temporary endpoint for creating stores."""
    return HttpResponse("Store creation endpoint")

# API Views
class StoreProfileAPIView(generics.RetrieveAPIView):
    queryset = StoreProfile.objects.all()
    serializer_class = StoreProfileSerializer
    lookup_field = 'profile_id' # Assuming profile_id is unique for lookup

class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        store_id = self.kwargs['store_id']
        return Product.objects.filter(store__id=store_id)


def store_detail(request, store_id):
    """Display details for a single store with its products."""
    store = get_object_or_404(Store, id=store_id)
    products = Product.objects.filter(store=store)
    return render(request, 'stores/store_detail.html', {
        'store': store,
        'products': products,
    })


# New view for selecting a store theme
def select_theme(request, store_id):
    """Display a page to choose a theme for the given store."""
    store = get_object_or_404(Store, id=store_id)
    return render(request, 'stores/select_theme.html', {'store': store})


