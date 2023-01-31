from django.urls import path

from bankapp import views
from bankapp.views import AjaxHandlerView

app_name = 'bankapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('form/',views.form,name='form'),
    path('form/get_branch',AjaxHandlerView.as_view()),
]