# my_site/urls.py

#

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from django.conf.urls import url
from . import views

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^frontend$', views.frontend_page, name='frontend'),
    url(r'^backend$', views.backend_page, name='backend'),
    url(r'^other$', views.other_page, name='other'),
    url(r'^about$', views.about_page, name='about'),
    url(r'^info$', views.info_page, name='info'),
    url(r'^services$', views.services_page, name='services'),
    url(r'^contacts$', views.contacts_page, name='contacts'),
    url(r'^feedback$', views.contacts_page, name='feedback'),
    url(r'^work/(?P<pk>[0-9]+)/$', views.work_page, name='work')
]
