
from django.urls import path,include
from . import views
from.views import GetDroplets
urlpatterns = [
 
        path('', GetDroplets.as_view(template_name='upload.html'), name='Droplet View'),
    
]

