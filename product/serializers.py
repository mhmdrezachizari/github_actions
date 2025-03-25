from rest_framework import serializers

from .models import PRODUCT


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = PRODUCT
        fields = '__all__'