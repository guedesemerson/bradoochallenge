from rest_framework.viewsets import ModelViewSet
from product.models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):

        vendor = self.request.query_params.get('vendor')


        if vendor :
            queryset = Product.objects.filter(vendor=vendor, )
            serializer = ProductSerializer(queryset, many=True)
            return Response(serializer.data)

        else:
            queryset = self.get_queryset()
            serializer = ProductSerializer(queryset, many=True)
            return Response(serializer.data)
