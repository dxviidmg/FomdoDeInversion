from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from inversiones.models import Inversion
from .forms import *
from django.contrib.auth import authenticate, login

class ListViewAccounts(View):
	def get(self, request):
		template_name = "accounts/listAccounts.html"
		listUsers = User.objects.all().order_by('last_name', 'first_name').filter(is_superuser=False)
		paginator = Paginator(listUsers, 10)

		page = request.GET.get('page')

		try:
			users = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			users = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			users = paginator.page(paginator.num_pages)

		context = {
			'users': users,
		}
		return render(request, template_name, context)

class DetailViewAccount(View):
	def get(self, request, pk):
		template_name="accounts/detailAccount.html"	
		user = get_object_or_404(User, pk=pk)
		#perfil = Perfil.objects.get(user=user)
		perfil = get_object_or_404(Perfil, user=user)
		lisInversiones = Inversion.objects.filter(user=user)
		paginator = Paginator(lisInversiones, 10)

		page = request.GET.get('page')

		try:
			inversiones = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			inversiones = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			inversiones = paginator.page(paginator.num_pages)

		context={
			'user': user,
			'perfil': perfil,
			'inversiones':inversiones,
		}
		return render(request, template_name, context)

class CreateViewAccount(View):
#	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/createAccount.html"
		
		UserForm = UserCreateForm()
		PerfilForm = PerfilCreateForm()
		
		context = {
			'UserForm': UserForm,
			'PerfilForm': PerfilForm,
		}
		return render(request,template_name,context)

	def post(self,request):
		template_name = "accounts/createAccount.html"

		users = User.objects.filter(is_staff=False).count()
		userActual = users + 1

		NuevoUserForm = UserCreateForm(request.POST)
		NuevoPerfilForm = PerfilCreateForm(request.POST)
		
		if NuevoUserForm.is_valid(): 
			NuevoUser = NuevoUserForm.save(commit=False)
			NuevoUser.username = str(NuevoUser.last_name[0].upper()) + str(NuevoUser.last_name[1].upper()) + str(NuevoUser.last_name[2].upper()) + str(NuevoUser.last_name[3].upper()) + str(NuevoUser.first_name[0].upper()) + str(NuevoUser.first_name[1].upper()) + str(userActual)
			NuevoUser.password = "generica" + str(NuevoUser.first_name[0].lower()) + str(NuevoUser.last_name[0].lower())
			NuevoUser.set_password('generica')
			NuevoUser.save()

		if NuevoPerfilForm.is_valid():
			NuevoPerfil = NuevoPerfilForm.save(commit=False)
			NuevoPerfil.user = NuevoUser
			NuevoPerfil.save()

		return redirect("accounts:ListViewAccounts")

class LoginView(View):
	def login(request):
		template_name="registration/login.html"

		username = request.POST.get("username", False)
		password = request.POST.get("password", False)
		user = authenticate(username=username, password=password)
		
		if user is not None:
			login(request, user)
			return redirect("accounts:Profile")
		else:
			return render(request,template_name)

class Profile(View):
#	@method_decorator(login_required)
	def get(self, request):
		#if request.user.is_staff:
		template_name = "accounts/profile.html"
		#else:
		#	template_name = "accounts/profileUser.html"

		user = request.user
		

		try:
			perfil = Perfil.objects.get(user=user)
		except Perfil.DoesNotExist:
			perfil = None
		context = {
			'perfil': perfil
		}
		return render(request,template_name,context)