from rest_framework import serializers
from .models import *


class SupplierDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=SupplierDetails
        fields='__all__'