from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PRODUCT
from .serializers import productSerializer
# Create your views here.
class ProductViewSet(APIView):
    def get(self,request):
        ped = PRODUCT.objects.all()
        ser_data = productSerializer(ped, many=True)
        return Response(ser_data.data)