from django.conf.urls import url
from . import views


urlpatterns = [

	url(r'^inversiones/pago/nuevo/(?P<pk>\d+)/$',views.CreateViewPago.as_view(), name='CreateViewPago'),
	url(r'^inversiones/nuevo/(?P<pk>\d+)/$',views.CreateViewInversion.as_view(), name='CreateViewInversion'),

	url(r'^inversiones/pago/actualizar/(?P<pk>\d+)/$', views.UpdateViewPago.as_view(), name="UpdateViewPago"),
	url(r'^inversiones/pago/eliminar/(?P<pk>\d+)/$', views.DeleteViewPago.as_view(), name="DeleteViewPago"),

	url(r'^inversiones/(?P<pk>\d+)/$', views.DetailViewInversion.as_view(), name="DetailViewInversion"),
	url(r'^inversiones/actualizar/(?P<pk>\d+)/$', views.UpdateViewInversion.as_view(), name="UpdateViewInversion"),
	url(r'^inversiones/eliminar/(?P<pk>\d+)/$', views.DeleteViewInversion.as_view(), name="DeleteViewInversion"),
	url(r'^inversiones/$',views.ListViewInversionesPorPagar.as_view(), name='ListViewInversionesPorPagar'),

]