from django import forms
from django.forms import ModelForm
from cotizacion.models import Usuarios,CotizacionesSolicitadas, Materiales, TipoDeTrabajo, Clientes
from cotizacion import views


class Crear_usuario(ModelForm):
    class Meta:
         model = Usuarios
         fields = ("username", "first_name","last_name","password", "email", "categoria")

class Materiales(ModelForm):
    class Meta:
        model = Materiales
        exclude = ["usuario"]

class TipoDeTrabajo(ModelForm):
    class Meta:
        model = TipoDeTrabajo
        exclude = ["usuario"]

class Clientes(ModelForm):
    class Meta:
        model = Clientes
        exclude = ["usuario"]


class Solicitud_cot(ModelForm):
    class Meta:
        model = CotizacionesSolicitadas
        exclude = ["vendedor","cotizador","numero_cotizacion"]
        #widgets = {"impresion":forms.RadioSelect(),"uv":forms.RadioSelect(),"laminado":forms.RadioSelect(),"troquelado":forms.RadioSelect()}
