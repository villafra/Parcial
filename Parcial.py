
from email.policy import default
import numpy as np
import datetime as dt
from Clases import *
import random as rnd


ListaUsuarios = []
ListaTarjetas = []

persona = Usuario("DNI", 123, "asd", "sad")
ListaUsuarios.append(persona)
persona = Usuario("DNI", 122, "assasd", "sad")
ListaUsuarios.append(persona)



def MenuPrincipal():
   print ("Banco Monte Dei Paschi")
   print ("Por favor elija un item del menu:\n\
   1-Clientes\n\
   2-Tarjetas\n\
   3-Operaciones\n\
   4-Salir\n")
   try:
    opcion = int(input())
   except ValueError:
       MenuPrincipal()

   while opcion < 5:
       if opcion == 1:
           MenuCliente()
           break
       elif opcion == 2:
           MenuTarjeta()
           break
       elif opcion == 3:
           pass
       elif opcion == 4:
           quit()
   else:
        MenuPrincipal()

def MenuCliente():
    print("Por favor elija un item del menu:\n\
        1-Crear Usuario\n\
        2-Modificar Usuario\n\
        3-Eliminar Usuario\n\
        4-Salir\n")
    try:
        menu1= int(input())
    except ValueError:
            MenuCliente()
    while menu1 < 5:
        if menu1 == 1:
            CrearUsuario()
            break
        if menu1 == 2:
            ModificarUsuario()
            break
        if menu1 == 3:
            EliminarUsuario()
            break
        if menu1 == 4:
            MenuPrincipal()
            break
        print("Por favor elija un item del menu:\n\
        1-Crear Usuario\n\
        2-Modificar Usuario\n\
        3-Eliminar Usuario\n\
        4-Salir\n")
    else:
        MenuCliente()

def MenuTarjeta():
    print("Por favor elija un item del menu:\n\
        1-Asignar Tarjeta\n\
        2-Modificar Saldo\n\
        3-Eliminar tarjeta\n\
        4-Salir\n")
    try:
        menu2= int(input())
    except ValueError:
            MenuTarjeta()
    while menu2 <5:
        if menu2 == 1:
            CrearTarjeta()
            break
        if menu2 == 2:
            ModificarLimite()
            break
        if menu2 == 3:
            EliminarTarjeta()
            break
        if menu2 == 4:
            MenuPrincipal()
            break
    else:
        MenuTarjeta()
        
def Operaciones():
    pass
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
            MenuCliente()
        else:
            print("El usuario ya existe.")
            CrearUsuario()
    else:
        ListaUsuarios.append(nuevo)
        print (f"{nuevo} se ha agregado al sistema\n")
        MenuCliente()


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

def ModificarUsuario():
    print("Ingrese Numero de documento:\n")
    numero = int(input())
    if not ValidarID(numero):
        indice = BuscarIndex(numero)
        aux = ListaUsuarios[indice]
        ListaUsuarios.pop(indice)
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
        modificado = Usuario(tipo, numero, nombre, apellido)
        ListaUsuarios.insert(indice,modificado)

def EliminarUsuario():
    print("Ingrese Numero de documento:\n")
    numero = int(input())
    if not ValidarID(numero):
        indice = BuscarIndex(numero)
        ListaUsuarios.pop(indice)
     
def GenerarNumero():
    nuevonumero = str(rnd.randint(0,9))
    for x in range(11):
        nuevonumero += str(rnd.randint(0,9))
    return nuevonumero

def ValidarNumero(numero):
    for ID in ListaTarjetas:
            if ID.numero == numero:
                ValidarNumero(GenerarNumero())
    return numero

def CrearTarjeta(usuario):
    print("Elija Nivel Tarjeta:\n\
         1-Platinum\n\
         2-Gold\n\
         3-Plata\n")
    tipo = TipoTarjeta(int(input()))
    if tipo == TipoTarjeta.Platinum:
        tarjeta = Platinum(dt.date.today(), usuario)
        tarjeta.Setnumero(ValidarNumero(GenerarNumero()))    
    elif tipo == TipoTarjeta.Gold:
        tarjeta = Gold(dt.date,usuario)
        tarjeta.Setnumero(ValidarNumero(GenerarNumero()))
    elif tipo == TipoTarjeta.Plata:
        tarjeta = Plata(dt.date, usuario)
        tarjeta.Setnumero(ValidarNumero(GenerarNumero()))
    return tarjeta


def ModificarLimite(numero):
    print("Ingrese Nuevo Limite de Pesos:\n")
    print("(0 para no modificar)")
    pesos = float(input())
    print("Ingrese Nuevo Limite de Dolares:\n")
    print("(0 para no modificar)")
    dolares = float(input())
    for tarjeta in ListaTarjetas:
        if tarjeta.numero == numero:
            tarjeta.ModificarLimite(pesos, dolares)


def EliminarTarjeta(numero):
    for tarjeta in ListaTarjetas:
        if tarjeta.numero == numero:
            if tarjeta.AcumuladoPesos == 0 & tarjeta.AcumuladoDolares == 0:
                ListaTarjetas.pop(ListaTarjetas.index(tarjeta))


MenuPrincipal()