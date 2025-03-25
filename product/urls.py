from django.urls import path
from .views import ProductViewSet
urlpatterns = [
path('dataaa/' , ProductViewSet.as_view())
]
