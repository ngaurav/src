from django.contrib import admin
from .models import Collect

class CollectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Collect, CollectAdmin)
