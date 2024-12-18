from django.urls import path
from .views import *

urlpatterns=[
    path('supplierdetails/',SupplierView.as_view(),name='supplier_details'),
    path('supplierupdate/<int:id>/',SupplierView.as_view(),name='supplier_edit'),
    path('supplierdelete/<int:id>/',SupplierView.as_view(),name='supplier_delete')

]