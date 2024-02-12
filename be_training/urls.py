from django.urls import path, include
from .views import hello_world, hello_world2, ItemViewSet, get_all_items, update_item, delete_item, create_item
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/items/<int:pk>/', ItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='item-detail'),
    path('api/get_all_items/', get_all_items, name='get-all-items'),
    path('api/update_item/<int:pk>/', update_item, name='update-item'),
    path('api/delete_item/<int:pk>/', delete_item, name='delete-item'),
    path('api/create_item/', create_item, name='create-item'),  # Thêm đường dẫn cho API tạo một mục mới
    path('hello/', hello_world, name='hello_world'),
    path('hello2/', hello_world2, name='hello_world2'),
]
