from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from sms_signup.views import LoginView, PasswordRecoveryView


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', TemplateView.as_view(template_name="base.html"), name='home'),
    url(r'^signup/', include('sms_signup.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^login/$',  LoginView.as_view(), name='login'),
    url(r'^forgot_password/$',  PasswordRecoveryView.as_view(), name='forgot_password'),
    url(r'^password_sent/$',  TemplateView.as_view(template_name = "password_sent.html"), name='password_sent'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
