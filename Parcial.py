
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
            AsignarTarjeta()
            break
        if menu2 == 2:
            BuscarTitular()
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
    try:
        tipo = TipoID(int(input())).name
    except :
        print("Debe elegir 1 o 2\n")
        CrearUsuario()
    print(f"Ingrese {tipo}:\n")
    try:
        numero = int(input())
    except:
        print(f"Ingrese {tipo} sin puntos ni comas\n")
        CrearUsuario()
    print ("Ingrese Nombre:\n")
    nombre = str(input())
    print ("Ingrese Apellido:\n")
    apellido = str(input())

    nuevo = Usuario(tipo, numero, nombre, apellido)
    if ListaUsuarios:
        if ValidarID(nuevo.numero):
            ListaUsuarios.append(nuevo)
            print (f"{nuevo} se ha agregado al sistema.\n")
            MenuCliente()
        else:
            print("El usuario ya existe.\n")
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
    print("Ingrese Numero de documento de usuario a modificar:")
    try:
        numero = int(input())
    except:
        print(f"Ingrese documento sin puntos ni comas\n")    
    if not ValidarID(numero):
        indice = BuscarIndex(numero)
        aux = ListaUsuarios[indice]
        ListaUsuarios.pop(indice)
        print(f"Modificar tipo documento? Dato actual: {aux.tipo}")
        print("1-Si")
        print("2-No")
        try:
            respuesta = int(input())
            if respuesta == 1:
                print("Elija nuevo tipo documento:\n\
                    1-DNI\n\
                    2-Pasaporte\n")
                try:
                    tipo = TipoID(int(input())).name
                except :
                    print("Debe elegir 1 o 2\n")
                    ListaUsuarios.insert(indice, aux)
                    ModificarUsuario()
            elif respuesta == 2:
                tipo = aux.tipo
            else:
                print("Debe elegir 1 o 2\n")
                ListaUsuarios.insert(indice, aux)
                ModificarUsuario()
        except:
            ListaUsuarios.insert(indice, aux)
            ModificarUsuario()
        print(f"Modificar numero documento? Dato actual: {aux.numero}")
        print("1-Si")
        print("2-No")
        try:
            respuesta = int(input())
            if respuesta == 1:
                print(f"Ingrese nuevo {tipo}:")
                try:
                    numero = int(input())
                except :
                    print(f"Ingrese {tipo} sin puntos ni comas\n")
                    ListaUsuarios.insert(indice, aux)
                    ModificarUsuario()
            elif respuesta == 2:
                numero = aux.numero
            else:
                print("Debe elegir 1 o 2\n")
                ListaUsuarios.insert(indice, aux)
                ModificarUsuario()

        except:
            ListaUsuarios.insert(indice, aux)
            ModificarUsuario()
        print(f"Modificar nombre? Dato actual: {aux.nombre}")
        print("1-Si")
        print("2-No")
        try:
            respuesta = int(input())
            if respuesta == 1:
               print ("Ingrese nuevo Nombre:")
               nombre = str(input())
            elif respuesta == 2:
                nombre = aux.nombre
            else:
                print("Debe elegir 1 o 2\n")
                ListaUsuarios.insert(indice, aux)
                ModificarUsuario()
        except:
            ListaUsuarios.insert(indice, aux)
            ModificarUsuario()
        print(f"Modificar Apellido? Dato actual: {aux.apellido}")
        print("1-Si")
        print("2-No")
        try:
            respuesta = int(input())
            if respuesta == 1:
                print ("Ingrese nuevo Apellido:")
                apellido = str(input())
            elif respuesta == 2:
                apellido = aux.apellido
            else:
                print("Debe elegir 1 o 2\n")
                ListaUsuarios.insert(indice, aux)
                ModificarUsuario()
        except:
            ListaUsuarios.insert(indice, aux)
            ModificarUsuario()
        modificado = Usuario(tipo, numero, nombre, apellido)
        ListaUsuarios.insert(indice,modificado)
        print(f"El usuario {aux} ha sido modificado correctamente.")
        print("Los nuevos datos son:")
        print(f"{tipo}: {numero}")
        print(modificado)
        MenuCliente()

