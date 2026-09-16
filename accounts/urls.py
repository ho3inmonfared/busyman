from django.urls import path
from . import views


app_name = "accounts"


urlpatterns = [

    path(
        "login/",
        views.phone_login,
        name="phone_login"
    ),

    path(
        "verify-otp/",
        views.verify_otp_view,
        name="verify_otp"
    ),

    path(
        "profile/",
        views.complete_profile,
        name="complete_profile"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),

]