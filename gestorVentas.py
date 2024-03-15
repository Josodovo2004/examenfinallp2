from clases import *

class GestorVentas():
    def menuBucle(self):
        while True:
            eleccion = input(''''Bienvenido al gestor de eventos que deseas realizar:
                1)Registrar Compradores o Organizadores
                2)Crear Eventos
                3)Registrar Ventas de Boletos
                4)Salir''')
            
            if eleccion == '1':
                self.regstro_personas()
            elif eleccion == '2':
                self.creacion_eventos()
            elif eleccion == '3':
                self.registrar_ventas()
            elif eleccion == '4':
                break
            else:
                print('Eleccion no valida')
        
    def creacion_eventos():
        password = input('Ingrese su password de Organizador')

        with open('database.json', 'r+') as file:
            data = json.load(file)

            for value in data['personas']:
                if len(value) > 4:
                    if value['password'] == password:
                        organizador = Organizador(value['nombre'], value['apellido'], value['dni'], value['email'], value['password'])

                        eleccion = input(f'''BIENVENIDO {organizador.nombre} {organizador.apellido}, que clase de evento quiere registrar: 
                                         1)Evento Normal
                                         2)Evento VIP''')
                        
                        if eleccion == '1':
                            nombre = input('Nombre: ')
                            fecha = input('Fecha: ')
                            precioBoleto = int(input(precioBoleto))
                            esVIP = False
                            descuento = int(input('Porcentaje de descuento por mas de 5 boletos en 1 sola compara: '))
                            capacidad = int(input('Capacidad del Evento: '))

                            evento = EventoParrillada(nombre, fecha, precioBoleto, esVIP, organizador.dni, descuento, capacidad)
                            evento.registro_evento()

                            print('Evento Registrado con exito')
                        elif eleccion == '2':
                            nombre = input('Nombre: ')
                            fecha = input('Fecha: ')
                            precioBoleto = int(input(precioBoleto))
                            esVIP = False
                            descuento = int(input('Porcentaje de descuento por mas de 5 boletos en 1 sola compara: '))
                            capacidad = int(input('Capacidad del Evento: '))
                            beneficios = input('Beneficios del evento: ')

                            evento = EventoVIP(nombre, fecha, precioBoleto, esVIP, organizador.dni, descuento, capacidad, beneficios)
                            evento.registro_evento()

                            print('Evento Registrado con exito')

                        else:
                            print('opcion no valida')
                        
    def registrar_ventas():
        dniComprador = input('Ingrese el dni del comprador')

        with open('database.json', 'r+') as file:

            data = json.load(file)

            for value in data['personas']:
                if value['dni'] == dniComprador:
                    comprador = Comprador(value['nombre'],value['apellido'],value['dni'],value['email'])

            for value in data['eventos']:
                print(f"id: {value['id']},Evento: {value['nombre']}, es VIP: {value['esVIP']}")

        idEvento = input('Ingrese el id del evento del cual desea comprar: ')

        cantidad = int(input('Cuantas entradas desea comprar: '))

        venta = Venta(dniComprador, idEvento, cantidad)
        venta.venta_boletos()

    def regstro_personas():
        eleccion = int(input('''Que desea hacer:
                         1)Registrar un Organizador
                         2)Registrar un Comprador'''))
        
        if eleccion == 1:
            nombre = input('Nombre: ')
            apellido = input('apellido: ')
            dni = input('dni: ')
            email = input(email)

            comprador = Comprador(nombre, apellido, dni, email)
            comprador.registrar_persona()
        elif eleccion == 2:
            nombre = input('Nombre: ')
            apellido = input('apellido: ')
            dni = input('dni: ')
            email = input('email: ')
            password = input('password: ')

            organizador = Organizador(nombre, apellido, dni, email, password)
            organizador.registrar_persona()

        else:
            print('Eleccion no valida')


app = GestorVentas()

app.menuBucle()