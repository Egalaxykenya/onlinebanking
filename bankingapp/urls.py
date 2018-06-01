from django.conf.urls import url
from bankingapp import views
from bankingapp.views import HomeView


# name spacing for the bankingapp
app_name = 'bankingapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', 'django.contrib.auth.views.login', name='login'),
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    url(r'^home/$', HomeView.as_view(), name='Apphome'),
    url(r'^utilitybillstransactions/$', views.utilitybillstransactions, name='utilitybillstransactions'),
    url(r'^fundstransactions/$', views.fundstransactions, name='fundstransactions'),
    url(r'^monthlystatements/$', views.monthlystatements, name='monthlystatements'),
    url(r'^fundstransfer/$', views.fundstransfer, name='fundstransfer'),
    url(r'^payutilities/$', views.payutilities, name='payutilities'),
    url(r'^updateprofile/$', views.updateprofile, name='updateprofile'),
    url(r'^accesslogs/$', views.accesslogs, name='accesslogs'),
    url(r'^signup/$', views.signup, name='signup'),

]
