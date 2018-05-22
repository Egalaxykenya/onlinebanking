from django.conf.urls import url
from bankingapp import views

# name spacing for the bankingapp
app_name = 'bankingapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.Apphome, name='apphome'),
    url(r'^transactions/$', views.transactions, name='transactions'),
    url(r'^monthlystatements/$', views.monthlystatements, name='monthlystatements'),
    url(r'^fundstransfer/$', views.fundstransfer, name='fundstransfer'),
    url(r'^payutilities/$', views.payutilities, name='payutilities'),
    url(r'^updateprofile/$', views.updateprofile, name='updateprofile'),
    url(r'^accesslogs/$', views.accesslogs, name='accesslogs'),

]
