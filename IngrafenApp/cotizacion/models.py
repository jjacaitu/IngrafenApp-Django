from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MaxValueValidator
from django import forms

# Create your models here.

IMPRESION_CHOICES = (("NO","Sin impresion"),("FCT","Full color tiro"),("FCTR","Full color tiro y retiro"),("PT","Pantone Tiro"),("PTR","Pantone Tiro y Retiro"))
TIPO_PR_CHOICES = (("OF","OFFSET"),("G","GIGANTOGRAFIA"),("OF","OFFSET Y GIGANTOGRAFIA"))
CATEGORIA_USUARIO = (("ADM","ADMINISTRADOR"),("VEN","VENDEDOR"),("COT","COTIZADOR"))
UV_CHOICES = (("SIN","SIN UV"),("UVT","UV TIRO"),("UVTR","UV TIRO Y RETIRO"),("UVST","UV SECTORIZADO TIRO"),("UVSTR","UV SECTORIZADO TIRO Y RETIRO"))
LAMINADO_CHOICES = (("SIN","SIN LAMINADO"),("LBT","LAMINADO BRILLO TIRO"),("LBTR","LAMINADO BRILLO TIRO Y RETIRO"),("LMT","LAMINADO MATE TIRO"),("LMTR","LAMINADO MATE TIRO Y RETIRO"))
TROQUELADO_CHOICES = (("SIN","SIN TROQUELAR"),("TRN","TROQUEL NUEVO"),("TRE","TROQUEL EXISTENTE"),("MC","EN PLANAS CON MEDIO CORTE"))


class Usuarios(AbstractUser):
    categoria = models.CharField(max_length=3,choices=CATEGORIA_USUARIO,default="ADM")


class Materiales(models.Model):
    material = models.CharField(max_length=40)
    usuario = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.material

    def save(self):
       self.material = self.material.title()
       super(Materiales, self).save()
    #COLOCAR OTROS ASPECTOS DE VENDEDOR

class TipoDeTrabajo(models.Model):
    trabajo = models.CharField(max_length=40)
    hojas_interiores = models.BooleanField(default=False)
    usuario = models.CharField(max_length=20, blank=True)

    def save(self):
       self.trabajo = self.trabajo.title()
       super(TipoDeTrabajo, self).save()

    def __str__(self):
        return self.trabajo

class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    usuario = models.CharField(max_length=20, blank=True)
    def save(self):
       self.nombre = self.nombre.title()
       super(Clientes, self).save()

    def __str__(self):
        return self.nombre

class CotizacionesSolicitadas(models.Model):
    num_solicitud = models.AutoField(primary_key = True)
    vendedor = models.CharField(max_length=20, blank=True)
    trabajo = models.CharField(max_length=40)
    nombre_cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT, related_name="client")
    tipo_trabajo = models.CharField(max_length=30,null=True,blank=True)
    cantidad = models.IntegerField()
    material = models.ForeignKey(Materiales, on_delete=models.CASCADE)

    medida_alto = models.FloatField(validators=[MaxValueValidator(99)])
    medida_ancho = models.FloatField(validators=[MaxValueValidator(99)])

    material_interiores = models.ForeignKey(Materiales, on_delete=models.CASCADE, related_name="material_interiores",null=True,blank=True)
    medida_alto_interiores = models.FloatField(null=True,blank=True,validators=[MaxValueValidator(99)])
    medida_ancho_interiores = models.FloatField(null=True,blank=True,validators=[MaxValueValidator(99)])

    fecha_solicitada = models.DateTimeField(auto_now_add=True)
    impresion = models.CharField(max_length=3, choices=IMPRESION_CHOICES)
    uv = models.CharField(max_length=5, choices=UV_CHOICES)
    laminado = models.CharField(max_length=5, choices=LAMINADO_CHOICES)
    troquelado = models.CharField(max_length=5, choices=TROQUELADO_CHOICES)
    detalles = models.CharField(max_length=300, blank=True,null=True)
    fecha_completada = models.DateTimeField(auto_now=True)
    cotizador = models.CharField(max_length=20, blank=True)
    numero_cotizacion = models.CharField(max_length=20, blank=True)
    imagen = models.ImageField(upload_to="uploads/", blank=True, null=True)
#AUMENTAR PARA SUBIR IMAGEN DE LO QUE SE DESEA COTIZAR




    def __str__(self):
        return "#{},cliente: {},trabajo: {}".format(str(self.num_solicitud),str(self.nombre_cliente),str(self.tipo_trabajo))

#CAMBIAR EL MODELO
