from django.contrib import admin
from .models import Player, PlayerDetails, Solved


admin.site.site_header = "Qriosity 2.0"
admin.site.site_title = "User Admin Area"
admin.site.index_title = "Welcome to the Qriosity admin area"


class PlayerDetailsInline(admin.TabularInline):
    model = PlayerDetails


class SolvedInline(admin.TabularInline):
    model = Solved
    extra = 1


class PlayerAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['user', 'name', 'score', 'question_level', 'level2']}),
                 ('Other Informations', {'fields': ['image', 'rank', 'email', 'last_submit'], 'classes': ['collapse']}), ]
    inlines = [PlayerDetailsInline, SolvedInline]


admin.site.register(Player, PlayerAdmin)
