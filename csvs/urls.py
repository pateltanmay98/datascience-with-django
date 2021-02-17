from django.urls import path

from csvs import views

app_name = 'csvs'

urlpatterns = [
    path('', views.upload_file_view, name='upload-view'),
]
