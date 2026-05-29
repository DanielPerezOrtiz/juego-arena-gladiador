import random,json
class Personaje:
    def __init__(self, nombre, vida, defensa, ataque, suerte=0, pociones=0, dificultad= 1):
        self.nombre = nombre
        self.vida_max=vida
        self.vida_actual=vida
        self.defensa=defensa
        self.ataque=ataque
        self.suerte=suerte
        self.pociones=pociones
        self.dificultad = dificultad
        self.segunda_fase_activada = False
    def recibir_critico(self,daño_entrante):
        daño_critico = max (0,daño_entrante-(self.defensa*0.7))
        self.vida_actual-= daño_critico
        self.vida_actual= max(0,self.vida_actual)
        self.verificacion_de_transformacion()
        return daño_critico    
    def recibir_daño(self,daño_entrante):
        daño_real=max(0,daño_entrante-self.defensa)
        self.vida_actual-=daño_real
        self.vida_actual=max(0,self.vida_actual)
        self.verificacion_de_transformacion()
        return daño_real
    def verificacion_de_transformacion(self):
      if self.dificultad == 3 and not self.segunda_fase_activada and self.vida_actual<= (self.vida_max*0.1):
        self.segunda_fase_activada = True
        self.nombre = 'Demon Lord'
        self.ataque+=20
        self.defensa+=5
        self.vida_max+=50
        self.vida_actual=self.vida_max
        print ("\n"+"="*40)
        print ('!!!!!!El enemigo se ha transformado !!!!!!!')
        print (f'!!!!!!CUIDADO, HA NACIDO {self.nombre}, SUS ESTADISTICAS HAN AUMENTADO SIGNIFICATIVAMENTE !!!!!!!!  ')
        print ("="*40 + "\n") 
    def esta_vivo(self):
        if self.vida_actual >0:
            return True
        else:
            return False
    def curarse(self):
        if self.pociones >0:
            curacion=random.randint(15,40)        
            self.vida_actual=min(self.vida_max,self.vida_actual+curacion)
            self.pociones-=1
            print(f"{self.nombre} se ha curado {curacion} HP")
    def calcular_defensa (self):
        if self.defensa >7:
            self.defensa += 5
            print(f"Su defensa es de alto rango, suma un bono de puntos de defensa su defensa es {self.defensa} ")              
def pedir_datos(mensaje,minimo,maximo):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit() :
            valor = int (entrada)
            if minimo <= valor <= maximo :
                return valor
            else : 
                print (f"el valor debe estar entre {minimo} y {maximo}")
        else:
            print (f"el valor debe ser numerico nada de letras o signos")
def combate (gladiador,enemigo):
    while gladiador.esta_vivo() and enemigo.esta_vivo():
        print ("1. Atacar | 2. Sanarse ")
        opcion = pedir_datos('Que quiere hacer',1,2)
        if opcion == 1 :
            daño = random.randint(15,gladiador.ataque)
            probabilidad_esquivar_enemy = enemigo.suerte*6+5
            if random.randint (1,100)<=probabilidad_esquivar_enemy:
                print ('El enemigo ha esquivado su ataque y se burla')
            else:
                if daño>=40 :
                    enemigo.recibir_critico(daño)
                    print (f'{gladiador.nombre} ha realizado un ataque critico, la vida del enemigo es de {enemigo.vida_actual}') 
                else:
                    enemigo.recibir_daño(daño)
                    print (f'{gladiador.nombre} ha realizado un ataque, la vida del enemigo es {enemigo.vida_actual}')
        elif opcion == 2 :
            if gladiador.pociones >0 :
                gladiador.curarse()
                print (f"{gladiador.nombre} se ha curado, su vida actual es {gladiador.vida_actual} ")
            else :
                print ('no tiene mas pociones ')
        if enemigo.esta_vivo():
            if enemigo.vida_actual <= enemigo.vida_max*0.3 and enemigo.pociones>0:
                enemigo.curarse()
            probabilidad_esquivar = gladiador.suerte*6+5 
            if random.randint(1,100) <= probabilidad_esquivar:
                print (f" {gladiador.nombre} ha esquivado ")
            else :
                gladiador.recibir_daño(enemigo.ataque) 
                print (f'{enemigo.nombre} ha realizado un ataque, la vida del gladiador es de {gladiador.vida_actual}')           
def guardar_datos (gladiador):
    try:
        with open ('personajes.json','r') as f:
            personajes = json.load(f)
    except FileNotFoundError:
        personajes = {}
    personajes [gladiador.nombre] = {
        'vida_max': gladiador.vida_max,
        'vida_actual': gladiador.vida_actual,
        'defensa': gladiador.defensa,
        'ataque':gladiador.ataque,
        'suerte': gladiador.suerte,
        'pociones': gladiador.pociones
    }  
    with open ('personajes.json','w') as f:
        json.dump(personajes,f,indent=4)
        print(f"personaje {gladiador.nombre} guardado!!!")  
