from django.urls import path,include
from .import views
from django.contrib.auth import views as auth_view
# from django.contrib.auth import views as auth_views




urlpatterns = [
    # path(),
    # path(),
    # path('', views.home, name='index' ),
    path('login/', views.my_view, name='index' ),
    # path('', views.index, name='index' ),

]
 