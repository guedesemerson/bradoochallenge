from django.urls import path
from .api.viewsets import VendorViewSet
list_actions = {
    'get': 'list',
    'post': 'create'
}

single_actions = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}

urlpatterns = [

    path('test_vendor/', VendorViewSet.as_view(list_actions), name='vendor_transactions'),
    path('test_vendor/<pk>', VendorViewSet.as_view(single_actions), name='vendor_transaction'),
]