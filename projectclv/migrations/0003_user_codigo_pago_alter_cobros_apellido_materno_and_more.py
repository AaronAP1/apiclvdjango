# Generated by Django 5.0 on 2024-03-16 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectclv', '0002_cobros_dataconsolidado_recaudaciones_resumen'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='codigo_pago',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='APELLIDO_MATERNO',
            field=models.TextField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='APELLIDO_PATERNO',
            field=models.TextField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='CODIGO_CONCEPTO_1',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='CODIGO_DE_GRUPO_INTEGRANTES',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='CODIGO_INTEGRANTE',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='CODIGO_REFERENCIA_CLIENTE',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='DESCRIPCION_COBRO_REALIZAR',
            field=models.TextField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='FECHA_EMICION_RECIBO',
            field=models.DateTimeField(max_length=254),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='FECHA_VENCIMIENTO_RECIBO',
            field=models.DateField(max_length=254),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='ID_COBROS',
            field=models.CharField(max_length=254, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='IMPORTE_COBRO_COMPLETO',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='INDICADOR_COBRO_MORA',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='MONEDA_A_PAGAR',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='NOMBRES',
            field=models.TextField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='NUMERO_DE_RECIBO',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='OBSERVACIONES_RECIBO',
            field=models.TextField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='APELLIDO_MATERNO',
            field=models.TextField(db_column='APELLIDO MATERNO', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='APELLIDO_PATERNO',
            field=models.TextField(db_column='APELLIDO PATERNO', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='ASESOR',
            field=models.TextField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='CAPTACION',
            field=models.DateField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='CELULAR',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='CODIGO_DE_PAGO',
            field=models.CharField(db_column='CODIGO DE PAGO', max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='COMENTARIO',
            field=models.TextField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='CUOTA',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='DEPARTAMENTO',
            field=models.TextField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='DIRECCION',
            field=models.CharField(db_column='DIRECCIÓN', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='DISTRITO',
            field=models.TextField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='DOC',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='EMAIL',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='ID_DATOS',
            field=models.CharField(db_column='IDDATOS', max_length=254, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='INICIAL',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='INICIOPAGO',
            field=models.DateField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='M2',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='MZLTS',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='NOMBRES',
            field=models.TextField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='NUMERO',
            field=models.CharField(db_column='NÚMERO', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='PRECIOVENTA',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='PROVINCIA',
            field=models.TextField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='SALDO',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='SPAGADOS',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='SVENCIDOS',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='UBICACION',
            field=models.TextField(db_column='UBICACIÓN', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='recaudaciones',
            name='APELLIDOS_NOMBRES',
            field=models.TextField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='recaudaciones',
            name='CALC_MORA',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='recaudaciones',
            name='CODIGO_INTEGRANTE',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='recaudaciones',
            name='DESCRIPCION_RECIBO',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='recaudaciones',
            name='DIA_MORA',
            field=models.IntegerField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='recaudaciones',
            name='FECHA_ACTUALIZADA',
            field=models.DateField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='recaudaciones',
            name='FECHA_PAGO',
            field=models.DateField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='recaudaciones',
            name='FECHA_VENCIMIENTO',
            field=models.DateField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='recaudaciones',
            name='FORMA_PAGO',
            field=models.TextField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='recaudaciones',
            name='GRUPO',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='recaudaciones',
            name='ID_RECAUDACIONES',
            field=models.CharField(max_length=254, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='recaudaciones',
            name='IMP_MORA',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='recaudaciones',
            name='IMP_RECIBO',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='recaudaciones',
            name='IMP_TOTAL',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='recaudaciones',
            name='MZLTE',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='recaudaciones',
            name='NUMERO_DE_RECIBO',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='resumen',
            name='CPAGADAS',
            field=models.IntegerField(max_length=254),
        ),
        migrations.AlterField(
            model_name='resumen',
            name='CVENCIDAS',
            field=models.IntegerField(max_length=254),
        ),
        migrations.AlterField(
            model_name='resumen',
            name='FECHA_RESUMEN',
            field=models.DateField(max_length=254),
        ),
        migrations.AlterField(
            model_name='resumen',
            name='ID_INTEGRANTE',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='resumen',
            name='SPAGADOS',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='resumen',
            name='SVENCIDOS',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
