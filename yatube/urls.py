from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('__debug__/', include('debug_toolbar.urls'))
]
