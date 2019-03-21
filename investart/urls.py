from django.conf.urls import url
from django.contrib.auth import views as auth_views
from investart import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^account/$', views.account, name='account'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^dev_login/$', views.dev_login, name='dev_login'),
    url(r'^inv_login/$', views.inv_login, name='inv_login'),
    url(r'^dev_signup/$', views.dev_signup, name='dev_signup'),
    url(r'^inv_signup/$', views.inv_signup, name='inv_signup'),
    url(r'^developer/$', views.developer, name='developer'),
    url(r'^investor/$', views.investor, name='investor'),
    url(r'^project/(?P<project_name_slug>[\w\-]+)/$', views.show_project, name='show_project'),
    url(r'^add_project/$', views.add_project, name='add_project'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]
