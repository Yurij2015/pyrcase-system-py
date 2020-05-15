from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^learnbooks/$', views.LearnbookListView.as_view(), name='learnbooks'),
    url(r'^purchase/(?P<pk>\d+)$', views.LearnbookDetailView.as_view(), name='purchase-detail'),
    url(r'^tutors/$', views.TutorListView.as_view(), name='tutors'),
    url(r'^tutor/(?P<pk>\d+)$', views.TutorDetailView.as_view(), name='tutor-detail'),

]

STATIC_URL = '/static/'
