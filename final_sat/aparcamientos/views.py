from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Parking, Selected_Parking, Comments, Style_CSS
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


def show_index(request):

    parkings = Parking.objects.all()
    for parking in parkings:
        parking.delete()

    theParser = make_parser()
    theHandler = myContentHandler()
    theParser.setContentHandler(theHandler)

    xmlFile = urllib.request.urlopen("http://datos.munimadrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=202584-0-aparcamientos-residentes&mgmtid=e84276ac109d3410VgnVCM2000000c205a0aRCRD&preview=full")
    theParser.parse(xmlFile)
    
    context = {}
    parkings = Parking.objects.all()
    context['user'] = request.user

    return render_to_response('index.html',context)


def aparcamientos(request):
    context = {}
    context['user'] = request.user
    context['parkings'] = Parking.objects.all()
    return render_to_response('aparcamientos.html', context)

def aparcamientos_id(request,id):
    print (id)
    context = {}
    context['parking'] = Parking.objects.filter(id_entidad=id).first()
    return render_to_response('aparcamientos_id.html', context)


@csrf_exempt
def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
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


def about(request):
    return render_to_response('about.html')
