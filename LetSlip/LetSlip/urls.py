from django.contrib import admin
from django.urls import path
from accounts import views as accounts_views
from LsApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # LsApp
    path('search/', views.search, name='search'),
    path('post_new', views.post_new, name='post_new'),
    path('post_detail/<int:post_id>', views.post_detail, name='post_detail'),
    path('comment_new/<int:post_id>', views.comment_new, name='comment_new'),
    
    # accounts
    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)