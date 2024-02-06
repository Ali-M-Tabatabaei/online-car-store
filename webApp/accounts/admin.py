from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Own)
admin.site.register(Purchased)
admin.site.register(Cart)
admin.site.register(ForSale)
admin.site.register(Sold)