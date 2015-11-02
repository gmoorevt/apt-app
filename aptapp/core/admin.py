from django.contrib import admin
from .models import Portfolio,Building,Unit,Address,Tenant,Lease,Receivable
# Register your models here.
class UnitInline(admin.TabularInline):
    fieldsets = [(None,{'fields':['name','description','number_bedrooms','number_bathrooms']})]
    model = Unit
    extra = 4

class UnitAdmin(admin.ModelAdmin):
    model = Unit
    fieldsets = [(None,{'fields':['name','description']})]

class BuldingAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields':['portfolio']}),
        (None,{'fields':['building_name','address', 'description']}),

    ]
    list_display = ('building_name','description')
    #list_display = ('building_name', 'description')
    inlines = [UnitInline]


admin.site.register(Building,BuldingAdmin)

admin.site.register(Portfolio)

admin.site.register(Unit)
admin.site.register(Address)
admin.site.register(Tenant)
admin.site.register(Lease)
admin.site.register(Receivable)