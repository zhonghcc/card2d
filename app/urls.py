from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('',
	url(r'^$',views.index, name='index'),
	url(r'^list/*$',views.list, name='list'),
	# url(r'^(?P<card_id>\d+)$', views.detail, name='detail'),
)