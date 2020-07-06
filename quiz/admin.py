from django.contrib import admin
from .models import Stage_1, StageTwo
# Register your models here.

admin.site.site_header = "Qriosity 2.0"
admin.site.site_title = "User Admin Area"
admin.site.index_title = "Welcome to the Qriosity admin area"


admin.site.register(Stage_1)
admin.site.register(StageTwo)
