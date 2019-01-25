from django.conf.urls import url
from .import views
app_name = 'github'
urlpatterns = [
    url(r'^index',views.index, name = "home"),
    url(r'^next',views.result, name = "result"),
    url(r'^signup$',views.regis, name = "signup"),
    url(r'^$', views.login_page, name = "login"),
    url(r'^logout', views.logout_page, name = "logout"),
]