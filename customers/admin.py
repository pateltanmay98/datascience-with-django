from django.contrib import admin

# Register your models here.
from customers.models import Customer

admin.site.register(Customer)
