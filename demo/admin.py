from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


#admin.site.register(ListeElecteur)
#admin.site.register(Fichier)

@admin.register(Fichier)
class ListeAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Parraine)