from django.urls import path
from . import views
from django.conf.urls.static import static

from .. import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
