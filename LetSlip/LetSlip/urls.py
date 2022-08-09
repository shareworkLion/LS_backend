from django.contrib import admin
from django.urls import path
from accounts import views as accounts_views
from LsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # accounts 앱
    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),
    path('profile/<int:pk>', accounts_views.profile, name='profile'),
    path('profile_update/', accounts_views.profile_update, name='profile_update')
    # url(r'^profile/(?P<pk>[0-9]+)/$', login_required(views.ProfileView.as_view()), name='profile'),
]
