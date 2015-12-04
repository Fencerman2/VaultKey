from django.contrib import admin

from .models import Request
# Register your models here.
class RequestAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',            {'fields': ['name_text']}),
        ('Email',           {'fields': ['email_text']}),
        ('Card Name',         {'fields': ['card_name']}),
        ('Card Quantity',         {'fields': ['card_quantity']}),
        ('Alter Type',         {'fields': ['alter_type']}),
        ('Date information',{'fields': ['pub_date']}),
    ]

admin.site.register(Request, RequestAdmin)
