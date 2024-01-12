from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategorySerializerViewsets, ProductSerializerViewsets



router = DefaultRouter()
router.register('category', CategorySerializerViewsets)
router.register('list', ProductSerializerViewsets)


urlpatterns = [
    path('', include(router.urls)),
]
