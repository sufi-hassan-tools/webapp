from django.http import HttpResponse
from rest_framework import generics
from .models import StoreProfile, Product
from .serializers import StoreProfileSerializer, ProductSerializer

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


