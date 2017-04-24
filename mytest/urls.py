from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    
    ] 