from django.urls import path

from users.apps import UsersConfig
from users.views import user_register_view, user_login_view, user_profile_view, user_logged_out_view, user_update_view, \
    user_change_password_view, user_generate_new_passport_view

app_name = UsersConfig.name

urlpatterns = [
    path("register/", user_register_view, name="user_register"),
    path("user_login", user_login_view, name="user_login"),
    path("profile/", user_profile_view, name="user_profile"),
    path('logout', user_logged_out_view, name='user_logout', ),
    path('update/', user_update_view, name= 'user_update',),
    path("change_password/",user_change_password_view,name='user_change_password'),
    path('profile/genpassword/',user_generate_new_passport_view,name='user_generate_new_password')
]
