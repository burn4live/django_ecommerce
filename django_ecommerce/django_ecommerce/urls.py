from django.conf.urls import patterns, include, url
from payments import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.index', name='home'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^contact/', 'contact.views.contact', name='contact'),

    # user registration/authentication
    url(r'^sign_in$', views.sign_in, name='sign_in'),
    url(r'^sign_out$', views.sign_out, name='sign_out'),
    url(r'^register$', views.register, name='register'),
    url(r'^edit$', views.edit, name='edit'),
    url(r'^report$', 'main.views.report', name="report"),
    url(r'^api/v1/', include('main.urls')),
)
