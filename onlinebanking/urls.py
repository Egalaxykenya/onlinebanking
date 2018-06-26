"""onlinebanking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from bankingapp import views
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView

# Create a new class that redirects the user to the homepage,
# if successful at logging

class BankingRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/bankingapp/'



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/register/$', BankingRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),

    url(r'^bankingapp/', include('bankingapp.urls')),
    url(r'^admin/', admin.site.urls),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
