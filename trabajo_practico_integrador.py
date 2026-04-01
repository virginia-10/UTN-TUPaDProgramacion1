#Ejercicio 1 "Caja del kiosco"

print("\nCaja del Kiosco")

nombre = input("Cliente: ").strip()

while nombre == "" or not nombre.isalpha():
     print("Error: Ingresa un nombre no vacio y solo con letras")
     nombre = input("Cliente: ").strip()

cantidad_str = input("Ingresa la cantidad de productos: ").strip()

while not cantidad_str.isdigit() or int(cantidad_str) == 0:
    print("Error: Ingresa un numero entero positivo y difrente a 0")
    cantidad_str = input("Ingresa la cantidad de productos: ").strip()

cantidad_int = int(cantidad_str)
total_sin_descuento = 0
total_con_descuento = 0

for i in range(1,cantidad_int+1):
    precio_str = input(f"Producto {i} = Precio: ").strip()

    while not precio_str.isdigit() or int(precio_str) == 0:
        print("Error: el precio debe ser un numero entero positivo.")
        precio_str = input(f"Producto {i} = Precio: ").strip()

    precio_int = int(precio_str)

    descuento = input("Descuento S/N: ").strip().lower()
    
    while descuento != "s" and descuento != "n":
        print("Error ingresar S para si o N para no.")
        descuento = input("Descuento s/n: ").strip().lower()
    
    total_sin_descuento += precio_int

    if descuento == "s":
        precio_final = precio_int * 0.9
    else:
        precio_final = precio_int
    
    total_con_descuento += precio_final

ahorro_total = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_int

print()
print(f"Total sin descuento: ${total_sin_descuento: .2f}")
print(f"Total con descuento: $ {total_con_descuento: .2f}")
print(f"Ahorro total: $ {ahorro_total: .2f}")
print(f"Promedio: $ {promedio: .2f}")

print("///////")

#Ejercicio 2 “Acceso al Campus y Menú Seguro” 

print("\nIngreso al Campus")

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
max_intentos = 3


while intentos < max_intentos:
    usuario = input("Ingrese usuario: ")
    clave = input("Ingrese clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Login exitoso")
        break
    else:
        intentos += 1
        print(f"Datos incorrectos. Intento {intentos} de {max_intentos}\n")


if intentos == max_intentos:
    print("Cuenta bloqueada")
else:

    while True:
        print("\nMENÚ:")
        print("1. Ver estado de inscripción")
        print("2. Cambiar clave")
        print("3. Mensaje motivacional")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if not opcion.isdigit():
            print("Error: Debe ingresar un número")
            continue

        opcion = int(opcion)

        if opcion < 1 or opcion > 4:
            print("Error: Opción fuera de rango")
            continue

        if opcion == 1:
            print("Estado: Inscripto")

        elif opcion == 2:
            nueva_clave = input("Ingrese nueva clave: ")
            confirmar_clave = input("Confirme nueva clave: ")

            if len(nueva_clave) < 6:
                print("Error: La clave debe tener al menos 6 caracteres")
                continue


            if nueva_clave != confirmar_clave:
                print("Error: Las claves no coinciden")
            else:
                clave_correcta = nueva_clave
                print("Clave cambiada correctamente")

        elif opcion == 3:
            print("No te preocupes por el ritmo de los demás; la carrera que importa es la que corres contra tus propios límites\n")

        elif opcion == 4:
            print("Salir")
            break

print("///////")

#Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

print("\nAgenda de turnos")

lunes1 = lunes2 = lunes3 = lunes4 = ""

martes_1 = martes_2 = martes_3 = ""

nombre = input("\nNombre del Operador: ").strip()

while nombre == "" or not nombre.isalpha():
     print("Error: Ingresa un nombre no vacio y solo con letras")
     nombre = input("Nombre del Operador: ").strip()

print(f"\nBienvenido {nombre} !".title())

