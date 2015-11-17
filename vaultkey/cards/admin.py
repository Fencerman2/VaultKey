from django.contrib import admin

from .models import Cards
# Register your models here.
class RequestAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['cards_text']}),
        ('Date information',{'fields': ['pub_date']}),
    ]

admin.site.register(Request, RequestAdmin)
