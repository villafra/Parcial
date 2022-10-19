import datetime as dt
from Clases import *
import random as rnd
import re


ListaUsuarios = []
ListaTarjetas = []

def MenuPrincipal():
   ListarConsigna()
   print ("\nBanco Monte Dei Paschi")
   print ("Por favor elija un item del menu:")
   print ("1-Clientes")
   print ("2-Tarjetas")
   print ("3-Operaciones")
   print ("4-Salir")
   
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
           Operaciones()
           break
       elif opcion == 4:
           quit()
   else:
        MenuPrincipal()

def MenuCliente():
    print("Por favor elija un item del menu:")
    print("1-Crear Usuario")
    print("2-Modificar Usuario")
    print("3-Eliminar Usuario")
    print("4-Salir")
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
 
    else:
        MenuCliente()

def MenuTarjeta():
    print("Por favor elija un item del menu:")
    print("1-Asignar Tarjeta")
    print("2-Modificar Saldo")
    print("3-Eliminar tarjeta")
    print("4-Salir")
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
            BuscarTitular(2)
            break
        if menu2 == 4:
            MenuPrincipal()
            break
    else:
        MenuTarjeta()
        
def Operaciones():
    print("Por favor elija un item del menu:")
    print("1-Listado de Clientes")
    print("2-Listado de Tarjetas")
    print("3-Pago de Tarjetas")
    print("4-Consumo de Tarjetas")
    print("5-Deuda Total de Cliente")
    print("6-Deuda de cliente por Tarjetas")
    print("7-Salir")
    try:
        menu3= int(input())
    except ValueError:
            Operaciones()
    while menu3 < 8:
        if menu3 == 1:
            ListarClientes()
            print("\n")
            Operaciones()
            break
        if menu3 == 2:
            ListarTarjetas()
            print("\n")
            Operaciones()
            break
        if menu3 == 3:
            PagarTarjetas()
            break
        if menu3 == 4:
            ListarClientes()
            DeclararConsumo(BuscarUsuarioDNI())
        if menu3 == 5:
            BuscarMoroso()
            Operaciones()
            break
        if menu3 == 6:
            BuscarMorosoXTarjeta()
            Operaciones()
        if menu3 == 7:
            MenuPrincipal()
            break
    else:
       Operaciones()
def CrearUsuario():
    print("Elija Tipo Documento:")
    print("1-DNI")
    print("2-Pasaporte")
    try:
        tipo = TipoID(int(input())).name
    except :
        print("Debe elegir 1 o 2\n")
        CrearUsuario()
    print(f"Ingrese {tipo}:")
    try:
        numero = str(input())
        if ValidarDNI(tipo, numero):
            pass
        else:
            print(f"Ingrese {tipo} sin puntos ni comas\n")
            CrearUsuario()
    except:
        print(f"Ingrese {tipo} sin puntos ni comas\n")
        CrearUsuario()
    print ("Ingrese Nombre:")
    nombre = str(input())
    print ("Ingrese Apellido:")
    apellido = str(input())
    if tipo == TipoID.Pasaporte.name:
        nuevo = Usuario(tipo, numero, nombre, apellido)
    else:
        nuevo = Usuario(tipo, int(numero), nombre, apellido)
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
    ListarClientes()
    print("Ingrese Numero de documento de usuario a modificar:")
    try:
        numero = str(input())
        if re.fullmatch(r"[0-9]{8}",numero):
            numero = int(numero)
        elif not re.fullmatch(r"[a-zA-Z]{3}[0-9]{6}", numero):
            print("Ingrese el documento en el formato correcto")
            ModificarUsuario()
    except:
        print(f"Ingrese documento sin puntos ni comas\n") 
        ModificarUsuario()
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
                print("Elija nuevo tipo documento:")
                print("1-DNI")
                print("2-Pasaporte")
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
    ListarClientes()
    print("Ingrese Numero de documento de usuario a eliminar:")
    try:
        numero = str(input())
        if re.fullmatch(r"[0-9]{8}",numero):
            numero = int(numero)
        elif not re.fullmatch(r"[a-zA-Z]{3}[0-9]{6}", numero):
            print("Ingrese el documento en el formato correcto")
            EliminarUsuario()
    except:
        print("Ingrese el documento en el formato correcto")
        EliminarUsuario()
    if not ValidarID(numero):
        indice = BuscarIndex(numero)
        aux = ListaUsuarios[indice]
        tarjetas = BuscarTarjeta(aux)
        if type(tarjetas) != str:
            for tarjeta in tarjetas:
                if tarjeta.AcumuladoPesos > 0:
                    acumuladopesos += tarjeta.AcumuladoPesos
                if tarjeta.AcumuladoDolares >0:
                    acumuladodolares += tarjeta.AcumuladoDolares
            if acumuladopesos <= 0 and acumuladodolares <= 0:
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
        numero = str(input())
        if re.fullmatch(r"[0-9]{8}",numero):
            numero = int(numero)
        elif not re.fullmatch(r"[a-zA-Z]{3}[0-9]{6}", numero):
            print("Ingrese el documento en el formato correcto")
            BuscarUsuarioDNI()
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
        ListarClientes()
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
    print("Elija Nivel Tarjeta:")
    print("1-Platinum")
    print("2-Gold")
    print("3-Plata")
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

