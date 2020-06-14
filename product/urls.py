from django.urls import path
from .api.viewsets import ProductViewSet
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

    path('test_product/', ProductViewSet.as_view(list_actions), name='product_transactions'),
    path('test_product/<pk>', ProductViewSet.as_view(single_actions), name='product_transaction'),

]