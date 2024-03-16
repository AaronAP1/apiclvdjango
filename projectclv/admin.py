from django.contrib import admin
from .models import DataConsolidado, Cobros, Recaudaciones
from import_export.admin import ImportExportActionModelAdmin
from .resources import DataConsolidadoResource, CobrosResource, RecaudacionesResource




@admin.register(DataConsolidado)
class DataConsolidadoAdmin(ImportExportActionModelAdmin):
    resource_class = DataConsolidadoResource  # Especifica la clase de recurso
    list_display = ( 'ITEM', 'CODIGO_DE_PAGO', 'MZLTS', 'CAPTACION', 'ASESOR', 'APELLIDO_PATERNO', 'APELLIDO_MATERNO', 'NOMBRES', 'DOC', 'NUMERO', 'DIRECCION', 'DISTRITO', 'PROVINCIA', 'DEPARTAMENTO', 'CELULAR', 'EMAIL', 'M2', 'UBICACION', 'PRECIOVENTA', 'INICIAL', 'SALDO', 'CUOTAS', 'CUOTA', 'INICIOPAGO', 'CVENCIDAS', 'CPAGADAS', 'SVENCIDOS', 'SPAGADOS', 'COMENTARIO')
    search_fields = ('CODIGO_DE_PAGO',)
@admin.register(Cobros)
class CobrosAdmin(ImportExportActionModelAdmin):
    resource_class = CobrosResource
    list_display = ('NUMERO_DE_RECIBO', 'CODIGO_INTEGRANTE', 'APELLIDO_PATERNO', 'APELLIDO_MATERNO', 'NOMBRES', 'CODIGO_DE_GRUPO_INTEGRANTES', 'FECHA_EMICION_RECIBO', 'FECHA_VENCIMIENTO_RECIBO', 'MONEDA_A_PAGAR', 'CODIGO_REFERENCIA_CLIENTE', 'DESCRIPCION_COBRO_REALIZAR', 'OBSERVACIONES_RECIBO', 'INDICADOR_COBRO_MORA', 'CODIGO_CONCEPTO_1', )
    search_fields = ('CODIGO_INTEGRANTE',)

    actions = ['import_cobros']

@admin.register(Recaudaciones)
class RecaudacionesAdmin(ImportExportActionModelAdmin):
    resource_class = RecaudacionesResource
    list_display = ('CODIGO_INTEGRANTE','NUMERO_DE_RECIBO','APELLIDOS_NOMBRES','GRUPO','DESCRIPCION_RECIBO','IMP_RECIBO','FECHA_VENCIMIENTO','DIA_MORA','IMP_MORA','IMP_TOTAL','FECHA_PAGO','MZLTE','FORMA_PAGO','CALC_MORA','FECHA_ACTUALIZADA')
    search_fields = ('CODIGO_INTEGRANTE',)

# Register your models here.

admin.site.site_header="Panel de Administracion CLV | VENTAS"
admin.site.index_title="Opciones Disponibles"