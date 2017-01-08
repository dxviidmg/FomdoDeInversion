from django.conf.urls import url
from . import views


urlpatterns = [

	url(r'^inversiones/pago/nuevo/(?P<pk>\d+)/$',views.CreateViewPago.as_view(), name='CreateViewPago'),
	url(r'^inversiones/nuevo/(?P<pk>\d+)/$',views.CreateViewInversion.as_view(), name='CreateViewInversion'),

	url(r'^inversiones/(?P<pk>\d+)/$', views.DetailViewInversion.as_view(), name="DetailViewInversion"),
	url(r'^inversiones/$',views.ListViewInversionesPorPagar.as_view(), name='ListViewInversionesPorPagar'),

]