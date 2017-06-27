"""final_sat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from django.contrib.auth.views import logout
from aparcamientos import views


admin.autodiscover()


urlpatterns = [
    url(r'^$', 'aparcamientos.views.show_index',),
    url(r'^xml/$', 'aparcamientos.views.xml_inicio',),
    url(r'^json/$', 'aparcamientos.views.json_inicio',),
    url(r'^rss/$', 'aparcamientos.views.rss_comentarios',),
    url(r'^registro/$', 'aparcamientos.views.registro',),
    url(r'^sign_up/$','aparcamientos.views.sign_up',),
    url(r'^login/$', 'aparcamientos.views.log_in',),
    url(r'^logout/$', 'aparcamientos.views.log_out',),
    url(r'^aparcamientos/$', 'aparcamientos.views.aparcamientos',),
    url(r'^aparcamientos/(?P<id_parking>\d+)/$', 'aparcamientos.views.aparcamientos_id',),
    url(r'^add_comentario/(?P<id_parking>\d+)/$', 'aparcamientos.views.comentarios_add',),
    url(r'^sumar_like/(?P<id_parking>\d+)/$', 'aparcamientos.views.sumar_like',),
    url(r'^favoritos/add/(?P<id_parking>\d+)/$', 'aparcamientos.views.favoritos_add',),
    url(r'^favoritos/del/(?P<id_parking>\d+)/$', 'aparcamientos.views.favoritos_del',),
    url(r'^accesibilidad/$', 'aparcamientos.views.accesibilidad',),
    url(r'^cargar_aparcamientos/$', 'aparcamientos.views.cargar_aparcamientos',),
    url(r'^preferencias/$', 'aparcamientos.views.preferencias',),
    url(r'^cambiar_titulo/$', 'aparcamientos.views.cambiar_titulo',),
    url(r'^cambiar_css/$', 'aparcamientos.views.cambiar_css',),
    url(r'^filtrar_distrito/(?P<dist>\S+)/$', 'aparcamientos.views.filtrar_distrito',),
    url(r'^about/$', 'aparcamientos.views.about',),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<usuario_pag>\w+)/$', 'aparcamientos.views.pagina_usuario',),
    url(r'^(?P<usuario_pag>\w+)/xml/$', 'aparcamientos.views.xml_usuario',),
    url(r'^(?P<usuario_pag>\w+)/json/$', 'aparcamientos.views.json_usuario',),

]
