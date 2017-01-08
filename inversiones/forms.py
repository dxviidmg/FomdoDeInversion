from django import forms
from .models import *

class InversionCreateForm(forms.ModelForm):
	class Meta:
		model = Inversion
		fields = ('cantidad', 'comprobante',)

class PagoCreateForm(forms.ModelForm):
	class Meta:
		model = Pago
		fields = ('cantidad', 'comprobante', 'tipo',)