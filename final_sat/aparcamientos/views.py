from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from .models import Parking, Users_Page, Users_Favs, Comment
from operator import itemgetter
import urllib.request
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from aparcamientos.xml_parser import myContentHandler
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User as user
from django.contrib.auth import authenticate, login, logout
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

accesibilidad_on = False
error_loading = False
filtro_dist = ""

@csrf_exempt
def cargar_aparcamientos(request):
    if request.user in user.objects.all():
        parkings = Parking.objects.all()
        for parking in parkings:
            parking.delete()

        theParser = make_parser()
        theHandler = myContentHandler()
        theParser.setContentHandler(theHandler)
        xmlFile = urllib.request.urlopen("http://datos.munimadrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=202584-0-aparcamientos-residentes&mgmtid=e84276ac109d3410VgnVCM2000000c205a0aRCRD&preview=full")
        theParser.parse(xmlFile)

    else:
        global error_loading
        error_loading = True
    return redirect('/')


def show_index(request):
    context = {}
    parkings = Parking.objects.all()
    context['user'] = request.user
    users_css = user.objects.filter(username=request.user.username).first()
    context['usuario_css'] = Users_Page.objects.filter(usuario=users_css).first()
    context['users_list'] = Users_Page.objects.all()
    global accesibilidad_on
    context['accesibilidad_on'] = accesibilidad_on
    if accesibilidad_on:
        context['parkings'] = Parking.objects.filter(accesibilidad=1).order_by("-likes")[:5]
    else:
        context['parkings'] = Parking.objects.all().order_by("-likes")[:5]
    global error_loading
    context['error_loading'] = error_loading
    context['parkings_loaded'] = (len(parkings) != 0)
    return render_to_response('index.html',context)


def aparcamientos(request):
    global filtro_dist
    filtro_dist = ""

    context = {}
    context['user'] = request.user
    users_css = user.objects.filter(username=request.user.username).first()
    context['usuario_css'] = Users_Page.objects.filter(usuario=users_css).first()
    context['users_list'] = Users_Page.objects.all()
    global accesibilidad_on
    if accesibilidad_on:
        context['parkings'] = Parking.objects.filter(accesibilidad=1)
    else:
        context['parkings'] = Parking.objects.all()
    return render_to_response('aparcamientos.html', context)


def filtrar_distrito(request,dist):
    global filtro_dist
    filtro_dist = dist
    context = {}
    context['user'] = request.user
    users_css = user.objects.filter(username=request.user.username).first()
    context['usuario_css'] = Users_Page.objects.filter(usuario=users_css).first()
    context['users_list'] = Users_Page.objects.all()
    distr = dist.replace("_", " ")
    global accesibilidad_on
    if accesibilidad_on:
        context['parkings'] = Parking.objects.filter(accesibilidad=1).filter(distrito=distr)
    else:
        context['parkings'] = Parking.objects.filter(distrito=distr)
    return render_to_response('aparcamientos.html', context)


def sumar_like(request, id_parking):
    parking = Parking.objects.get(id_entidad=id_parking)
    parking.likes += 1
    parking.save()
    return redirect('/aparcamientos/')


def favoritos_add(request, id_parking):
    parking_fav = Users_Favs.objects.filter(usuario=request.user, id_entidad=id_parking).first()
    if not parking_fav:
        Users_Favs.objects.create(
            usuario = request.user,
            id_entidad = id_parking,
        )
    return redirect('/aparcamientos/')


def favoritos_del(request, id_parking):
    parking_fav = Users_Favs.objects.filter(usuario=request.user, id_entidad=id_parking).first()
    if parking_fav:
        parking_fav.delete()
    return redirect("/"+request.user.username+"/")


def aparcamientos_id(request,id_parking):
    context = {}
    context['user'] = request.user
    users_css = user.objects.filter(username=request.user.username).first()
    context['usuario_css'] = Users_Page.objects.filter(usuario=users_css).first()
    favs = Users_Favs.objects.filter(usuario=users_css)
    context['favoritos'] = favs
    context['users_list'] = Users_Page.objects.all()
    context['parking'] = Parking.objects.filter(id_entidad=id_parking).first()
    context['comentarios'] = Comment.objects.filter(id_entidad=id_parking)
    return render_to_response('aparcamientos_id.html', context)


@csrf_exempt
def comentarios_add(request,id_parking):
    if request.method == 'POST':
        titulo_c = request.POST['titulo_c']
        if titulo_c == "":
            titulo = "Sin título"
        texto_c = request.POST['texto_c']

        Comment.objects.create(
            id_entidad = id_parking,
            titulo = titulo_c,
            texto = texto_c,
            autor = request.user,
        )
    return redirect("/aparcamientos/"+id_parking)


def accesibilidad(request):
    global accesibilidad_on
    if accesibilidad_on:
        accesibilidad_on = False
    else:
        accesibilidad_on = True
    return redirect('/')


def xml_inicio(request):
    context = {}
    global accesibilidad_on
    if accesibilidad_on:
        context['parkings'] = Parking.objects.filter(accesibilidad=1).order_by("-likes")[:5]
    else:
        context['parkings'] = Parking.objects.all().order_by("-likes")[:5]
    context['comentarios'] = Comment.objects.all()
    return render_to_response('xml_inicio.html', context, content_type='text/xml')


