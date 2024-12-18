from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *


# Create your views here.

class SupplierView(APIView):
    def post(self,request):
        data=request.data
        serilaizer=SupplierDetailsSerializer(data=data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(
                {
                    "success" : True,
                    'data':serilaizer.data,
                    "message": "Supplier Created",
                    "error":None
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                    {
                        'success': False,
                        'data': None, 
                        'message': 'Supplier NOT Created',
                        'errors': serilaizer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST
                ) 
    def get(self,request):
        supplier_data=SupplierDetails.objects.all()
        serializer = SupplierDetailsSerializer(supplier_data,many=True)
        return Response(
            {
                    "success" : True,
                    'data':serializer.data,
                    "message": "Supplier List",
                    "error":None
                },
            status=status.HTTP_200_OK
        )
    

    def put(self,request,id):
        supplier_data=SupplierDetails.objects.filter(id=id).first()
        serializer=SupplierDetailsSerializer(data=request.data,instance=supplier_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'success': True,
                    'data': serializer.data, 
                    'message': 'Supplier updated',
                    'errors': None
                },
                status=status.HTTP_200_OK
            )
        else:
             return Response(
                    {
                        'success': False,
                        'data': None, 
                        'message': 'Supplier not updated',
                        'errors': serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )  
    
    def delete(self,request,id):
        supplier_data=SupplierDetails.objects.filter(id=id).first()
        supplier_data.delete()
        return Response(
                {
                    'success': True,
                    'data': None, 
                    'message': 'Supplier Deleted',
                    'errors': None
                },
                status=status.HTTP_200_OK
            )