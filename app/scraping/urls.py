from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('get_all_face_insta_accounts/',views.get_all_face_insta_accounts,name='get_all_face_insta_accounts'),
    path('get_specific_account/<int:faceid>',views.get_specific_account,name='get_specific_account'),
    path('get_all_adds_face_insta/',views.get_all_adds_face_insta,name='get_all_adds_face_insta'),
]
