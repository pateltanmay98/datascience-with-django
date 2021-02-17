from django.urls import path

from customers import views

app_name = 'customers'

urlpatterns = [
    path('', views.customer_corr_view, name='main-customer-view'),
]