def BuscarTitular(opcion = 1):
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
                          if opcion == 1:
                            ModificarLimite(modtarjeta[ind-1].numero)
                            print(f"La tarjeta {ListaTarjetas[ind-1]} Nro: {ListaTarjetas[ind-1].numero}")
                            print(f"Tiene ${ListaTarjetas[ind-1].limitePesos} de limite en Pesos")
                            print(f"y tiene ${ListaTarjetas[ind-1].limiteDolares} de limite en dolares")
                          else:
                              aux = ListaTarjetas[ind-1]
                              if EliminarTarjeta(modtarjeta[ind-1].numero):
                                    print(f"La tarjeta {aux} Nro: {aux.numero}")
                                    print(f"Ha sido desasociada de {aux.titular}")
                              else:
                                  print("La tarjeta seleccionada tiene deuda pendiente, no puede desasociarse en este momento.")
                          MenuTarjeta()
                      except:
                          print(f"Solo puede elegir entre {x-1} opciones")
                  else:
                    MenuTarjeta()
            else:
                print(usuarios)
                MenuTarjeta()
        elif respuesta == 2:
                  ListarClientes()
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
                          if opcion == 1:
                            ModificarLimite(modtarjeta[ind-1].numero)
                            print(f"La tarjeta {ListaTarjetas[ind-1]} Nro: {ListaTarjetas[ind-1].numero}")
                            print(f"Tiene ${ListaTarjetas[ind-1].limitePesos} de limite en Pesos")
                            print(f"y tiene ${ListaTarjetas[ind-1].limiteDolares} de limite en dolares")
                          else:
                              aux = ListaTarjetas[ind-1]
                              if EliminarTarjeta(modtarjeta[ind-1].numero):
                                    print(f"La tarjeta {aux} Nro: {aux.numero}")
                                    print(f"Ha sido desasociada de {aux.titular}")
                              else:
                                  print("La tarjeta seleccionada tiene deuda pendiente,\n\
                                   no puede desasociarse en este momento.")
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

def EncontrarTarjeta(numero):
    encontrada = "No existe Tarjeta con ese numero"
    for tarjeta in ListaTarjetas:
        if tarjeta.numero == numero:
            encontrada = tarjeta
    return encontrada

def ModificarLimite(numero):
    for tarjeta in ListaTarjetas:
        if tarjeta.numero == numero:
                print(f"Limite en Pesos: ${tarjeta.limitePesos}")
                print("Ingrese Nuevo Limite de Pesos:")
                print("(0 para no modificar)")
                pesos = float(input())
                print(f"Limite en Dolares: ${tarjeta.limiteDolares}")
                print("Ingrese Nuevo Limite de Dolares:")
                print("(0 para no modificar)")
                dolares = float(input())
                tarjeta.ModificarLimite(pesos, dolares)

