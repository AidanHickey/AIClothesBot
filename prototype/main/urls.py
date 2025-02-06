from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "main"
urlpatterns = [
    path("", views.index, name='index'),
    path("marketplace", views.marketplace, name="marketplace"),
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("logout", views.logout, name="logout"),
    path("settings", views.settings, name="settings"),
    path("get_favorite/<int:userid>", views.get_favorite, name='get_favorite'),
    path("change_favorite/<int:productid>/<int:userid>", views.change_favorite, name='change_favorite')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


