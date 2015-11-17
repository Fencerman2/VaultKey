from django.contrib import admin

from .models import Request
# Register your models here.
class RequestAdmin(admin.ModelAdmin)
    fieldsets = [
        (None,              {'fields': ['request_text']}),
        ('Date information',{'fields': ['pub_date']}),
    ]

admin.site.register(Request, RequestAdmin)
