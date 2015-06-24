from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^sync$',views.sync),
	url(r'^syncresults$',views.syncresults),
    url(r'^sentiment$',views.sentiment),
    url(r'^logout$',views.logout),
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.main),
    url(r'^(?P<folk_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'', include('social_auth.urls'))
  
]
