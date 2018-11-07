from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('sign_in/', views.sign_in, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('demo/', views.index, name='index'),
    path("search/", views.search, name="search"),
    path("mon_electeur/", views.mon_electeur, name="mon_electeur"),
    path("get_person_info/", views.get_person_info, name="get_person_info"),
    path("create_person/", views.create_person, name="create_person"),
]