while True:
    print("\nMENÚ:")
    print("1. Reservar turno.")
    print("2. Cancelar turno.")
    print("3. Ver agenda del dia.")
    print("4. Ver resumen general")
    print("5. Cerrar sistema.")

    opcion = input("Seleccione una opción: ")

    if not opcion.isdigit():
        print("Error: Debe ingresar un número")
        opcion = input("Seleccione una opción: ")

    opcion = int(opcion)

    if opcion < 1 or opcion > 5:
            print("Error: Opción fuera de rango")
            opcion = input("Seleccione una opción: ")
    
    if opcion == 1:
        print("Reservar turno.")
        dia = input("1 = Lunes o 2 = Martes: ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) >2:
            print("Error ingrese opcion 1 o 2")
            dia = input("1 = Lunes o 2 = Martes: ")    
        dia = int(dia)
    
        paciente = input("Ingrese su nombre: ").strip()
        if not paciente.isalpha():
                print("Error: el nombre solo puede contener letras.")
                paciente = input("Ingrese su nombre: ").strip()

        if dia == 1:
         if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
            print(f"Error {paciente} ya tiene turno asigando ese dia. ")
            continue
         elif lunes1 == "":
                lunes1 = paciente
                print(f"Turno reservado: Lunes - Turno 1 para {paciente}.")      
         elif lunes2 == "":
                lunes2 = paciente
                print(f"Turno reservado: Lunes - Turno 2 para {paciente}.")
         elif lunes3 == "":
                lunes3 = paciente
                print(f"Turno reservado: Lunes - Turno 3 para {paciente}.")
         elif lunes4 == "":
                lunes4 = paciente
                print(f"Turno reservado: Lunes - Turno 4 para {paciente}.")
         else:
            print("No hay mas turnos disponibles.")
    
        if dia == 2:
         if paciente == martes_1 or paciente == martes_2 or paciente == martes_3:
          print(f"Error {paciente} ya tiene turno asigando ese dia. ")     
         elif martes_1 == "":
                martes_1 = paciente
                print(f"Turno reservado: Martes - Turno 1 para {paciente}.")      
         elif martes_2 == "":
                martes_2 = paciente
                print(f"Turno reservado: Martes - Turno 2 para {paciente}.")
         elif martes_3 == "":
                martes_3 = paciente
                print(f"Turno reservado: Martes - Turno 3 para {paciente}.")
    
    if opcion == 2:
         print("Cancelar turno.")
         dia = input("1 = Lunes o 2 = Martes: ")
         while not dia.isdigit() or int(dia) < 1 or int(dia) >2:
          dia = input("1 = Lunes o 2 = Martes: ")    
         dia = int(dia)

         paciente = input("Ingrese su nombre: ")
         if not paciente.isalpha():
                print("Error: el nombre solo puede contener letras.")
                paciente = input("Ingrese su nombre: ")
        
         cancelado = False
         if dia == 1:
            if lunes1 == paciente:
                lunes1 = ""
                cancelado = True
            elif lunes2 == paciente:
              lunes2 = ""
              cancelado = True
            elif lunes3 == paciente:
                lunes3 = ""
                cancelado = True
            elif lunes4 == paciente:
              lunes4 = ""
              cancelado = True
         else:
              if martes_1 == paciente:
                   martes_1 = ""
                   cancelado = True
              elif martes_2 == paciente:
                   martes_2 = ""
                   cancelado = True
              elif martes_3 == paciente:
                   martes_3 = ""
                   cancelado = True
              
            
            
         if cancelado:
            print(f"Turno de {paciente} cancelado.")
         else:
            print(f"No se encontró turno para {paciente} en ese día.")


    elif opcion == 3:
        print("Ver agenda del dia.")
        dia = input("1 = Lunes o 2 = Martes: ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) >2:
          dia = input("1 = Lunes o 2 = Martes: ")    
        dia = int(dia)

        if dia == 1:
            if lunes1 == "":
             print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {lunes1}")
            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {lunes2}")
            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {lunes3}")
            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print(f"Turno 4: {lunes4}")
        if dia == 2:
            if martes_1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {martes_1}")
            if martes_2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {martes_2}")
            if martes_3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {martes_3}")

    elif opcion == 4:
        print("Ver resumen general.")
    
        ocupados_lunes = 0
        libres_lunes = 0

        if lunes1 == "":
            libres_lunes += 1
        else:
            ocupados_lunes += 1
        if lunes2 == "":
            libres_lunes +=1
        else:
            ocupados_lunes += 1
        if lunes3 == "":
            libres_lunes += 1
        else:
            ocupados_lunes += 1
        if lunes4 == "":
            libres_lunes +=1
        else:
            ocupados_lunes += 1
       
        ocupados_martes = 0
        libres_martes = 0

        if martes_1 == "":
            libres_martes += 1
        else:
            ocupados_martes += 1
        if martes_2 == "":
            libres_martes +=1
        else:
            ocupados_martes += 1
        if martes_3 == "":
            libres_martes += 1
        else:
            ocupados_martes += 1
        
        print(f"Lunes: Libres: {libres_lunes} / Ocupados: {ocupados_lunes}")
        print(f"Martes: Libres: {libres_martes} / Ocupados: {ocupados_martes}")

        if ocupados_lunes > ocupados_martes:
            print("Dia con mas turnos: Lunes")
        elif ocupados_martes >ocupados_lunes:
            print("Dia con mas turnos: Martes")
        else:
            print("Ambos dias con la misma cantidad de turnos.")
        
    elif opcion == 5:
        print("Cerrar sistema")
        break

print("///////")

#Ejercicio 4 — “Escape Room: La Bóveda”
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
contador_forzar_seguido = 0

print("\nESCAPE ROOM: LA BOVEDA")

nombre = input("\nNombre del agente: ").strip()

while nombre == "" or not nombre.isalpha():
     print("Error: Ingresa un nombre no vacio y solo con letras")
     nombre = input("Cliente: ").strip()

print(f"\nBienvenido Agente {nombre} ! que comience el juego...".title())

while energia >0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:

    if alarma and tiempo <= 3:
         print("Sistema bloqueado por la alarma")
         break
    
    print(f"\n=Estado=")
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}")
    

    print("\nMENÚ:")
    print("1. Forzar cerradura.")
    print("2. Hackear panel.")
    print("3. Descansar.")

    opcion = input("Seleccione una opción: ")

    if not opcion.isdigit():
        print("Error: Debe ingresar un número")
        opcion = input("Seleccione una opción: ")

    opcion = int(opcion)

    if opcion < 1 or opcion > 3:
            print("Error: Opción fuera de rango")
            opcion = input("Seleccione una opción: ")

    if opcion == 1:
         print("Forzar cerradura")
         contador_forzar_seguido += 1
         energia -= 20
         tiempo -= 2
         
         if energia < 40:
            numero = input("Riesgo de alarma. Elegir un numero del 1 al 3.")
            while not numero.isdigit() or int(numero) < 1 or int(numero) > 3:
                print("Numero invalido")
                numero = input("Ingresar un numero del 1 al 3.")
     
            if numero == 3:
                alarma = True
                print("Alarma activada.")
    
         if contador_forzar_seguido == 3:
              print("Alarma forzaste la cerradura 3 veces. ")
              print("La cerradura se trabo")
              alarma = True
              contador_forzar_seguido = 0
              break
         else:
           if not alarma:
                cerraduras_abiertas += 1
                print("Abriste cerradura.")
           else:
                print("Se activo alarma. No se puede abrir.")
         
    elif opcion == 2:
         print("Hackear panel.")
         energia -= 10
         tiempo -= 3

         for paso in range(1,5):
              codigo_parcial += "B"
              print(f"Progreso: {paso}/4 , Codigo parcial: {codigo_parcial}")
              
              if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                   cerraduras_abiertas += 1
                   print("Se abre cerradura.")
                   codigo_parcial = ""

    elif opcion == 3:
         print("Descansar.")
         energia += 15
         if energia >100:
              energia = 100
              print("Energia recuperada.")
         
         tiempo -= 1
         
         if alarma:
              energia -= 10
              print("Se te esta agotando la energia") 
         print("Descansa") 
    
    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        print("Sistema bloqueado.")
        break

print("=RESULTADO=")
if cerraduras_abiertas == 3:
     print("VICTORIA")
elif energia <= 0 or tiempo <= 0:
     print("DERROTA")
else: 
    print("DERROTA. Bloqueado por alarma.")

print("///////")

#Ejercicio 5 — “Escape Room:"La Arena del Gladiador"

print("\n= La Arena del Gladiador =")

nombre = input("\nNombre del Gladiador: ").strip().title()

while nombre == "" or not nombre.isalpha() or nombre.isdigit():
     print("Error: solo se permiten letras.")
     nombre = input("Nombre del Gladiador: ").strip().title()
    
print(f"\nAdelante Gladiador {nombre}!\n")

vida_del_gladiador = 100
vida_del_enemigo = 100
pociones_de_vida = 3
daño_ataque_pesado = 15
daño_base_enemigo = 12
turno_gladiador = True

while vida_del_gladiador >0 and vida_del_enemigo >0:
      
    print(f"{nombre}: HP: {vida_del_gladiador} vs Enemigo: HP: {vida_del_enemigo}, Pociones restantes: {pociones_de_vida}\n")

    print("Elegir una opcion del Menú: ")
    print("1. Ataque Pesado")
    print("2. Rafaga Veloz")
    print("3. Curar")

    opcion = input("Seleccione una opción: ")

    if not opcion.isdigit():
        print("Error: Debe ingresar un número")
        opcion = input("Seleccione una opción: ")

    opcion = int(opcion)

    if opcion < 1 or opcion > 3:
            print("Error: Opción fuera de rango")
            opcion = input("Seleccione una opción: ")

    if opcion == 1:
        daño_final = daño_ataque_pesado
        if vida_del_enemigo < 20:
            daño_total = float(daño_base_enemigo) * 1.5
            print(f"= Golpe critico = resultado:  {daño_total}")

            vida_del_enemigo -= daño_total
            print(f"Atacaste al enemigo por {daño_final} puntos de daño!.")

    elif opcion == 2:
        print("Inicias una rafaga de golpes!.")
        for i in range(1,4):
           vida_del_enemigo -= 5
           print(f"> Golpe conectado por 5 de daño <.") 
    
    elif opcion == 3:
         print("Cura")
         if pociones_de_vida >0:
              vida_del_gladiador += 30
              pociones_de_vida -= 1
         else:
              print("¡¡No quedan mas pociones!! Pierdes tu turno.")

    if vida_del_enemigo >0:
        vida_del_gladiador -= daño_base_enemigo
        print(f"El enemigo te ataco por {daño_base_enemigo} puntos.")
       
print("FIN DE LA BATALLA\n")     
if vida_del_gladiador > 0:
    print(f"VICTORIA!! {nombre} ha ganado la batalla.")
     
else:
    print(f"DERROTA. Has caido en combate.")