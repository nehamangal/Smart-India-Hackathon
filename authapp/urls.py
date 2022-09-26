from django import views
from django.urls import path,include
from . import views

app_name= 'userapp'

urlpatterns = [
  path('',views.base,name='base'),
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.user_login,name='login'),
    path('profile/',views.user_profile,name='profile'),
    path('logout/',views.user_logout,name='logout'),
    path('main/',views.main,name='main'),
    path('changepass/',views.user_change_pass,name='changepass'),
    path('news/',views.news,name='news'),
    # path('profilenew/',views.profilenew,name='profilenew'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('userProfile/',views.UserProfile,name='UserProfile'),
    path('getmentor/',views.getmentor,name='getmentor'),
    path('networking/',views.networking,name='networking'),
    path('map/',views.map,name='map'),
    path('cardsfront/',views.cardsfront,name='cardsfront'),
    path('newsfront/',views.newsfront,name='newsfront'),
    path('joinhub/',views.joinhub,name='joinhub'),

    
    path('investors/',views.investors,name='investors'),
    path('idea/',views.idea,name='idea'),
    path('pich/',views.pich,name='pich'),
    path('go/',views.go,name='go'),
    path('revenue/',views.revenue,name='revenue'),
    path('prototype/',views.prototype,name='prototype'),
    path('fundraising/',views.fundraising,name='fundraising'),
    path('mentorp/',views.mentorp,name='mentorp'),
    path('mentordesc/',views.mentordesc,name='mentordesc'),
    path('accv/',views.acv,name='accv'),
    path('acc/',views.ac,name='acc'),
    


]