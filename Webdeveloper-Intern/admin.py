from django.contrib import admin
# Register your models here.
from .models import Dreamreal

admin.site.register(Dreamreal)
class MyModelAdmin(admin.Admin):
    actions = [export_csv, export_xls, export_xlsx]

admin.site.register(Dreamreal, MyModelAdmin)
