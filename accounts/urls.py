from django.conf.urls import url

from . import views
from .forms import LoginForm


urlpatterns = [
	url(r'^login/$', views.LoginView.login, name="login"),

	url(r'^profile/$', views.Profile.as_view(), name="Profile"),

	url(r'^clientes/nuevo/$', views.CreateViewAccount.as_view(), name="CreateViewAccount"),
	url(r'^accounts/(?P<pk>\d+)/$', views.DetailViewAccount.as_view(), name="DetailViewAccount"),
	url(r'^accounts', views.ListViewAccounts.as_view(),name="ListViewAccounts"),
]

