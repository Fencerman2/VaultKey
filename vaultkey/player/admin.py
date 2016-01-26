from django.contrib import admin

from .models import Player
# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['player_name']}),
        (None,  {'fields': ['player_description']}),
    ]

admin.site.register(Player, PlayerAdmin)
