from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
     url(r'^admin/', admin.site.urls),
     url(r'^', include('post.urls')),   # To make post app available at /
   ]