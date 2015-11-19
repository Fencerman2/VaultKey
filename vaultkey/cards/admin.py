from django.contrib import admin

from .models import Cards
# Register your models here.
class CardAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['article_text']}),
        ('Date information',{'fields': ['pub_date']}),
    ]

admin.site.register(Cards, CardAdmin)
