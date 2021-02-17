from django.contrib import admin

# Register your models here.
from csvs.models import Csv

admin.site.register(Csv)
