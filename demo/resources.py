from import_export import resources
from .models import ListeElecteur

class PersonResource(resources.ModelResource):
    class Meta:
        model = ListeElecteur