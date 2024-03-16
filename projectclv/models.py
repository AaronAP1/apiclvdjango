from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, codigo_pago=None, **extra_fields):
        if not email:
            raise ValueError('El campo email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, codigo_pago=codigo_pago, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, codigo_pago=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Los superusuarios deben tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Los superusuarios deben tener is_superuser=True.')

        return self.create_user(email, password, codigo_pago=codigo_pago, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    codigo_pago = models.CharField(max_length=50, blank=True, null=True) 
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


# ModelosTablas      
    
class DataConsolidado(models.Model):
    ID_DATOS = models.CharField(primary_key=True, db_column='IDDATOS',max_length=254)
    ITEM = models.IntegerField()
    CODIGO_DE_PAGO = models.CharField(unique=True, null=True, db_column='CODIGO DE PAGO',max_length=254)
    MZLTS = models.CharField(null=True,max_length=254)
    CAPTACION = models.DateField(null=True,max_length=254)
    ASESOR = models.TextField(null=True,max_length=254)
    APELLIDO_PATERNO = models.TextField(null=True, db_column='APELLIDO PATERNO',max_length=254)
    APELLIDO_MATERNO = models.TextField(null=True, db_column='APELLIDO MATERNO',max_length=254)
    NOMBRES = models.TextField(null=True,max_length=254)
    DOC = models.CharField( null=True,max_length=254)
    NUMERO = models.CharField( null=True,db_column='NÚMERO',max_length=254)
    DIRECCION = models.CharField(null=True,db_column='DIRECCIÓN',max_length=254) 
    DISTRITO = models.TextField(null=True,max_length=254)
    PROVINCIA = models.TextField(null=True,max_length=254)
    DEPARTAMENTO = models.TextField(null=True,max_length=254)
    CELULAR = models.CharField( null=True,max_length=254)
    EMAIL = models.CharField(null=True,max_length=254)
    M2 = models.CharField(null=True,max_length=254)
    UBICACION = models.TextField(null=True, db_column='UBICACIÓN',max_length=254)
    PRECIOVENTA = models.CharField(null=True,max_length=254)
    INICIAL = models.CharField(null=True,max_length=254)
    SALDO = models.CharField(null=True,max_length=254)
    CUOTAS = models.IntegerField(null=True)
    CUOTA = models.CharField(null=True,max_length=254)
    INICIOPAGO = models.DateField(null=True,max_length=254)
    CVENCIDAS = models.IntegerField(null=True)
    CPAGADAS = models.IntegerField(null=True)
    SVENCIDOS = models.CharField(null=True,max_length=254)
    SPAGADOS = models.CharField(null=True,max_length=254)
    COMENTARIO = models.TextField(null=True,max_length=254)

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
    ID_COBROS = models.CharField(primary_key=True,max_length=254)
    CODIGO_INTEGRANTE = models.CharField(null=True,max_length=254)
    NUMERO_DE_RECIBO = models.CharField(max_length=254)
    APELLIDO_PATERNO = models.TextField( null=True,max_length=254)
    APELLIDO_MATERNO = models.TextField( null=True,max_length=254)
    NOMBRES = models.TextField( null=True,max_length=254)
    CODIGO_DE_GRUPO_INTEGRANTES = models.CharField( null=True,max_length=254)
    FECHA_EMICION_RECIBO = models.DateTimeField(max_length=254)
    FECHA_VENCIMIENTO_RECIBO = models.DateField(max_length=254)
    MONEDA_A_PAGAR = models.CharField( null=True,max_length=254)
    CODIGO_REFERENCIA_CLIENTE = models.CharField(null=True,max_length=254)
    DESCRIPCION_COBRO_REALIZAR = models.TextField(null=True,max_length=254)
    OBSERVACIONES_RECIBO = models.TextField( null=True,max_length=254)
    INDICADOR_COBRO_MORA = models.CharField( null=True,max_length=254)
    CODIGO_CONCEPTO_1 = models.CharField(null=True,max_length=254)
    IMPORTE_COBRO_COMPLETO = models.CharField(null=True,max_length=254)
    
class Recaudaciones(models.Model):
    ID_RECAUDACIONES = models.CharField(primary_key=True,max_length=254)
    CODIGO_INTEGRANTE = models.CharField(null=True,max_length=254)
    NUMERO_DE_RECIBO = models.CharField(null=True,max_length=254)
    APELLIDOS_NOMBRES = models.TextField(null=True,max_length=254)
    GRUPO = models.CharField(null=True,max_length=254)
    DESCRIPCION_RECIBO = models.CharField(null=True,max_length=254)
    IMP_RECIBO = models.CharField(null=True,max_length=254)
    FECHA_VENCIMIENTO = models.DateField(null=True,max_length=254)
    DIA_MORA = models.IntegerField(null=True,max_length=254)
    IMP_MORA = models.CharField(null=True,max_length=254)
    IMP_TOTAL = models.CharField(null=True,max_length=254)
    FECHA_PAGO = models.DateField(null=True,max_length=254)
    MZLTE = models.CharField(null=True,max_length=254)
    FORMA_PAGO = models.TextField(null=True,max_length=254)
    CALC_MORA = models.CharField(null=True,max_length=254)
    FECHA_ACTUALIZADA = models.DateField(null=True,max_length=254)

class Resumen(models.Model):
    ID_RESUMEN = models.CharField(primary_key=True, max_length=10) 
    ID_INTEGRANTE = models.CharField(max_length=254)
    FECHA_RESUMEN = models.DateField(max_length=254)
    CVENCIDAS = models.IntegerField(max_length=254)
    CPAGADAS = models.IntegerField(max_length=254)
    SVENCIDOS = models.CharField(max_length=254)
    SPAGADOS = models.CharField(max_length=254)
