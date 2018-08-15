
from django.conf.urls import url
from django.contrib import admin
from core import views as v
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
     url(r'^signup/', v.signup),
       url(r'^signup/homePage', v.home),
       url(r'^login/$', auth_views.LoginView.as_view(template_name='Login.html'), name='login'),
    url(r'^$', v.home),
    url(r'^accounts/profile/$',v.profile),
]
