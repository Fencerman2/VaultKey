from django.contrib import admin

from .models import Player
# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['player_firstname']}),
        (None,  {'fields': ['player_lastname']}),
        (None,  {'fields': ['player_description']}),
        (None,  {'fields': ['image']}),
    ]

admin.site.register(Player, PlayerAdmin)
