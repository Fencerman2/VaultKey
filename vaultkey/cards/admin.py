from django.contrib import admin

from .models import Card
# Register your models here.
class CardAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['article_text']}),
        ('Date information',{'fields': ['pub_date']}),
    ]

admin.site.register(Card, CardAdmin)
