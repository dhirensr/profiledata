from django.urls import path

from . import views

app_name = 'enterdata'
urlpatterns = [
    path('',views.enterdata,name='enterdata'),
    path('profiles/',views.viewdata,name='viewdata'),
    path('profile/<int:profile_id>',views.viewprofile,name='viewprofile')
]
