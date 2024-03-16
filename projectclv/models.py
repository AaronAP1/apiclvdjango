from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)
# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Falta Email')
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user =self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    email =models.EmailField(unique=True)
    name = models.CharField(max_length=254)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
 
    USERNAME_FIELD = 'email'


# ModelosTablas      
    
class DataConsolidado(models.Model):
    ID_DATOS = models.CharField(primary_key=True, db_column='IDDATOS')
    ITEM = models.IntegerField()
    CODIGO_DE_PAGO = models.CharField(unique=True, null=True, db_column='CODIGO DE PAGO')
    MZLTS = models.CharField(null=True)
    CAPTACION = models.DateField(null=True)
    ASESOR = models.TextField(null=True)
    APELLIDO_PATERNO = models.TextField(null=True, db_column='APELLIDO PATERNO')
    APELLIDO_MATERNO = models.TextField(null=True, db_column='APELLIDO MATERNO')
    NOMBRES = models.TextField(null=True)
    DOC = models.CharField( null=True)
    NUMERO = models.CharField( null=True,db_column='NÚMERO')
    DIRECCION = models.CharField(null=True,db_column='DIRECCIÓN') 
    DISTRITO = models.TextField(null=True)
    PROVINCIA = models.TextField(null=True)
    DEPARTAMENTO = models.TextField(null=True)
    CELULAR = models.CharField( null=True)
    EMAIL = models.CharField(null=True)
    M2 = models.CharField(null=True)
    UBICACION = models.TextField(null=True, db_column='UBICACIÓN')
    PRECIOVENTA = models.CharField(null=True)
    INICIAL = models.CharField(null=True)
    SALDO = models.CharField(null=True)
    CUOTAS = models.IntegerField(null=True)
    CUOTA = models.CharField(null=True)
    INICIOPAGO = models.DateField(null=True)
    CVENCIDAS = models.IntegerField(null=True)
    CPAGADAS = models.IntegerField(null=True)
    SVENCIDOS = models.CharField(null=True)
    SPAGADOS = models.CharField(null=True)
    COMENTARIO = models.TextField(null=True)

    # Método para obtener información de Cobros relacionados
    def obtener_info_cobros(self):
        return Cobros.objects.filter(CODIGO_INTEGRANTE=self.CODIGO_DE_PAGO).values(
            'NUMERO_DE_RECIBO',
            'DESCRIPCION_COBRO_REALIZAR',
            'IMPORTE_COBRO_COMPLETO',
            'FECHA_VENCIMIENTO_RECIBO',
            'INDICADOR_COBRO_MORA',
            'OBSERVACIONES_RECIBO'
        )

    # Método para obtener información de Recaudaciones relacionadas
    def obtener_info_recaudaciones(self):
        return Recaudaciones.objects.filter(CODIGO_INTEGRANTE=self.CODIGO_DE_PAGO).values(
            'NUMERO_DE_RECIBO',
            'DESCRIPCION_RECIBO',
            'IMP_RECIBO',
            'FECHA_VENCIMIENTO',
            'DIA_MORA',
            'IMP_MORA',
            'IMP_TOTAL',
            'FECHA_PAGO',
            'MZLTE',
            'FORMA_PAGO',
            'CALC_MORA',
            'FECHA_ACTUALIZADA'
        )
    
class Cobros(models.Model):
    ID_COBROS = models.CharField(primary_key=True)
    CODIGO_INTEGRANTE = models.CharField(null=True)
    NUMERO_DE_RECIBO = models.CharField()
    APELLIDO_PATERNO = models.TextField( null=True)
    APELLIDO_MATERNO = models.TextField( null=True)
    NOMBRES = models.TextField( null=True)
    CODIGO_DE_GRUPO_INTEGRANTES = models.CharField( null=True)
    FECHA_EMICION_RECIBO = models.DateTimeField()
    FECHA_VENCIMIENTO_RECIBO = models.DateField()
    MONEDA_A_PAGAR = models.CharField( null=True)
    CODIGO_REFERENCIA_CLIENTE = models.CharField(null=True)
    DESCRIPCION_COBRO_REALIZAR = models.TextField(null=True)
    OBSERVACIONES_RECIBO = models.TextField( null=True)
    INDICADOR_COBRO_MORA = models.CharField( null=True)
    CODIGO_CONCEPTO_1 = models.CharField(null=True)
    IMPORTE_COBRO_COMPLETO = models.CharField(null=True)
    
class Recaudaciones(models.Model):
    ID_RECAUDACIONES = models.CharField(primary_key=True)
    CODIGO_INTEGRANTE = models.CharField(null=True)
    NUMERO_DE_RECIBO = models.CharField(null=True)
    APELLIDOS_NOMBRES = models.TextField(null=True)
    GRUPO = models.CharField(null=True)
    DESCRIPCION_RECIBO = models.CharField(null=True)
    IMP_RECIBO = models.CharField(null=True)
    FECHA_VENCIMIENTO = models.DateField(null=True)
    DIA_MORA = models.IntegerField(null=True)
    IMP_MORA = models.CharField(null=True)
    IMP_TOTAL = models.CharField(null=True)
    FECHA_PAGO = models.DateField(null=True)
    MZLTE = models.CharField(null=True)
    FORMA_PAGO = models.TextField(null=True)
    CALC_MORA = models.CharField(null=True)
    FECHA_ACTUALIZADA = models.DateField(null=True)

class Resumen(models.Model):
    ID_RESUMEN = models.CharField(primary_key=True, max_length=10) 
    ID_INTEGRANTE = models.CharField()
    FECHA_RESUMEN = models.DateField()
    CVENCIDAS = models.IntegerField()
    CPAGADAS = models.IntegerField()
    SVENCIDOS = models.CharField()
    SPAGADOS = models.CharField()
