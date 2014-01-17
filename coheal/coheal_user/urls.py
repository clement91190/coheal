from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^connexion/$', 'coheal_user.views.connexion'),
    )
