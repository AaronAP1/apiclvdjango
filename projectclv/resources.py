from import_export import resources
from .models import DataConsolidado, Cobros, Recaudaciones


class DataConsolidadoResource(resources.ModelResource):
    class Meta:
        model = DataConsolidado
        import_id_fields = ['ID_DATOS']
        skip_unchanged = True  # Evitar importar filas que no han cambiado
        report_skipped = False  # No generar informes para filas saltadas
        exclude = ('id',) 
        

class CobrosResource(resources.ModelResource):
    

    class Meta:
        model = Cobros
        import_id_fields = ['ID_COBROS']
        skip_unchanged = True
        report_skipped = False
        exclude = ('id',)

   

class RecaudacionesResource(resources.ModelResource):
   

    class Meta:
        model = Recaudaciones
        import_id_fields = ['ID_RECAUDACIONES']
        skip_unchanged = False  # Importar filas incluso si no han cambiado
        report_skipped = False  # No generar informes para filas saltadas
        exclude = ('id',)