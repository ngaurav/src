from django.contrib import admin

from .models import Venue

class VenueAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', )
    list_filter = ('cost_per_person','group_size')
    search_fields = ('title', 'address')

admin.site.register(Venue, VenueAdmin)