def EliminarUsuario():
    acumuladopesos = 0
    acumuladodolares = 0
    tarjetas = []
    print("Ingrese Numero de documento de usuario a eliminar:")
    numero = int(input())
    if not ValidarID(numero):
        indice = BuscarIndex(numero)
        aux = ListaUsuarios[indice]
        tarjetas = BuscarTarjeta(aux)
        if tarjetas:
            for tarjeta in tarjetas:
                if tarjeta.AcumuladoPesos > 0:
                    acumuladopesos += tarjeta.AcumuladoPesos
                if tarjeta.AcumuladoDolares >0:
                    acumuladodolares += tarjeta.AcumuladoDolares
            if acumuladopesos <= 0 & acumuladodolares <= 0:
                ListaUsuarios.pop(indice)
                print(f"El usuario {aux} ha sido eliminado de la base de datos.")
                MenuCliente()
            else:
                print(f"El usuario {aux} aun tiene tarjetas con deuda activa, no puede eliminarse.")
                MenuCliente()
        else:
            ListaUsuarios.pop(indice)
            print(f"El usuario {aux} ha sido eliminado de la base de datos.")
            MenuCliente()

def BuscarTarjeta(usuario):
    tarjetasxpersonas = []
    for tarjeta in ListaTarjetas:
        if tarjeta.titular.numero == usuario.numero:
            tarjetasxpersonas.append(tarjeta)
    return tarjetasxpersonas
            
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

def BuscarUsuarioDNI():
    print(f"Ingrese numero de documento:")
    usuarioencontrado = 0
    try:
       numero = int(input())
    except :
       print(f"Ingrese documento sin puntos ni comas\n")
    for usuario in ListaUsuarios:
        if usuario.numero == numero:
            usuarioencontrado = usuario
    if type(usuarioencontrado) != int:
        return usuarioencontrado
    else:
        return "No se ha encontrado el usuario"

def BuscarUsuarioxNombre():
    usuarios = []
    print(f"Ingrese apellido a buscar:")
    apellido = str(input())
    for usuario in ListaUsuarios:
        if usuario.apellido == apellido:
            usuarios.append(usuario)
    if usuarios:
        return usuarios
    else:
        return "No se ha encontrado usuario con ese apellido."

def AsignarTarjeta():
    print("Buscar usuario por: (elija la opcion correcta)")
    print("1-Apellido")
    print("2-Nro Documento")
    try:
        respuesta = int(input())
        if respuesta == 1:
            usuarios = BuscarUsuarioxNombre()
            if type(usuarios) != str:
                  for usuario in usuarios:
                      print(f"{usuario}, {usuario.tipo}:{usuario.numero}")
                  usuario = BuscarUsuarioDNI()
                  if type(usuario) != str:
                      print(f"Se le va a asignar una tarjeta a {usuario}")
                      print("Desea continuar?")
                      print("1-Si")
                      print("2-No")
                      try:
                         opcion = int(input())
                         if opcion == 1:
                                nuevatarjeta = CrearTarjeta(usuario)
                                ListaTarjetas.append(nuevatarjeta)
                                print(f"La tarjeta {nuevatarjeta} Nro: {nuevatarjeta.numero}")
                                print(f"Ha sido asignada a {usuario}")
                                MenuTarjeta()
                         else:
                             MenuTarjeta()
                      except:
                             print("Debe elegir 1 o 2\n")
                             MenuTarjeta()
                  else:
                        print(usuarios)
                        MenuTarjeta()
            else:
                  print(usuarios)
                  MenuTarjeta()
        elif respuesta == 2:
                  usuario = BuscarUsuarioDNI()
                  if type(usuario) != str:
                        print(f"Se le va a asignar una tarjeta a {usuario}")
                        print("Desea continuar?")
                        print("1-Si")
                        print("2-No")
                        try:
                            opcion = int(input())
                            if opcion == 1:
                                nuevatarjeta = CrearTarjeta(usuario)
                                ListaTarjetas.append(nuevatarjeta)
                                print(f"La tarjeta {nuevatarjeta} Nro: {nuevatarjeta.numero}")
                                print(f"Ha sido asignada a {usuario}")
                                MenuTarjeta()
                            else:
                                MenuTarjeta()
                        except:
                            print("Debe elegir 1 o 2\n")
                            MenuTarjeta()
                  else:
                        print(usuario)
                        MenuTarjeta()
        else:
                print("Debe elegir 1 o 2\n")
                MenuTarjeta()
    except:
        print("Debe elegir 1 o 2\n")
        MenuTarjeta()

