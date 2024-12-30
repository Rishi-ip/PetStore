from django.contrib import admin
from.models import pet,customer,cart,adminmodel

# Register your models here.
admin.site.register(pet)
admin.site.register(customer)
admin.site.register(cart)
admin.site.register(adminmodel)