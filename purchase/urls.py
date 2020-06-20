from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^purchasess/$', views.PurchaseListView.as_view(), name='purchases'),
]

