from django.contrib import admin
from stuscore.models import Stuscore

class StuscoreAdmin(admin.ModelAdmin):
    list_display = ['no','total']

admin.site.register(Stuscore,StuscoreAdmin)
