from django.contrib import admin
from .models import Person

# Register your models here.
admin.site.register(Person)

class PersonAdmin(admin.ModelAdmin):   # new
    list_display = ('acc', 'amount', 'tel', 'address', 'account')
    list_filter = ('acc', 'amount', 'tel', 'address', 'account')

    fieldsets = (
        (None, {
            'fields': ('acc', 'amount', 'tel', 'address', 'account')
        }),
        ('Availability', {
            'fields': ('acc', 'amount', 'tel', 'address', 'account')
        }),
    )