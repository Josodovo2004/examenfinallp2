import json
import uuid

class Persona():
    def __init__(self, nombre, apellido, dni, email) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email

    def registrar_persona(self):
        with open("database.json", "r+") as file:
            data = json.load(file)
            person = {"nombre": self.nombre, "apellido": self.apellido, "dni" : self.dni, "email": self.email}
            data["personas"].append(person)
            file.seek(0)
            json.dump(data, file, indent=2)
            file.truncate()

class Comprador(Persona):
    def __init__(self, nombre, apellido, dni, email) -> None:
        super().__init__(nombre, apellido, dni, email)

class Organizador(Persona):
    def __init__(self, nombre, apellido, dni, email, password) -> None:
        super().__init__(nombre, apellido, dni, email)        
        self.password = password

    def registrar_persona(self):
        with open("database.json", "r+") as file:
            data = json.load(file)
            person = {"nombre": self.nombre, "apellido": self.apellido, "dni" : self.dni, "email": self.email, "password" : self.password}
            data["personas"].append(person)
            file.seek(0)
            json.dump(data, file, indent=2)
            file.truncate()


class Evento():
    def __init__(self,nombre ,fecha, precioBoleto, esVIP: bool, dniOrganizador, descuento: bool, capacidad) -> None:
        self.nombre = nombre
        self.fecha = fecha
        self.precioBoleto = precioBoleto
        self.esVIP = esVIP
        self.dniOrganizador = dniOrganizador
        self.descuento = descuento
        self.capacidad = capacidad

    def registro_evento(self):
        with open("database.json", "r+") as file:
            data = json.load(file)
            event = {"id": str(uuid.uuid4()),"nombre": self.nombre, "fecha": self.fecha, "precioBoleto" : self.precioBoleto, "esVIP": self.esVIP, "dniOrganizador": self.dniOrganizador, "descuento": self.descuento, 'capacidad': self.capacidad}
            data["eventos"].append(event)
            file.seek(0)
            json.dump(data, file, indent=2)
            file.truncate()

    def mostrar_detalle(self):
        print(f'nombre: {self.nombre}, fecha: {self.fecha}, precioBoleto:{self.precioBoleto}')

class EventoParrillada(Evento):
    def __init__(self, nombre, fecha, precioBoleto, esVIP: bool, dniOrganizador, descuento: bool, capacidad) -> None:
        super().__init__(self,nombre ,fecha, precioBoleto, esVIP, dniOrganizador, descuento, capacidad)

class EventoVIP(Evento):
    def __init__(self, nombre, fecha, precioBoleto, esVIP: bool, dniOrganizador, descuento: bool, capacidad, beneficios) -> None:
        super().__init__(self,nombre ,fecha, precioBoleto, esVIP, dniOrganizador, descuento, capacidad)
        self.beneficios = beneficios

    def registro_evento(self):
        with open("database.json", "r+") as file:
            data = json.load(file)
            event = {"id": str(uuid.uuid4()),"nombre": self.nombre, "fecha": self.fecha, "precioBoleto" : self.precioBoleto, "esVIP": self.esVIP, "dniOrganizador": self.dniOrganizador, "descuento": self.descuento, 'capacidad': self.capacidad, 'beneficios': self.beneficios}
            data["eventos"].append(event)
            file.seek(0)
            json.dump(data, file, indent=2)
            file.truncate()

    def mostrar_detalle(self):
        print(f'nombre: {self.nombre}, fecha: {self.fecha}, precioBoleto:{self.precioBoleto}, beneficios:{self.beneficios}')

class Venta():
    def __init__(self, dniComprador, idEvento, cantidadBoletos) -> None:
        self.dniComprador = dniComprador
        self.idEvento = idEvento
        self.cantidadBoletos = cantidadBoletos

    def venta_boletos(self):
        with open('database.json', 'r+') as file:
            data = json.load(file)

            for value in data['eventos']:
                if value['id'] == self.idEvento:
                    evento = value
            entradasYaVendidas = 0
            if evento:
                for value in data["ventas"]:
                    if value['idEvento'] == self.idEvento:
                        entradasYaVendidas += value['cantidadBoletos']

                if entradasYaVendidas + self.cantidadBoletos > evento['capacidad']:
                    print('No se pueden comprar tantos bolestos')
                    print(f"Solo quedan {value['capaciadad'] - entradasYaVendidas} boletos disponibles")
                else:
                    event = {"id": 'Bol' + str(uuid.uuid4()), 'dniComprador': self.dniComprador, 'idEvento': self.idEvento, 'cantidadBoletos': self.cantidadBoletos}
                    data['ventas'].append(event)
                    file.seek(0)
                    json.dump(data, file, indent=2)
                    file.truncate()
            else:
                print('No existe ese evento')