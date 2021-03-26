from django.urls import path
from antpage import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",views.index,name='antpage'),
    path("liked/",views.liked,name='antpage'),
    path("addformdata/",views.addformdata,name='addformdata'),
    path("statuslike/",views.statuslike,name='statuslike')

]