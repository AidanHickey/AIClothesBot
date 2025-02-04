from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path("", views.index, name='index'),
    path("marketplace", views.marketplace, name="marketplace"),
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("logout", views.logout, name="logout"),
    path("get_favorite/<int:userid>", views.get_favorite, name='get_favorite'),
    path("change_favorite/<int:productid>/<int:userid>", views.change_favorite, name='change_favorite')
]

