from django.contrib import admin

from .models import Player
# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('First Name',   {'fields': ['player_firstname']}),
        ('Last Name',    {'fields': ['player_lastname']}),
        ('Bio',          {'fields': ['player_description']}),
        (None,           {'fields': ['image']}),
    ]

admin.site.register(Player, PlayerAdmin)
