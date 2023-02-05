from django.urls import path
from . import views
urlpatterns = [
    path('home',views.home,name="home"),
    path('logout',views.logout,name="logout"),
    path('helpnow',views.help,name="helpnow"),
    path('ngodashboard',views.ngodash,name="ngodashboard"),
    path('dashboard',views.dash,name="dashboard"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('upload/<ngoname>/<ngoemail>',views.upload,name="upload"),
    path('ngologin',views.ngologin,name="ngologin"),
    path('ngoregister',views.ngoregister,name="ngoregister"),
    path('success/<id>',views.success,name="success"),
]
