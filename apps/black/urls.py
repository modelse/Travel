from django.conf.urls import url
from . import views
  # def method_to_run(request):
  #     print "Whatever route that was hit by an HTTP request (by the way) decided to invoke me!"
  #     print "By the way, here's the request object that Django automatically passes us:", request
  #     print "By the by, we still aren't delivering anything to the browser, so you should see 'ValueError at /'"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^create$', views.create, name='create'),
    url(r'^addTrip$', views.addTrip, name='addTrip'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^addtoList$', views.addtoList, name='addtoList'),
    url(r'^add/(?P<id>\d+)$', views.add, name='add'),
    url(r'^view/(?P<id>\d+)$', views.view, name='view'),

 ]