def CrearTarjeta(usuario):
    aux = usuario
    print("Elija Nivel Tarjeta:\n\
         1-Platinum\n\
         2-Gold\n\
         3-Plata\n")
    try:
        tipo = TipoTarjeta(int(input()))
    except :
        print("Debe elegir de 1 a 3\n")
        CrearTarjeta(aux)
    if tipo == TipoTarjeta.Platinum:
        tarjeta = Platinum(dt.date.today(), usuario)
        tarjeta.Setnumero(ValidarNumero(GenerarNumero()))    
    elif tipo == TipoTarjeta.Gold:
        tarjeta = Gold(dt.date.today(),usuario)
        tarjeta.Setnumero(ValidarNumero(GenerarNumero()))
    elif tipo == TipoTarjeta.Plata:
        tarjeta = Plata(dt.date.today(), usuario)
        tarjeta.Setnumero(ValidarNumero(GenerarNumero()))
    return tarjeta

def BuscarTitular():
    print("Buscar usuario por: (elija la opcion correcta)")
    print("1-Apellido")
    print("2-Nro Documento")
    try:
        respuesta = int(input())
        if respuesta == 1:
            usuarios = BuscarUsuarioxNombre()
            if type(usuarios) != str:
                  for usuario in usuarios:
                      print(f"{usuario}, {usuario.tipo}:{usuario.numero}")
                  usuario = BuscarUsuarioDNI()
                  if type(usuario) != str:
                      modtarjeta = BuscarTarjeta(usuario)
                      x = 1
                      print("Elija una opcion de tarjeta de la lista:")
                      for tarjeta in modtarjeta:
                          print(f"{x}-{tarjeta} Nro:{tarjeta.numero}")
                          x += 1
                      try: 
                          ind = int(input())
                          ModificarLimite(modtarjeta[ind-1].numero)
                          print(f"La tarjeta {ListaTarjetas[ind-1]} Nro: {ListaTarjetas[ind-1].numero}")
                          print(f"Tiene ${ListaTarjetas[ind-1].limitePesos} de limite en Pesos")
                          print(f"y tiene ${ListaTarjetas[ind-1].limiteDolares} de limite en dolares")
                          MenuTarjeta()
                      except:
                          print(f"Solo puede elegir entre {x} opciones")
                  else:
                    MenuTarjeta()
            else:
                print(usuarios)
                MenuTarjeta()
        elif respuesta == 2:
                  usuario = BuscarUsuarioDNI()
                  if type(usuario) != str:
                      modtarjeta = BuscarTarjeta(usuario)
                      x = 1
                      print("Elija una opcion de tarjeta de la lista:")
                      for tarjeta in modtarjeta:
                          print(f"{x}-{tarjeta} Nro:{tarjeta.numero}")
                          x += 1
                      try: 
                          ind = int(input())
                          ModificarLimite(modtarjeta[ind-1].numero)
                          print(f"La tarjeta {ListaTarjetas[ind-1]} Nro: {ListaTarjetas[ind-1].numero}")
                          print(f"Tiene ${ListaTarjetas[ind-1].limitePesos} de limite en Pesos")
                          print(f"y tiene ${ListaTarjetas[ind-1].limiteDolares} de limite en dolares")
                          MenuTarjeta()
                      except:
                          print(f"Solo puede elegir entre {x} opciones")
                  else:
                        print(usuario)
                        MenuTarjeta()
        else:
                print("Debe elegir 1 o 2\n")
                MenuTarjeta()
    except:
        print("Debe elegir 1 o 2\n")
        MenuTarjeta()

def BuscarTarjeta(usuario):
    tarjetas =[]
    for tarjeta in ListaTarjetas:
        if tarjeta.titular.numero == usuario.numero:
            tarjetas.append(tarjeta)
    if tarjetas:
        return tarjetas
    else:
        return "El usuario no posee tarjetas activas."

def ModificarLimite(numero):
    print("Ingrese Nuevo Limite de Pesos:")
    print("(0 para no modificar)")
    pesos = float(input())
    print("Ingrese Nuevo Limite de Dolares:")
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