def cargar_personajes():     
    try:
        with open('personajes.json','r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}           
def nueva_partida():
          #gladiador
    nombre = input('su nombre es: ')
    vida = pedir_datos('Su vida es de (1/150) : ', 1, 150)
    ataque = pedir_datos('Con cuantos puntos de ataque cuenta usted (15/50): ',15,50)
    defensa = pedir_datos('Su defensa es de (1/10) :',1,10)
    suerte = pedir_datos('Su suerte es de (1/10) : ',1,10)
    pociones = pedir_datos('Trae consigo cuantas pociones (0/5): ',0,5)                      
    gladiador = Personaje(nombre,vida,defensa,ataque,suerte,pociones)                    
    #elegir dificultad 
    print('\nElija la dificultad:')
    print('1. facil')
    print ('2. dificil')
    print ('3. imposible')
        #sistema del enemigo
    dificultad = pedir_datos('Elija su dificultad: ',1,3)
    if dificultad==1:
            nombre_enemy = 'Duende'
            vida_enemy= 80
            defensa_enemy = 4
            ataque_enemy = 15
            suerte_enemy = 2
            pociones_enemy = 0
            dificultad = 1
    elif dificultad == 2:
            nombre_enemy = 'Orco'
            vida_enemy= 100
            defensa_enemy = 6
            ataque_enemy = 25
            suerte_enemy = 5
            pociones_enemy = 2
            dificultad = 2
    elif dificultad == 3:
            nombre_enemy = 'Demon'
            vida_enemy= 150
            defensa_enemy = 10
            ataque_enemy = 50
            suerte_enemy = 10
            pociones_enemy = 5
            dificultad = 3
    enemigo = Personaje(nombre_enemy,vida_enemy,defensa_enemy,ataque_enemy,suerte_enemy,pociones_enemy, dificultad)
    print (f"HA aparecido un {enemigo.nombre} ")
    gladiador.calcular_defensa()
    enemigo.calcular_defensa()
        #sistema de combate
    victoria = False    
    combate(gladiador,enemigo)    
    if not gladiador.esta_vivo() : 
                    print (f"{gladiador.nombre} esta muerto, game over")
    elif not enemigo.esta_vivo():
                    print (f"\n !HAS DERROTADO A {enemigo.nombre}")
                    victoria = True
    if gladiador.esta_vivo():
        opcion = input("guardar personaje (s/n): ")
        if opcion.lower()== "s":
            guardar_datos(gladiador)
                   
    with open ('Arena.txt','a') as archivo:
        if victoria == True:
            archivo.write (f"\n El gladiador entra en la arena y venció")
        else:
            archivo.write(f"\n El gladiador cayó en la arena")                                
def jugar():            
        while True:
            print(f"\n =================")
            print(f" Coliseo menu ")
            print (f"\n =================")
            print('1. Iniciar nueva partida')
            print('2. Cargar partida')
            print('3. Salir del juego')
            opcion_menu= pedir_datos('',1,3)
            if opcion_menu == 1:
                print (f"\n Bienvenido a nuestro coliseo")
                nueva_partida()
            elif opcion_menu == 2:
                personajes_dict = cargar_personajes()
                if not personajes_dict:
                    print('no hay partidas guardadas')
                else:
                    print('\n ----Personajes guardados -----')
                    lista = list(personajes_dict.keys())
                    for i, nombre in enumerate(lista,1):
                        datos = personajes_dict[nombre]
                        print(f"{i}. {nombre}(vida:{datos['vida_actual']}/{datos['vida_max']})")
                    seleccion = pedir_datos("\nSeleccione un personaje (0 para volver)",0, len(lista))
                    if seleccion > 0:
                        datos = personajes_dict[lista[seleccion-1]]
                        gladiador = Personaje(
                            lista[seleccion-1],
                            datos['vida_max'],
                            datos['defensa'],
                            datos['ataque'],
                            datos['suerte'],
                            datos['pociones']
                        )
                        gladiador.vida_actual = datos['vida_actual']
                        print (f"\nCargando a {gladiador.nombre}....")
                        print ('\n Elija dificultad :')
                        print ('1. Facil')
                        print ('2. Dificil')
                        print ('3. Imposible')
                        dificultad = pedir_datos('Elija la dificultad:',1,3)
                        if dificultad==1:
                            nombre_enemy = 'Duende'
                            vida_enemy= 80
                            defensa_enemy = 4
                            ataque_enemy = 15
                            suerte_enemy = 2
                            pociones_enemy = 0
                            dificultad = 1
                        elif dificultad == 2:
                            nombre_enemy = 'Orco'
                            vida_enemy= 100
                            defensa_enemy = 6
                            ataque_enemy = 25
                            suerte_enemy = 5
                            pociones_enemy = 2
                            dificultad = 2
                        elif dificultad == 3:
                            nombre_enemy = 'Demon'
                            vida_enemy= 150
                            defensa_enemy = 10
                            ataque_enemy = 50
                            suerte_enemy = 10
                            pociones_enemy = 5
                            dificultad = 3
                        enemigo = Personaje(nombre_enemy,vida_enemy,defensa_enemy,ataque_enemy,suerte_enemy,pociones_enemy, dificultad)
                        print (f"HA aparecido un {enemigo.nombre} ")
                        gladiador.calcular_defensa()
                        enemigo.calcular_defensa()
                        #sitema de combate
                        combate(gladiador,enemigo)
                        victoria = False
                        if not gladiador.esta_vivo() : 
                                    print (f"{gladiador.nombre} esta muerto, game over")
                        elif not enemigo.esta_vivo():
                                    print (f"\n !HAS DERROTADO A {enemigo.nombre}")
                                    victoria = True
                        if gladiador.esta_vivo():
                          opcion = input("guardar personaje(s/n): ")
                          if opcion.lower()== "s":
                            guardar_datos(gladiador) 
                        with open ('Arena.txt','a') as archivo:
                         if victoria == True:
                            archivo.write (f"\n El gladiador entra en la arena y vencio")
                         else:
                            archivo.write(f"\n El gladiador cayo en la arena")
            elif opcion_menu == 3 :
                print (f"\n gracias por jugar")
                break              
if __name__ =="__main__":        
    jugar()                                          