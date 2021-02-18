from django.urls import path

from products import views

app_name = 'products'

urlpatterns = [
    path('', views.chart_select_view, name='main-products-view'),
    path('add/', views.add_purchase_view, name='add-purchase-view'),
    path('sales/', views.sales_dist_view, name='sales-view'),
]