def json_inicio(request):
    context = {}
    global accesibilidad_on
    if accesibilidad_on:
        context['parkings'] = Parking.objects.filter(accesibilidad=1).order_by("-likes")[:5]
    else:
        context['parkings'] = Parking.objects.all().order_by("-likes")[:5]
    context['comentarios'] = Comment.objects.all()
    return render_to_response('json_inicio.html', context, content_type='text/json')


def rss_comentarios(request):
    context = {}
    context['comentarios'] = Comment.objects.all()
    return render_to_response('rss_comentarios.html', context, content_type='text/rss')


def pagina_usuario(request,usuario_pag):
    context = {}
    context['user'] = request.user
    users_css = user.objects.filter(username=request.user.username).first()
    context['usuario_css'] = Users_Page.objects.filter(usuario=users_css).first()
    users_page = user.objects.filter(username=usuario_pag).first()
    context['usuario_pagina'] = Users_Page.objects.filter(usuario=users_page).first()
    context['pagina_propia'] = str(request.user.username) == str(Users_Page.objects.filter(usuario=users_page).first().usuario)
    context['users_list'] = Users_Page.objects.all()
    favs = Users_Favs.objects.filter(usuario=users_page)
    context['favoritos'] = favs
    context['parkings'] = []
    for fav in favs:
        parking = Parking.objects.get(id_entidad=fav.id_entidad)
        context['parkings'].append(parking)
    return render_to_response('usuario.html', context)


def xml_usuario(request,usuario_pag):
    context = {}
    users_page = user.objects.filter(username=usuario_pag).first()
    context['usuario_pagina'] = Users_Page.objects.filter(usuario=users_page).first()
    favs = Users_Favs.objects.filter(usuario=users_page)
    context['favoritos'] = favs
    context['parkings'] = []
    for fav in favs:
        parking = Parking.objects.get(id_entidad=fav.id_entidad)
        context['parkings'].append(parking)
    context['comentarios'] = Comment.objects.all()
    return render_to_response('xml_usuario.html', context, content_type='text/xml')


def json_usuario(request,usuario_pag):
    context = {}
    users_page = user.objects.filter(username=usuario_pag).first()
    context['usuario_pagina'] = Users_Page.objects.filter(usuario=users_page).first()
    favs = Users_Favs.objects.filter(usuario=users_page)
    context['favoritos'] = favs
    context['parkings'] = []
    for fav in favs:
        parking = Parking.objects.get(id_entidad=fav.id_entidad)
        context['parkings'].append(parking)
    context['comentarios'] = Comment.objects.all()
    return render_to_response('json_usuario.html', context, content_type='text/json')


def preferencias(request):
    context = {}
    context['user'] = request.user
    users_page = user.objects.filter(username=request.user.username).first()
    context['usuario_css'] = Users_Page.objects.filter(usuario=users_page).first()
    context['usuario_pagina'] = Users_Page.objects.filter(usuario=users_page).first()
    context['users_list'] = Users_Page.objects.all()
    return render_to_response('preferencias.html', context)


@csrf_exempt
def cambiar_titulo(request):
    if request.method == 'POST':
        titulo_nuevo = request.POST['nuevo_titulo']
        usuario_pagina = Users_Page.objects.get(usuario=request.user)
        usuario_pagina.titulo = titulo_nuevo
        usuario_pagina.save()
    return redirect("/"+request.user.username+"/")


@csrf_exempt
def cambiar_css(request):
    if request.method == 'POST':
        color_nuevo = request.POST['nuevo_color']
        bg_nuevo = request.POST['nuevo_bg']
        usuario_pagina = Users_Page.objects.get(usuario=request.user)
        usuario_pagina.color = color_nuevo
        usuario_pagina.background = bg_nuevo
        font_nuevo = request.POST['nuevo_font']
        if font_nuevo == "":
            font_nuevo = usuario_pagina.font_size
        usuario_pagina.font_size = font_nuevo
        usuario_pagina.save()
    return redirect("/"+request.user.username+"/")


@csrf_exempt
def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request,user)
        if not hasattr(user, 'usuario'):
            titulo = "Página de " + username
            usuario = Users_Page(usuario=user, titulo=titulo).save()
        # Redirect to a success page.
        return redirect('/')
    else:
        # Return an 'invalid login' error message.
        print('error')
        return redirect('/')


@csrf_exempt
def log_out(request):
    logout(request)
    return redirect('/')


def registro(request):
    context = {}
    context['users_list'] = Users_Page.objects.all()
    return render_to_response("registro.html",context)


@csrf_exempt
def sign_up(request):
    username = request.POST['username']
    password = request.POST['password-1']
    password_2 = request.POST['password-2']
    if password == password_2:
        usuario = authenticate(username=username, password=password)
        if usuario is None:
            user.objects.create_user(username, "", password)
            usuario = authenticate(username=username, password=password)
            login(request,usuario)
            Users_Page.objects.create(
                usuario = usuario,
                titulo = "Página de " + username,
            )
    return redirect("/")




def about(request):
    context = {}
    context['user'] = request.user
    users_css = user.objects.filter(username=request.user.username).first()
    context['usuario_css'] = Users_Page.objects.filter(usuario=users_css).first()
    context['users_list'] = Users_Page.objects.all()
    return render_to_response('about.html', context)
