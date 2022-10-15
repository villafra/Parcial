
from ast import Not
from pickle import LIST
import numpy as np
import datetime as dt
from enum import Enum


ListaUsuarios = []
class Usuario:
    def __init__(self, tipo, numero, nombre, apellido):
        self.tipo = tipo
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
    def __str__(self):
        return f"{self.nombre} {self.apellido}" 
persona = Usuario("DNI", 123, "asd", "sad")
ListaUsuarios.append(persona)
persona = Usuario("DNI", 122, "assasd", "sad")
ListaUsuarios.append(persona)
class Tarjeta:
    def __init__(self, fechaotorga):
        self.fechaotorgacion = fechaotorga

    titular = ""
    numero = 1
    def Titular(self, usuario):
        self.titular = usuario

class Platinum(Tarjeta):
    def SetNumero(self, numero):
        if len(str(numero))==12:
            self.numero = "9999" + str(numero)

class TipoID(Enum):
    DNI = 1
    Pasaporte = 2

def MenuPrincipal():
   print ("Banco Monte Dei Paschi")
   print ("Por favor elija un item del menu:\n\
   1-Clientes\n\
   2-Tarjetas\n\
   3-Operaciones\n\
   4-Salir\n")

   opcion = int(input())

   #while opcion < 4:

def CrearUsuario():
    print("Elija Tipo Documento:\n\
    1-DNI\n\
    2-Pasaporte\n")
    tipo = TipoID(int(input())).name
    print(f"Ingrese {tipo}:\n")
    numero = int(input())
    print ("Ingrese Nombre:\n")
    nombre = str(input())
    print ("Ingrese Apellido:\n")
    apellido = str(input())

    nuevo = Usuario(tipo, numero, nombre, apellido)
    if len(ListaUsuarios)!=0:
        if ValidarID(nuevo.numero):
            ListaUsuarios.append(nuevo)
            print (f"{nuevo} se ha agregado al sistema")
            MenuPrincipal()
        else:
            print("El usuario ya existe.")
            CrearUsuario()
    else:
        ListaUsuarios.append(nuevo)
        print (f"{nuevo} se ha agregado al sistema\n")
        MenuPrincipal()


def ValidarID(numero):
    sino = True
    for dni in ListaUsuarios:
            if dni.numero == numero:
                sino = False
    return sino

def BuscarIndex(numero):
    for dni in ListaUsuarios:
        if dni.numero == numero:
            indice = ListaUsuarios.index(dni)
    return indice

def ModificarUsuario(modificado):

    print("Ingrese Numero de documento:\n")
    numero = int(input())
    if not ValidarID(numero):
        indice = BuscarIndex(numero)
        ListaUsuarios.pop(indice)
        ListaUsuarios.append(modificado)

def EliminarUsuario():
    print("Ingrese Numero de documento:\n")
    numero = int(input())
    if not ValidarID(numero):
        indice = BuscarIndex(numero)
        ListaUsuarios.pop(indice)
     
ModificarUsuario()
for x in ListaUsuarios:
    print(x)