def EliminarTarjeta(numero):
    for tarjeta in ListaTarjetas:
        if tarjeta.numero == numero:
            if tarjeta.AcumuladoPesos == 0 and tarjeta.AcumuladoDolares == 0:
                ListaTarjetas.pop(ListaTarjetas.index(tarjeta))
            else:
                return False

def BuscarDeuda (vertarjeta):
    deudapesos = 0
    deudadolares = 0
    for tarjeta in ListaTarjetas:
        if tarjeta.numero == vertarjeta.numero:
            deudapesos = tarjeta.DevolverSaldoPesos(tarjeta.AcumuladoPesos)
            deudadolares = tarjeta.DevolverSaldoDolares(tarjeta.AcumuladoDolares)
    return deudapesos, deudadolares

def BuscarDeudaTotal (usuario):
    deudatotalpesos = 0
    deudatotaldolares = 0
    for tarjeta in ListaTarjetas:
        if tarjeta.titular.numero == usuario.numero:
            deudatotalpesos += tarjeta.DevolverSaldoPesos(tarjeta.AcumuladoPesos)
            deudatotaldolares += tarjeta.DevolverSaldoDolares(tarjeta.AcumuladoDolares)
    return deudatotalpesos, deudatotaldolares

def ListarClientes():
    if ListaUsuarios:
        for clientes in ListaUsuarios:
            print(f"Nombre Y Apellido: {clientes}, {clientes.tipo}: {clientes.numero}")
        return True
    else:
        print("La lista de Clientes esta vacia de momento.")
        return False

def ListarTarjetas():
    if ListaTarjetas:
        for tarjetas in ListaTarjetas:
            print(f"Tarjeta {tarjetas} numero: {tarjetas.numero}")
            print(f"Titular: {tarjetas.titular}, {tarjetas.titular.tipo}: {tarjetas.titular.numero}")
            print(f"Limite en Pesos: {tarjetas.limitePesos}")
            print(f"Limite en Dolares: {tarjetas.limiteDolares}")
            print(f"Deuda en Pesos: {tarjetas.AcumuladoPesos}")
            print(f"Deuda en Dolares: {tarjetas.AcumuladoDolares}")
            print("\n")
        return True    
    else:
        print("No hay tarjetas asignadas de momento.")
        return False

def ListarConsigna():
    for clientes in ListaUsuarios:
        tarjetas = BuscarTarjeta(clientes)
        if type(tarjetas) != str:
            print("+----------------------------------+----------------------------------------+")
            print(f"|Nombre Y Apellido: {clientes}       | {clientes.tipo}: {clientes.numero}  |")
            print("+----------------------------------+----------------------------------------+")
            for tarjeta in tarjetas:
                print("+------------------------------------------------------+------------------------------------------------------------+")
                print("Numero               | Fecha de Otorgacion        | Fecha de Vencimiento     | Tipo      | Saldo $       | Saldo U$S ")
                print(f"{tarjeta.numero}         {tarjeta.fechaotorgacion}                  {tarjeta.fechavencimiento}                {tarjeta}              {tarjeta.AcumuladoPesos}             {tarjeta.AcumuladoDolares}")
                print("+------------------------------------------------------+------------------------------------------------------------+")
        else:
            pass

def OperarTarjeta(tarjeta):
    try:
        for operada in ListaTarjetas:
            if operada.numero == tarjeta.numero:
                operada.AcumuladoPesos = tarjeta.AcumuladoPesos
                operada.AcumuladoDolares = tarjeta.AcumuladoDolares
        return True
    except:
        return False

