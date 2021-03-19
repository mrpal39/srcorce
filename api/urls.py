
from django.urls import path,include
from . import views
from.views import GetDroplets,Get_search,github
urlpatterns = [
 
        path('plat/', GetDroplets.as_view(template_name='platform.html'), name='platform'),
        path('s/',Get_search.as_view(template_name = "search.html"),name="search"),
        path('git/',github.as_view(template_name='git.html'),name="github"),


]

