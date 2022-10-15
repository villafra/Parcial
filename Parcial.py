import numpy as np
import datetime as dt
from enum import Enum


class Usuario:
    def __init__(self, tipo, numero, nombre, apellido):
        self.tipo = tipo
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
    def __str__(self):
        return f"{self.nombre} {self.apellido}" 

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

  ListaUsuarios = 

CrearUsuario()