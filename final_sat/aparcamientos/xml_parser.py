#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from xml.sax import SAXParseException
import sys
import urllib.request
from aparcamientos.models import Parking


def normalize_whitespace(text):
    return string.join(string.split(text), ' ')


class myContentHandler(ContentHandler):

    def __init__ (self):
        self.inContent = False
        self.theContent = ""
        self.attribute = ""
        self.first_parking = True
        #campos de un aparcamiento:
        self.id_entidad = ""
        self.nombre = ""
        self.descripcion = ""
        self.accesibilidad = ""
        self.url = ""
        self.direccion = ""
        self.via = ""
        self.barrio = ""
        self.distrito = ""
        self.latitud = ""
        self.long = ""
        self.contacto = ""

    def startElement (self, name, attrs):
        if name == 'contenido' and not self.first_parking: #guarda el parking anterior
            parking = Parking(id_entidad = self.id_entidad, nombre = self.nombre,
                            descripcion = self.descripcion, accesibilidad = self.accesibilidad,
                            url = self.url, direccion = self.direccion, barrio = self.barrio,
                            distrito = self.distrito, latitud = self.latitud,
                            longitud = self.long, contacto = self.contacto).save()

        if name == 'atributo':
            self.attribute = attrs.get("nombre")
        if self.attribute in ["ID-ENTIDAD","NOMBRE", "DESCRIPCION", "ACCESIBILIDAD", "CONTENT-URL", "NOMBRE-VIA", "CLASE-VIAL", "NUM", "CODIGO-POSTAL", "BARRIO", "DISTRITO", "LATITUD", "LONGITUD", "TELEFONO", "EMAIL", "TIPO"]:
            self.inContent = True


    def endElement (self, name):

        if self.attribute == "ID-ENTIDAD":
            if self.first_parking:
                self.first_parking = False
            self.id_entidad = int(self.theContent)
        if self.attribute == "NOMBRE":
            self.nombre = self.theContent
        elif self.attribute == "DESCRIPCION":
            self.descripcion = self.theContent
        elif self.attribute == "ACCESIBILIDAD":
            self.accesibilidad = int(self.theContent)
        elif self.attribute == "CONTENT-URL":
            self.url = self.theContent

        # direccion
        elif self.attribute == "NOMBRE-VIA":
            self.via = self.theContent
        elif self.attribute == "CLASE-VIAL":
            self.direccion = self.theContent + " " + self.via
        elif self.attribute == "NUM":
            self.direccion += ", " + self.theContent
        elif self.attribute == "CODIGO-POSTAL":
            self.direccion += "\n CP: " + self.theContent + " MADRID"
        # fin direccion

        elif self.attribute == "BARRIO":
            self.barrio = self.theContent
        elif self.attribute == "DISTRITO":
            self.distrito = self.theContent
        elif self.attribute == "LATITUD":
            self.latitud = self.theContent
        elif self.attribute == "LONGITUD":
            if self.theContent != "":
                self.long = self.theContent

        # contacto
        elif self.attribute == "TELEFONO":
            self.contacto = self.theContent + "\n"
        elif self.attribute == "EMAIL":
            self.contacto += self.theContent
        # fin contacto

        if self.contacto == "":
            self.contacto = "NO HAY DATOS DE CONTACTO"

        self.inContent = False
        self.theContent = ""


    def characters (self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars
