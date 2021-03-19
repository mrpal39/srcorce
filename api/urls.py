
from django.urls import path,include
from . import views
from.views import GetDroplets
urlpatterns = [
 
        path('', GetDroplets.as_view(template_name='platform.html'), name='template1'),
        path('s/',views.getsearch,name="search"),

]

