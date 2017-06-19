from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from aparcamientos.models import Parking, Selected_Parking, Comments, Style_CSS
from operator import itemgetter
import urllib.request
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from aparcamientos.xml_parser import myContentHandler
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def show_index(request):

    all_parkings = Parking.objects.all()
    for parking in all_parkings:
        parking.delete()

    theParser = make_parser()
    theHandler = myContentHandler()
    theParser.setContentHandler(theHandler)

    xmlFile = urllib.request.urlopen("http://datos.munimadrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=202584-0-aparcamientos-residentes&mgmtid=e84276ac109d3410VgnVCM2000000c205a0aRCRD&preview=full")
    theParser.parse(xmlFile)

    return HttpResponse ("FUNCIONA")
