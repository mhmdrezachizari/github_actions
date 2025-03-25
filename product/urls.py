from django.urls import path
from .views import ProductViewSet
urlpatterns = [
path('dataa/' , ProductViewSet.as_view())
]
