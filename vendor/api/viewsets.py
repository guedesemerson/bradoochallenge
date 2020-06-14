from rest_framework.viewsets import ModelViewSet
from vendor.models import Vendor
from .serializers import VendorPostSerializer, VendorNormalToSerializer
class VendorViewSet(ModelViewSet):

    queryset = Vendor.objects.all()
    serializer_class = VendorNormalToSerializer

    def get_serializer_class(self):
        actions = [
            'create'
        ]
        if self.action in actions:
            return VendorPostSerializer
        else:
            return self.serializer_class
    #filter_backends = (SearchFilter,)
    #search_fields = ['address',]