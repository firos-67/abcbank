from django.contrib import admin

from bankapp.models import District,Branch,Customer

# Register your models here.

admin.site.register(District)
admin.site.register(Branch)
admin.site.register(Customer)