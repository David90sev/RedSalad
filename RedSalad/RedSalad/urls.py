"""RedSalad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from usuarios.views import IndexView,LogOut, LoginViewL
from django.conf.urls.static import static
from django.conf import settings
import usuarios

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view()),
    url('', include('social_django.urls', namespace='social')),
    url(r'iniciar$', LoginViewL.as_view()),
    url(r'salir$', LogOut),
    
]

#usuarios
urlpatterns+= [
    url(r'usuario/nuevoproductor$', usuarios.views.ProductorCrear_Usuario.as_view(), name='productor_crear_usuario'),
    url(r'usuario/nuevoproductor/2$', usuarios.views.ProductorCrear_Productor.as_view(), name='productor_crear_productor'),

    #url(r'usuario/nuevocliente', usuarios.views.nuevo_cliente, name='nuevo_cliente'),

    url(r'usuario/miperfilproductor/(?P<pk>[0-9]+)/$', usuarios.views.PerfilProductorView.as_view(), name='productor_perfil'),
    
    
    
    ]






if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

