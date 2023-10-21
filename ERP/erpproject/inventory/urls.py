from django.urls import path
from inventory.views import *

urlpatterns = [

    # path('', home_page),
    # path('home/', home_page),
    
    path('stock/', add_stock),
    path('save/', add_stock),

    path('supplier/', add_supplier),

    path('supplier-name/', list_of_supplier),
    path('list/supplier/', list_of_supplier, name='list_of_supplier'),
    
    path('list/stock/', list_of_stock),
    
    path('supplier/<int:supplier_id>/', supplier_detail, name='supplier_detail'),

    path('stock/<int:stock_id>/', stock_detail, name='stock_detail'),

    # path('combined_detail/', stock_and_supplier_control_card, name='combined_detail'),

    path('home/stock-supplier/', stock_and_supplier_control_card),
    path('home/{/stock-supplier/}', stock_and_supplier_control_card),
    path('stock-supplier/', stock_and_supplier_control_card),

    path('home/supplier_stock/', supplier_with_stock),
    path('home/{/supplier_stock/}', supplier_with_stock),
    path('supplier_stock/', supplier_with_stock),


    path('stock-control/', stock_control)
  
    ]