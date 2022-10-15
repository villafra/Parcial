from enum import Enum
from datetime import timedelta


class Usuario:
    def __init__(self, tipo, numero, nombre, apellido):
        self.tipo = tipo
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
    def __str__(self):
        return f"{self.nombre} {self.apellido}" 

class Tarjeta:
    def __init__(self, fechaotorga, titular):
        self.fechaotorgacion = fechaotorga
        self.titular = titular
        self.SetFechaVenc()
    def Setnumero(self, numero):
        return len(str(numero))==12
    def SetFechaVenc(self):
        self.fechavencimiento =  self.fechaotorgacion +  timedelta(1825)
    def ComprarPesos(self, cantidad):
        self.AcumuladoPesos += cantidad
    def ComprarDolares(self, cantidad):
        self.AcumuladoDolares += cantidad
    def PagarSaldoPeso(self, cantidad):
        self.AcumuladoPesos -= cantidad
    def PagarSaldoDolar(self, cantidad):
        self.AcumuladoDolares -= cantidad
    def VerificarSaldoPeso(self, cantidad):
        return self.AcumuladoPesos + cantidad <= self.limitePesos
    def VerificarSaldoDolar(self, cantidad):
        return self.AcumuladoDolares + cantidad <= self.limiteDolares

    numero = 0
    AcumuladoPesos = 0
    AcumuladoDolares = 0
    limitePesos = 0
    limiteDolares = 0
    

    

class Platinum(Tarjeta):
    def __init__(self, fechaotorga, titular):
        super().__init__(fechaotorga, titular)
        self.SetLimites()
        
    def Setnumero(self,numero):
        if Tarjeta.Setnumero(self,numero):
            self.numero = "9999" + str(numero)
    def SetLimites(self):
        self.limitePesos = 1000000
        self.limiteDolares = 10000

class Gold(Tarjeta):
    def __init__(self, fechaotorga, titular):
        super().__init__(fechaotorga, titular)
        self.SetLimites()
    def Setnumero(self, numero):
        Tarjeta.Setnumero(self,numero)
        self.numero = "8888" + str(numero)
    def SetLimites(self):
        self.limitePesos = 750000
        self.limiteDolares = 7500

class Plata(Tarjeta):
    def __init__(self, fechaotorga, titular):
        super().__init__(fechaotorga, titular)
        self.SetLimites()
    def Setnumero(self, numero):
        Tarjeta.Setnumero(self,numero)
        self.numero = "7777" + str(numero)
    def SetLimites(self):
        self.limitePesos = 500000
        self.limiteDolares = 5000

class TipoID(Enum):
    DNI = 1
    Pasaporte = 2

class TipoTarjeta(Enum):
    Platinum = 1
    Gold = 2
    Plata = 3