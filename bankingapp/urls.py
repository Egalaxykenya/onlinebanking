from django.conf.urls import url
from bankingapp import views
#from bankingapp.views import HomeView


# name spacing for the bankingapp
app_name = 'bankingapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^apphome/$', views.apphome, name='apphome'),
    url(r'^utilitybillstransactions/$', views.utilitybillstransactions, name='utilitybillstransactions'),
    url(r'^fundstransactions/$', views.fundstransactions, name='fundstransactions'),
    url(r'^monthlystatements/$', views.monthlystatements, name='monthlystatements'),
    url(r'^fundstransfer/$', views.fundstransfer, name='fundstransfer'),
    url(r'^payutilities/$', views.payutilities, name='payutilities'),
    url(r'^updateprofile/$', views.updateprofile, name='updateprofile'),
    url(r'^accesslogs/$', views.accesslogs, name='accesslogs'),
    url(r'^signup/$', views.signup, name='signup'),

]