def PagarTarjetas():
    print("Por favor elija un item del menu:")
    print("1-Buscar por Nro de Tarjeta")
    print("2-Buscar por Usuario")
    print("3-Salir")
    try:
        menu4= int(input())
    except ValueError:
            PagarTarjetas()
    while menu4 <4:
        if menu4 == 1:
            if ListarTarjetas():
                try:
                    numero = str(input())
                    tarjeta = EncontrarTarjeta(numero)
                    if type(tarjeta) != str:
                        pesos, dolares = BuscarDeuda(tarjeta)
                        print(f"Tarjeta {tarjeta.numero} de {tarjeta.titular} adeuda:")
                        print(f"$ {pesos}")
                        print(f"u$S {dolares}\n")
                        print("Elija Saldo a Pagar?")
                        print("1-Deuda en Pesos")
                        print("2-Deuda en Dolares")
                        print("3-Salir")
                        try:
                            opcion = int(input())
                            while opcion < 4:
                                if opcion == 1:
                                    print("Ingrese Cantidad en Pesos:")
                                    cantidad = float(input())
                                    tarjeta.PagarSaldoPeso(cantidad)
                                    if OperarTarjeta(tarjeta):
                                        print("El pago se ha efectuado correctamente.")
                                    else:
                                        print("No ha podido realizarse el pago, intente nuevamente.")
                                    Operaciones()
                                    break
                                if opcion == 2:
                                    print("Ingrese Cantidad de Dolares:")
                                    cantidad = float(input())
                                    tarjeta.PagarSaldoDolar(cantidad)
                                    if OperarTarjeta(tarjeta):
                                        print("El pago se ha efectuado correctamente.")
                                    else:
                                        print("No ha podido realizarse el pago, intente nuevamente.")
                                    Operaciones()
                                    break
                                if opcion == 3:
                                    Operaciones()
                                else:
                                    PagarTarjetas()
                        except:
                            print("Solo puede elegir entre tres opciones.")
                    else:
                        print(tarjeta)
                        PagarTarjetas()
                except:
                    print("Solo ingrese numeros, sin espacios ni guiones")
                    PagarTarjetas()
                break
            else:
                PagarTarjetas()
        if menu4 == 2:
            if ListarClientes():
                try:
                  usuario = BuscarUsuarioDNI()
                  if type(usuario) != str:
                      modtarjeta = BuscarTarjeta(usuario)
                      x = 1
                      print("Elija una opcion de tarjeta de la lista:")
                      for tarjeta in modtarjeta:
                          print(f"{x}-{tarjeta} Nro:{tarjeta.numero}")
                          x += 1
                      ind = int(input())
                      pesos, dolares = BuscarDeuda(modtarjeta[ind-1])
                      print(f"Tarjeta {modtarjeta[ind-1]} de {modtarjeta[ind-1].titular} adeuda:")
                      print(f"$ {pesos}")
                      print(f"u$S {dolares}\n")
                      print("Elija Saldo a Pagar?")
                      print("1-Deuda en Pesos")
                      print("2-Deuda en Dolares")
                      print("3-Salir")
                      try:
                            opcion = int(input())
                            while opcion < 4:
                                if opcion == 1:
                                    print("Ingrese Cantidad en Pesos:")
                                    cantidad = float(input())
                                    ListaTarjetas[ind-1].PagarSaldoPeso(cantidad)
                                    if OperarTarjeta(tarjeta):
                                        print("El pago se ha efectuado correctamente.")
                                    else:
                                        print("No ha podido realizarse el pago, intente nuevamente.")
                                    Operaciones()
                                    break
                                if opcion == 2:
                                    print("Ingrese Cantidad de Dolares:")
                                    cantidad = float(input())
                                    ListaTarjetas[ind-1].PagarSaldoDolar(cantidad)
                                    if OperarTarjeta(tarjeta):
                                        print("El pago se ha efectuado correctamente.")
                                    else:
                                        print("No ha podido realizarse el pago, intente nuevamente.")
                                    Operaciones()
                                    break
                                if opcion == 3:
                                    Operaciones()
                                else:
                                    PagarTarjetas()
                      except:
                          print("Solo puede elegir entre tres opciones.")
                  else:
                       print(tarjeta)
                       PagarTarjetas()
                except:
                    print("Solo ingrese numeros, sin espacios ni guiones")
                    PagarTarjetas()
                break
        if menu4 == 3:
            Operaciones()
        else:
            PagarTarjetas()

