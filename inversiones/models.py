from django.db import models
from decimal import Decimal
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Sum

class Inversion(models.Model):

	user = models.ForeignKey(User)
	cantidad = models.DecimalField(max_digits=20,decimal_places=2)
	fecha_alta = models.DateTimeField(default=timezone.now)
	comprobante = models.ImageField(upload_to='comprobantes/%Y/%m/%d/', null=True, blank=True)
	status = models.CharField(max_length=20, default="Por Pagar")
	devolucion = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	porcentaje_pagado = models.IntegerField(default=0)

	def CambioStatus(self):
		inversion = Inversion.objects.get(pk=self.pk)
		suma_pagos_dict = Pago.objects.filter(inversion=inversion).aggregate(Sum('cantidad'))
		if suma_pagos_dict['cantidad__sum'] == self.devolucion:
			self.status = "Pagado"
		else:
			self.status = "Por Pagar"
			self.save()

	def CalculaDevolucion(self):
		inversion = Inversion.objects.get(pk=self.pk)
		self.devolucion = self.cantidad * Decimal(1.12)
		self.save()

	def CalculaPorcentaje(self):
		inversion = Inversion.objects.get(pk=self.pk)
		suma_pagos_dict = Pago.objects.filter(inversion=inversion).aggregate(Sum('cantidad'))
		if suma_pagos_dict['cantidad__sum'] is None:
			suma_pagos_dict['cantidad__sum'] = 0
		self.porcentaje_pagado = round(100 * suma_pagos_dict['cantidad__sum'] / self.devolucion, 2)		
		self.save()

	def __str__(self):
		return 'Inversión de {} con cantidad de {}'.format(self.user, self.cantidad)

class Pago(models.Model):
	Tipo_CHOICES = (
		('Pago de Interés' , 'Pago de interés'),
		('Pago de Inversión' , 'Pago de Inversión'),
	)
	inversion = models.ForeignKey(Inversion)
	cantidad = models.DecimalField(max_digits=20,decimal_places=2)
	tipo = models.CharField(max_length=30, choices=Tipo_CHOICES)
	fecha_alta = models.DateTimeField(default=timezone.now)
	comprobante = models.ImageField(upload_to='Pago/comprobantes/%Y/%m/%d/', null=True, blank=True)

	def __str__(self):
		return '{} {}'.format(self.tipo, self.inversion)