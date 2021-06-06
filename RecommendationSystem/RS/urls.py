from . import views
from django.urls import path,include

app_name = "RS"
urlpatterns=[
path('',views.home,''),

path('new',views.new_user,name='new'),
path('login',views.user_login,name='login'),
path('logout',views.logout_request,name='logout'),
path('search/',views.search_box,name='search'),
path('recommendation/<str:search>/',views.recommendations,name='recommendation'),
path('details/<str:medicine>',views.view_details,name='details'),
path('expert_advice',views.expert_advice,name='expert_advice'),
]