def BuscarMoroso():
    if ListarClientes():
        try:
            Moroso = BuscarUsuarioDNI()
            if type(Moroso) != str:
                pesos, dolares = BuscarDeudaTotal(Moroso)
                print(f"{Moroso} tiene una deuda total de:")
                print(f"${pesos} en Pesos")
                print(f"${dolares} en Dolares\n")
            else:
                print(Moroso)
        except:
            print("Ingrese el DNI sin espacios, ni comas.")

def BuscarMorosoXTarjeta():
    if ListarClientes():
        try:
            Moroso = BuscarUsuarioDNI()
            if type(Moroso) != str:
                if ListaTarjetas:
                    for tarjeta in ListaTarjetas:
                        if tarjeta.titular.numero == Moroso.numero:
                            pesos, dolares = BuscarDeuda(tarjeta)
                            print(f"Tarjeta {tarjeta} a nombre de {Moroso} tiene una deuda total de:")
                            print(f"${pesos} en Pesos")
                            print(f"${dolares} en Dolares\n")
                        else:
                            print("El usuario no posee tarjeta activas.\n")
                else:
                    print("No hay tarjetas asociadas a ningun cliente.\n")
            else:
                print(Moroso)
        except:
            print("Ingrese el DNI sin espacios, ni comas.")

def DeclararConsumo(usuario):
     aux = usuario
     modtarjeta = BuscarTarjeta(usuario)
     if type(modtarjeta) != str:
        x = 1
        print("Elija una opcion de tarjeta de la lista:")
        for tarjeta in modtarjeta:
            print(f"{x}-{tarjeta} Nro:{tarjeta.numero}")
            x += 1
        try:
            ind = int(input())
            operartarjeta = modtarjeta[ind-1]
            print(f"Declarar Consumo en tarjeta{operartarjeta}")
            print("Elija moneda de la operacion:")
            print("1-Pesos")
            print("2-Dolares")
            moneda = int(input())
            if moneda == 1:
                print("Ingrese cantidad")
                cantidad = float(input())
                if operartarjeta.VerificarSaldoPeso(cantidad):
                    operartarjeta.ComprarPesos(cantidad)
                    if OperarTarjeta(operartarjeta):
                        print("La transaccion finalizo correctamente")
                        Operaciones()
                    else:
                        print("No se pudo completar la transaccion, intente nuevamente")
                        DeclararConsumo(aux)
                else:
                    print("Con esta compra superaria el limite de su tarjeta.")
                    Operaciones()
            elif moneda == 2:
                print("Ingrese cantidad")
                cantidad = float(input())
                if operartarjeta.VerificarSaldoDolar(cantidad):
                    operartarjeta.ComprarDolares(cantidad)
                    if OperarTarjeta(operartarjeta):
                        print("La transaccion finalizo correctamente")
                        Operaciones()
                    else:
                        print("No se pudo completar la transaccion, intente nuevamente")
                        DeclararConsumo(aux)
                else:
                    print("Con esta compra superaria el limite de su tarjeta.")
                    Operaciones()
            else:
                print("Solo puede elegir entre dos opciones de moneda")
                DeclararConsumo(aux)
        except:
            print("Elija una de las opciones disponibles sin comas ni puntos.")
            DeclararConsumo(aux)
     else:
         print("El cliente seleccionado no posee tarjetas activas. No puede declarar consumos.")
         Operaciones()
        
def ValidarDNI(tipo, numero):
    
    if tipo == TipoID.Pasaporte.name:
        validacion = re.compile(r"[a-zA-z]{3}[0-9]{6}")
    elif tipo == TipoID.DNI.name:
        validacion = re.compile(r"[0-9]{8}")
    else:
        return False

    if re.fullmatch(validacion, str(numero)):
        return True
    else:
        return False

def Hardcodear():
    
    persona = Usuario("DNI", 29682301, "Franco", "Villafane")
    ListaUsuarios.append(persona)
    persona = Usuario("DNI", 11924795, "Amelia", "Gomez")
    ListaUsuarios.append(persona)
    persona = Usuario("DNI", 29873848, "Marcos", "Moneta")
    ListaUsuarios.append(persona)
    persona = Usuario("DNI", 34989828, "Agostina", "Casella")
    ListaUsuarios.append(persona)
Hardcodear()
MenuPrincipal()
