from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import View
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ListViewInversionesPorPagar(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "inversiones/listInversionesPorPagar.html"
		inversiones = Inversion.objects.filter(status="Por Pagar")
		context = {
		'inversiones': inversiones,
		}
		return render(request, template_name, context)

class DetailViewInversion(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "inversiones/listPagos.html"
		inversion = get_object_or_404(Inversion, pk=pk)
		pagos = Pago.objects.filter(inversion=inversion)
		context = {
		'inversion': inversion,
		'pagos': pagos,
		}
		return render(request, template_name, context)

class CreateViewInversion(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "inversiones/createInversion.html"
		user = get_object_or_404(User, pk=pk)
		InversionForm = InversionCreateForm()
		
		context = {
			'user': user,
			'InversionForm': InversionForm,
		}
		return render(request,template_name,context)
	def post(self,request, pk):
		template_name = "inversiones/createInversion.html"
		user = User.objects.get(pk=pk)
		NuevaInversionForm = InversionCreateForm(request.POST, request.FILES)

		if NuevaInversionForm.is_valid():
			NuevoPerfil = NuevaInversionForm.save(commit=False)
			NuevoPerfil.user = user
			NuevoPerfil.save()
		return redirect("accounts:DetailViewAccount", pk=user.pk)

class UpdateViewInversion(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "inversiones/updateInversion.html"
		inversion = get_object_or_404(Inversion, pk=pk)
		user = User.objects.get(inversion=inversion)
		EdicionInversionForm = InversionCreateForm(instance=inversion)
		context = {
		'user': user,
		'EdicionInversionForm': EdicionInversionForm,
		}
		return render(request,template_name,context)
	def post(self, request, pk):
		template_name = "inversiones/updateInversion.html"
		inversion = get_object_or_404(Inversion, pk=pk)
		user = User.objects.get(inversion=inversion)
		EdicionInversionForm = InversionCreateForm(instance=inversion, data=request.POST)
		if EdicionInversionForm.is_valid:
			EdicionInversionForm.save()
		return redirect("accounts:DetailViewAccount", pk=user.pk)

class DeleteViewInversion(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "inversiones/deleteInversion.html"
		inversion = get_object_or_404(Inversion, pk=pk)
		user = User.objects.get(inversion=inversion)
		context = {
		'user': user,
		'inversion': inversion,
		}
		return render(request,template_name,context)
	def post(self, request, pk):
		template_name = "inversiones/deleteInversion.html"
		inversion = get_object_or_404(Inversion, pk=pk)
		if request.method=='POST':
			inversion.delete()
		return redirect("accounts:DetailViewAccount", pk=user.pk)

class CreateViewPago(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "inversiones/createPago.html"
		inversion = get_object_or_404(Inversion, pk=pk)
		PagoForm = PagoCreateForm()
		context = {
			'inversion': inversion,
			'PagoForm': PagoForm,
		}
		return render(request,template_name,context)
	def post(self,request, pk):
		inversion = get_object_or_404(Inversion, pk=pk)
		NuevoPagoForm = PagoCreateForm(request.POST, request.FILES)

		if NuevoPagoForm.is_valid():
			NuevoPago = NuevoPagoForm.save(commit=False)
			NuevoPago.inversion = inversion
			NuevoPago.save()
		return redirect("inversiones:DetailViewInversion", pk=inversion.pk)

class UpdateViewPago(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "inversiones/updatePago.html"
		pago = get_object_or_404(Pago, pk=pk)
		inversion = Inversion.objects.get(pago=pago)
		EdicionPagoForm = PagoCreateForm(instance=pago)
		context = {
		'pago': pago,
		'inversion': inversion,
		'EdicionPagoForm': EdicionPagoForm,
		}
		return render(request,template_name,context)
	def post(self, request, pk):
		template_name = "inversiones/updatePago.html"
		pago = get_object_or_404(Pago, pk=pk)
		inversion = Inversion.objects.get(pago=pago)
		EdicionPagoForm = PagoCreateForm(instance=pago, data=request.POST)
		if EdicionPagoForm.is_valid:
			EdicionPagoForm.save()
		return redirect("inversiones:DetailViewInversion", pk=inversion.pk)

class DeleteViewPago(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "inversiones/deletePago.html"
		pago = get_object_or_404(Pago, pk=pk)
		inversion = Inversion.objects.get(pago=pago)
		context = {
		'pago': pago,
		'inversion': inversion,
		}
		return render(request,template_name,context)
	def post(self, request, pk):
		template_name = "inversiones/deletePago.html"
		pago = get_object_or_404(Pago, pk=pk)
		inversion = Inversion.objects.get(pago=pago)
		if request.method=='POST':
			pago.delete()
		return redirect("inversiones:DetailViewInversion", pk=inversion.pk)