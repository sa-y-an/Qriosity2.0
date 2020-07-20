from django.contrib import admin
from .models import Player, PlayerDetails, Solved, StageOneHint


admin.site.site_header = "Qriosity 2.0"
admin.site.site_title = "User Admin Area"
admin.site.index_title = "Welcome to the Qriosity admin area"


class PlayerDetailsInline(admin.TabularInline):
    model = PlayerDetails


class SolvedInline(admin.TabularInline):
    model = Solved
    extra = 0


class StageOneInline(admin.TabularInline):
    model = StageOneHint
    extra = 0


class PlayerAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['user', 'name', 'score', 'question_level', 'level2', 'count2']}),
                 ('Other Informations', {'fields': ['image', 'rank', 'email', 'last_submit'], 'classes': ['collapse']}), ]
    inlines = [PlayerDetailsInline, SolvedInline, StageOneInline]


admin.site.register(Player, PlayerAdmin)
