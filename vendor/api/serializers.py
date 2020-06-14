from rest_framework.serializers import ModelSerializer
from product.models import Product
from vendor.models import Vendor

class VendorNormalToSerializer(ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class ProductToSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'code', 'price']

class VendorPostSerializer(ModelSerializer):

    products = ProductToSerializer(many=True)
    class Meta:
        model = Vendor
        fields = ['id','name', 'cnpj', 'city', 'products']

    def create_products(self, products, vendor):

        for product in products:
            product['vendor'] = vendor
            Product.objects.create(**product)


    def create(self, validate_data):

        products = validate_data['products']
        del validate_data['products']
        vendor = Vendor.objects.create(**validate_data)

        self.create_products(products,vendor)

        setattr(vendor, "products", products)
        return vendor