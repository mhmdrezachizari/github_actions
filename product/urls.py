from django.urls import path
from .views import ProductViewSet
urlpatterns = [
path('data/' , ProductViewSet.as_view())
]