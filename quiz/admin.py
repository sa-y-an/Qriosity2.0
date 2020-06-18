from django.contrib import admin
from .models import StaticQuestions, AudioQuestions
# Register your models here.

admin.site.site_header = "Qriosity 2.0"
admin.site.site_title = "Qriosity 2.0"
admin.site.index_title = "Welcome super admin"


admin.site.register(StaticQuestions)
admin.site.register(AudioQuestions)
