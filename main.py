#from locale import ABDAY_5
import numpy as np
import constants as c
import utils as u

#El número de barcos del usuario tocados
nb_us_tocados = 0

#El número de barcos de la máquina tocados 
nb_op_tocados = 0

#TO DO: necesitamos algo que traduzca el numero de 'x' en nuestro tablero a barcos
#TO Do: ir guardando las coordenadas para que no se puedan volver a decir
#Que la maquina no pueda disparar al mismo sitio
#colocar el barco


print("""\nBienvenido al juego de hundir la flota!!

Las normas son las siguientes:
- Puedes colocar los barcos en el tablero o elegir que se coloquen aleatoriamente
- Introduce las coordenadas para disparar al tablero de tu oponente1
- Si aciertas y disparas a un barco, tendrás otro turno, si no, será el turno de la máquina
- Gana el que consiga hundir todos los barcos de su oponente

Buena suerte!
""")

#Inicializamos los 3 tableros
tablero_us_barcos = u.Tablero('01') #Barcos del usuario y disparos del oponente
tablero_us_disparos = u.Tablero('02', tablero = np.full((u.Tablero.N, u.Tablero.N,), " ")) #Disparos del usuario
tablero_op_barcos = u.Tablero('03', tablero = np.full((u.Tablero.N, u.Tablero.N), " ")) #Barcos del oponente

ini_tablero = int(input("""Selecciona una opción para crear el tablero: 
0 - Montar tu tablero 
1 - Tablero aleatorio
: """))

if ini_tablero == 0:
    tablero_us_barcos.inicializar_tablero()
else:
    tablero_us_barcos.tablero_random()

#El tablero de la máquina se hace de manera aleatoria
tablero_op_barcos.tablero_random()


oponente_tocado = True
usuario_tocado = True
turno_usuario = True

while nb_us_tocados < c.NX_US and nb_op_tocados < c.NX_OP:
    
    while turno_usuario == True: #tengo otro turno mientras consiga darle a un barco 

        print("\nTablero con tus barcos:")
        tablero_us_barcos.tablero_mostrado()
        print("\nTus disparos efectuados:") 
        tablero_us_disparos.tablero_mostrado()

        check_input_coord = False
        while check_input_coord == False:
            coordenadas = input("\nIntroduce las coordenadas donde quieres disparar (por ejemplo, A1):")
            coordenadas = coordenadas.upper()
            if coordenadas not in c.coors_tab:
                check_input_coord = False
                print("\nNo es una coordenada válida")
            else:
                check_input_coord = True
        
        #Me devuelve un True o False en función de si he tocado barco o no
        oponente_tocado = tablero_op_barcos.disparo(coordenadas) 
        tablero_us_disparos.disparos_efectuados(coordenadas, oponente_tocado)

        if oponente_tocado == True and nb_op_tocados < c.NX_OP:
            print("\nOponente tocado!")
            tablero_us_disparos.tablero_mostrado()
            nb_op_tocados += 1
            if oponente_tocado == True and nb_op_tocados == c.NX_OP:
                print("\nHas ganado! Has hundido todos los barcos del oponente")
                break
        elif oponente_tocado == False:
            print("\nNo le has dado!\n")
            tablero_us_disparos.tablero_mostrado()
            turno_usuario = False
            
    
    while turno_usuario != True:
        
        usuario_tocado = tablero_us_barcos.disparo(np.random.randint(0,10,size=2)) #dispara la maquina a esta coordenada que me he inventado

        if usuario_tocado == True and nb_us_tocados < c.NX_US:
            print("\nEs el turno de tu oponente")
            tablero_us_barcos.tablero_mostrado()
            print("\nHa tocado tu barco!")
            nb_us_tocados += 1
            if usuario_tocado == True and nb_us_tocados == c.NX_US:
                tablero_us_barcos.tablero_mostrado()
                print("\nHas perdido! Tu oponente ha derribado todos tus barcos!")
                break
        elif usuario_tocado == False:
            print("\nEs el turno de tu oponente")
            tablero_us_barcos.tablero_mostrado()
            print("\nHa fallado, es tu turno!\n")
            turno_usuario = True
         