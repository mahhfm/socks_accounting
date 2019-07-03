from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [


    url(r'^$', views.home, name="home"),
    url(r'^profiles/$', views.ProfileListView.as_view(), name="view-profile"),


    url(r'^new/profiles/$', views.ProfileCreateView.as_view(), name="new-profile"),


    url(r'^login/',  views.LoginViewClass.as_view(), name="user-login"),
    url('^logout/', auth_views.LogoutView.as_view(template_name="user/logout.html"), name="user-logout"),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
