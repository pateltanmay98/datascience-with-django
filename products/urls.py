from django.urls import path

from products import views

app_name = 'products'

urlpatterns = [
    path('', views.chart_select_view, name='main-products-view')
]
