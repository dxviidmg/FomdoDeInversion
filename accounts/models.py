from django.db import models
from django.conf import settings

class Perfil(models.Model):
	Banco_CHOICES = (
		('BANAMEX', 'BANAMEX'),
		('BANCOMER', 'BANCOMER'),
		('BANORTE', 'BANORTE'),
		('SCOTIA BANK', 'SCOTIA BANK'),
		('SANTANDER', 'SANTANDER'),
		('HSBC', 'HSBC'),
	)
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	telefono = models.CharField(max_length=10,blank=True,null=True)
	banco = models.CharField(max_length=20, choices=Banco_CHOICES)
	cta = models.CharField(max_length=16)

	def __str__(self):
		return 'Perfil de {}'.format(self.user.username)