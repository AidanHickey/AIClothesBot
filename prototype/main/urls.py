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
    path("change_favorite/<int:productid>/<int:userid>", views.change_favorite, name='change_favorite'),
    path("upload", views.upload, name='upload'),
    path("like-post", views.like_post, name="like-post"), 
    path("get_inbox/<int:userid>", views.get_inbox, name='get_inbox'),
    path("profile/<int:userid>", views.profile, name='profile'),
    path("follow", views.follow, name='follow'),
    path("message", views.message, name='message'),
    path("get_message/<int:userid>", views.get_message, name='get_message'),
    path("send_message", views.send_message, name='send_message'),
    path("change_favorite/<int:productid>/<int:userid>", views.change_favorite, name='change_favorite')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


