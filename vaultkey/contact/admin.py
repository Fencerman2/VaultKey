from django.contrib import admin

from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['name_text']}),
        (None,              {'fields': ['email_text']}),
        (None,              {'fields': ['message_text']}),
    ]

admin.site.register(Contact, ContactAdmin)
