from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from product.api.viewsets import ProductViewSet
from vendor.api.viewsets import VendorViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'vendor', VendorViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Api",
      default_version='v1',
      description="Bradoo Api",
      terms_of_service="",
      contact=openapi.Contact(email="guedes.emerson@hotmail.com"),
      license=openapi.License(name="Own License"),
   ),
   public=True,

   permission_classes=(permissions.AllowAny,),
   patterns= [
        path('api/', include(router.urls)),
        path('admin/', admin.site.urls),

    ]

)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    path('test_product/', include('product.urls')),
    path('test_vendor/', include('vendor.urls')),


]
