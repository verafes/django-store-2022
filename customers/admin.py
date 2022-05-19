from django.contrib import admin
from .models import Customer, CustomerAddress

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'email', 'time_created', 'user_id']


class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'country', 'city', 'address', 'post_code', 'customer']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerAddress, CustomerAddressAdmin)