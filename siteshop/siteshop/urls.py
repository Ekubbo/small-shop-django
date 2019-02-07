from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from shop.views import views_list_product
from django.conf.urls import include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views_list_product, name="index"),
    url(r'^shop/', include('shop.urls', namespace='shop')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
