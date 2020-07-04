from django.contrib import admin
from .models import Stage_1, StageTwo
# Register your models here.

admin.site.site_header = "Qriosity 2.0"
admin.site.site_title = "Quiz"
admin.site.index_title = "Welcome super admin"


admin.site.register(Stage_1)
admin.site.register(StageTwo)
