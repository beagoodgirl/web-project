from django.contrib import admin
from .models import Person

# Register your models here.
admin.site.register(Person)

class PersonAdmin(admin.ModelAdmin):   # new
    list_display = ('ssn', 'amount', 'tel', 'address', 'account')
    list_filter = ('ssn', 'amount', 'tel', 'address', 'account')

    fieldsets = (
        (None, {
            'fields': ('ssn', 'amount', 'tel', 'address', 'account')
        }),
        ('Availability', {
            'fields': ('ssn', 'amount', 'tel', 'address', 'account')
        }),
    )