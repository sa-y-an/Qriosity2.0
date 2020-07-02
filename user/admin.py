from django.contrib import admin
from .models import *


admin.site.site_header = "Qriosity 2.0"
admin.site.site_title = "User Admin Area"
admin.site.index_title = "Welcome to the Qriosity admin area"


class PlayerDetailsInline(admin.TabularInline):
    model = PlayerDetails


class PlayerAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['user', 'name', 'score', 'question_level']}),
                 ('Other Informations', {'fields': ['image', 'rank', 'email', 'last_submit'], 'classes': ['collapse']}), ]
    inlines = [PlayerDetailsInline]


admin.site.register(Player, PlayerAdmin)
