from itertools import count
from tkinter import N
import numpy as np
import random
import constants as c

class Tablero:
    N = 10 #tamaño tablero
    mar = ' '
    barc = 'O'
    tocado = 'X'
    mar_t = '#'
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, id_usuario, dimensiones_tablero = (10,10), barcos = {'pequeño':1, 'mediano':2, 'grande':3, 'enorme':4}, tablero = np.full((N,N), " "), num_barcos = [4, 3, 2, 1]):
        self.id = id_usuario
        self.dim = dimensiones_tablero
        self.barco = barcos
        self.tablero = tablero
        self.num_barcos = num_barcos


    def hay_barco_ahi(self, tipo_barco, coordenadas, orientacion):
        habia_barco = False
        
        for i in range(self.barco[tipo_barco]):
            try:
                if orientacion == "N":
                    if self.tablero[coordenadas[0]-i][coordenadas[1]] != ' ':
                        habia_barco = True
                        
                elif orientacion == "S":  
                    if self.tablero[coordenadas[0]+i][coordenadas[1]] != ' ': 
                        habia_barco = True
                        
                elif orientacion == "E":
                    if self.tablero[coordenadas[0]][coordenadas[1]+i]!= ' ':
                        habia_barco = True
                
                elif orientacion == "O":
                    if self.tablero[coordenadas[0]][coordenadas[1]-i] != ' ':
                        habia_barco = True
            except:
                habia_barco = False
            
        return habia_barco



    def colocar_barco(self, tipo_barco, coordenadas, orientacion):
        
        for i in range(self.barco[tipo_barco]):

            if orientacion == "N":
                self.tablero[coordenadas[0]-i][coordenadas[1]] = "O"

            elif orientacion == "S":
                self.tablero[coordenadas[0]+i][coordenadas[1]] = "O"

            elif orientacion == "E":
                self.tablero[coordenadas[0]][coordenadas[1]+i] = "O"

            elif orientacion == "O": 
                self.tablero[coordenadas[0]][coordenadas[1]-i] = "O"


    def inicializar_tablero(self):#, tipo_barco, coordenadas, orientacion):
        
        print("""\nTienes a tu disposición:
4 barcos pequeños de 1 posición de eslora 
3 barcos medianos de 2 posiciones de eslora
2 barcos grandes de 3 posiciones de eslora
1 barco enorme de 4 posiciones de eslora""")
        
        try:

            barcos_colocados = 0
            while barcos_colocados < 10:
                
                self.tablero_mostrado()

                #INPUT TAMAÑO

                repeat = True
                check_input_tamaño = False

                while repeat == True or check_input_tamaño == False:
                    num_tipo_barco = int(input("""\nIntroduce el tamaño del barco: 
0 - Pequeño 
1 - Mediano
2 - Grande
3 - Enorme

Tamaño: """))

                    
                    if num_tipo_barco == 0:
                        tipo_barco = 'pequeño'
                        check_input_tamaño = True
                        if self.num_barcos[num_tipo_barco] != 0:
                            self.num_barcos[num_tipo_barco] -= 1
                            repeat = False
                        else:
                            print("\nNo tienes más barcos pequeños")
                            repeat = True

                    elif num_tipo_barco == 1:
                        tipo_barco = 'mediano'
                        check_input_tamaño = True
                        if self.num_barcos[num_tipo_barco] != 0:
                            self.num_barcos[num_tipo_barco] -= 1 
                            repeat = False
                        else:
                            print("\nNo tienes más barcos medianos")
                            repeat = True

                    elif num_tipo_barco == 2:
                        tipo_barco = 'grande'
                        check_input_tamaño = True
                        if self.num_barcos[num_tipo_barco] != 0:
                            self.num_barcos[num_tipo_barco] -= 1 
                            repeat = False
                        else:
                            print("\nNo tienes más barcos grandes")
                            repeat = True

                    elif num_tipo_barco == 3:
                        tipo_barco = 'enorme'
                        check_input_tamaño = True
                        if self.num_barcos[num_tipo_barco] != 0:
                            self.num_barcos[num_tipo_barco] -= 1 
                            repeat = False
                        else:
                            print("\nNo tienes más barcos enormes")
                            repeat = True
                    else:
                        check_input_tamaño = False #Lo q han introducido no es valido
                        print("\n Tienes que introducir un 0, 1, 2 o 3 para elegir.")
                    
                    if sum(self.num_barcos)== 0:
                        print("\n Bien hecho. Has colocado todos los barcos!")
                        repeat = False
                
                #INPUT COORDENADAS

                check_input_coors = False
                while check_input_coors == False:
                    
                    string_coordenadas = input("\nIntroduce la posición inicial del barco (Ej:A1):" )
                    string_coordenadas = string_coordenadas.upper()
                    if string_coordenadas not in c.coors_tab:
                        check_input_coors = False
                        print("\nNo es una coordenada válida, introdúcela en mayúsculas y sin espacios (Ej:J9)")
                    else:
                        check_input_coors = True

                coordenadas = np.array([0,0])
                if string_coordenadas[0] == 'A':
                    coordenadas[0] = 0
                elif string_coordenadas[0] == 'B':
                    coordenadas[0] = 1
                elif string_coordenadas[0] == 'C':
                    coordenadas[0] = 2
                elif string_coordenadas[0] == 'D':
                    coordenadas[0] = 3
                elif string_coordenadas[0] == 'E':
                    coordenadas[0] = 4
                elif string_coordenadas[0] == 'F':
                    coordenadas[0] = 5
                elif string_coordenadas[0] == 'G':
                    coordenadas[0] = 6
                elif string_coordenadas[0] == 'H':
                    coordenadas[0] = 7
                elif string_coordenadas[0] == 'I':
                    coordenadas[0] = 8
                elif string_coordenadas[0] == 'J':
                    coordenadas[0] = 9

                coordenadas[1] = int(string_coordenadas[1::])-1

                #INPUT ORIENTACION

                check_input_or = False
                while check_input_or ==False:
                    orientacion = input("""\nIntroduce la orientacion con la que colocar el barco (ej:N)
N - Norte
S - Sur
E - Este
O - Oeste
                
Orientación:""")
                    if orientacion not in ['N', 'S', 'E', 'O']:
                        check_input_or = False
                        print("\n Orientación no válida. Introduce una N, S, E u O.")
                    else:
                        check_input_or = True

                        
                habia_barco = self.hay_barco_ahi(tipo_barco, coordenadas, orientacion)
                
                if habia_barco == False:

                    if orientacion == "N":
                        if coordenadas[0] - self.barco[tipo_barco] < -1:
                            print("\nTu barco se sale del tablero por arriba")
                            self.num_barcos[num_tipo_barco] += 1 
                            
                        else:
                            self.colocar_barco(tipo_barco, coordenadas, orientacion)
                            barcos_colocados +=1
                            self.tablero_mostrado()

                    elif orientacion == "S":
                        if coordenadas[0] + self.barco[tipo_barco] > 10:
                            print("\nTu barco se sale del tablero por abajo")
                            self.num_barcos[num_tipo_barco] += 1 
                            
                        else:
                            self.colocar_barco(tipo_barco, coordenadas, orientacion)
                            barcos_colocados +=1
                            self.tablero_mostrado()
                    
                    elif orientacion == "E":
                        if coordenadas[1] + self.barco[tipo_barco] > 10:
                            print("\nTu barco se sale del tablero por la derecha")
                            self.num_barcos[num_tipo_barco] += 1 
                            
                        else:
                            self.colocar_barco(tipo_barco, coordenadas, orientacion)
                            barcos_colocados +=1
                            self.tablero_mostrado()

                    elif orientacion == "O":
                        if coordenadas[1] - self.barco[tipo_barco] < -1:
                            print("\nTu barco se sale del tablero por la izquierda")
                            self.num_barcos[num_tipo_barco] += 1 
                            
                        else:
                            self.colocar_barco(tipo_barco, coordenadas, orientacion)
                            barcos_colocados +=1
                            self.tablero_mostrado()

                elif habia_barco == True:
                    print('\nCuidado, no puedes pisar otro barco o salirte del tablero')
                    self.num_barcos[num_tipo_barco] += 1 
        
        except:
            print('\nLas coordenadas para poner el barco no están dentro del tablero')

        return self.tablero_mostrado()

    
    def tablero_random(self):
        """Crea un tablero con barcos en una posición random
            4 barcos de 1 posición de eslora 
            3 barcos de 2 posiciones de eslora
            2 barcos de 3 posiciones de eslora
            1 barco de 4 posiciones de eslora"""

        barcos_disponibles = ['enorme','grande','grande','mediano','mediano','mediano','pequeño','pequeño','pequeño','pequeño']

        for elem in barcos_disponibles:
            
            habia_barco = True
            barco_se_sale = True

            while habia_barco == True or barco_se_sale == True:
                coordenadas_aleatorias = np.random.randint(0,10,size=2)

                orientacion = random.choice(['N', 'S', 'E', 'O'])
                """orientacion_aleatoria = np.random.randint(4) # N=0, S=1, E=2, O=3
                if orientacion_aleatoria == 0:
                    orientacion = 'N'
                elif orientacion_aleatoria == 1:
                    orientacion = 'S'
                elif orientacion_aleatoria == 2:
                    orientacion = 'E'
                elif orientacion_aleatoria == 3:
                    orientacion = 'O'"""
                
                #1 Check de que no hay un barco donde quieres colocarlo
                habia_barco = self.hay_barco_ahi(elem, coordenadas_aleatorias, orientacion)

                #2 Check de que el barco no se sale del tablero al pintarlo    
                if orientacion == 'N' and (coordenadas_aleatorias[0] - self.barco[elem] >= 0):
                    barco_se_sale = False
                elif orientacion == 'S' and (coordenadas_aleatorias[0] + self.barco[elem] <= 9):
                    barco_se_sale = False
                elif orientacion == 'E' and (coordenadas_aleatorias[1] + self.barco[elem] <= 9):
                    barco_se_sale = False
                elif orientacion == 'O' and (coordenadas_aleatorias[1] - self.barco[elem] >= 0):
                    barco_se_sale = False
                else:
                    barco_se_sale = True

                if habia_barco == False and barco_se_sale == False:
                    continue
                

            if habia_barco == False and barco_se_sale == False: 
                
                if orientacion == 'N':
                    self.colocar_barco(elem, coordenadas_aleatorias, orientacion)
                
                elif orientacion == 'S':
                    self.colocar_barco(elem, coordenadas_aleatorias, orientacion)
                        
                elif orientacion == 'E':
                    self.colocar_barco(elem, coordenadas_aleatorias, orientacion)
                
                elif orientacion == 'O':
                    self.colocar_barco(elem, coordenadas_aleatorias, orientacion)
                
        #return self.tablero_mostrado() #Quitar almohadilla para debuggear, se vera el tablero del oponente

    
    def disparo(self, coordenadas):

        if coordenadas[0] == 'A':
            fil = 0
        elif coordenadas[0] == 'B':
            fil = 1
        elif coordenadas[0] == 'C':
            fil = 2
        elif coordenadas[0] == 'D':
            fil = 3
        elif coordenadas[0] == 'E':
            fil = 4
        elif coordenadas[0] == 'F':
            fil = 5
        elif coordenadas[0] == 'G':
            fil = 6
        elif coordenadas[0] == 'H':
            fil = 7
        elif coordenadas[0] == 'I':
            fil = 8
        elif coordenadas[0] == 'J':
            fil = 9
        

        if type(coordenadas[0]) == np.int32: # Si usas windows el valor de int debe ser np.int32!!!!!!!!!!
            fil = coordenadas[0]
            
        col = int(coordenadas[1::]) - 1

        if self.tablero[fil][col] == self.mar:
            # fallado
            self.tablero[fil][col] = self.mar_t
            return False

        elif self.tablero[fil][col] == self.barc:
            # acertado
            self.tablero[fil][col] = self.tocado
            return True
    
    
    def disparos_efectuados(self, coordenadas, oponente_tocado):
        if coordenadas[0] == 'A':
            fil = 0
        elif coordenadas[0] == 'B':
            fil = 1
        elif coordenadas[0] == 'C':
            fil = 2
        elif coordenadas[0] == 'D':
            fil = 3
        elif coordenadas[0] == 'E':
            fil = 4
        elif coordenadas[0] == 'F':
            fil = 5
        elif coordenadas[0] == 'G':
            fil = 6
        elif coordenadas[0] == 'H':
            fil = 7
        elif coordenadas[0] == 'I':
            fil = 8
        elif coordenadas[0] == 'J':
            fil = 9

        if type(coordenadas[0]) == np.int32:
            fil = coordenadas[0]
            
        col = int(coordenadas[1::]) - 1


        if oponente_tocado == True:
            self.tablero[fil][col] = self.tocado
        elif oponente_tocado == False:
            self.tablero[fil][col] = self.mar_t



    def tablero_mostrado(self):
        '''
        tableros moatrados por pantalla
        a partir de tableros introducidos por la funcion tableros()
        '''
        alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        alfabeto = alfabeto[0 : len(self.tablero)]

        lista_alf = list(alfabeto)
        matriz_letra = np.array([list(i) for i in lista_alf])
        lista_num = np.arange(11).reshape((1,11))

        suma = np.concatenate((matriz_letra, self.tablero), axis= 1)
        tot = np.vstack((lista_num, suma))

        print("\n")
        print(tot) 



