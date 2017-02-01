from django.conf.urls import url
from . import views
  # def method_to_run(request):
  #     print "Whatever route that was hit by an HTTP request (by the way) decided to invoke me!"
  #     print "By the way, here's the request object that Django automatically passes us:", request
  #     print "By the by, we still aren't delivering anything to the browser, so you should see 'ValueError at /'"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^reg$', views.registration, name='reg'),
    url(r'^clear$', views.clear, name='clear'),
    url(r'^success$', views.success, name='success'),
    url(r'^loggedIn$', views.loggedIn, name='loggedIn'),
    url(r'^logout$', views.logout, name='logout'),

 ]
