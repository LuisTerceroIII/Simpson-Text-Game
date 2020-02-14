from main import *
from configuracion import *
import random
import math
import pygame

pygame.init()
pygame.mixer.init()
#----------------------------------------------------------------------------------------------------#

#Funciones para limpiar archivo de subtitulos

def removerEspeciales(cadena): #Con esta funcion eliminamos todo caracter especial reemplazandolos con espacios.
    linea = ""
    for char in cadena:
        if((char >= "A" and char <= "Z") or (char >= "a" and char <= "z") or ord(char) == 209 or ord(char) == 241):
            linea = linea + char
        else:
            linea = linea + " "
    return linea

def soloLetras(linea):#Verificamos que la cadena tenga letras, si no es el caso, no debemos trabajar con ella.
    for char in linea:
        if((char >= "A" and char <= "Z") or (char >= "a" and char <= "z") or ord(char) == 209 or ord(char) == 241):
            return True
    return False

def elminarReciduos(linea): #Los reciduos a los que me refiero son las i's que quedan en frases por ejemplo: <i>Daly... Daly...</i> .
    lineaFinal = ""
    for i in range(len(linea)-1):
       if linea[i] == "i" and (linea[i+1] == " " and linea[i-1] == " "):
              lineaFinal = lineaFinal
       else:
            lineaFinal = lineaFinal + linea[i]
    return lineaFinal + linea[-1]

def borrarEspaciosSeguidos(linea):#Se elimina el problema de que aparezacan frases de 2 palabras o una palabra por los espacios extras.
    lineaFinal = ""
    for i in range(len(linea)-1):
        if (linea[i] == " " and linea[i+1] == " "):
            lineaFinal = lineaFinal
        else:
            lineaFinal = lineaFinal + linea[i]
    return lineaFinal + linea[-1]

def cuentaPalabras(cadena):#Cuenta las palabras en una cadena, cada vez que hay un espacio se cuenta como una.
    cont = 0
    for c in cadena:
        if(c == " "):
            cont = cont + 1
    return cont

def lectura(archivo, subtitulo,n):
    lineas = archivo.readlines() #Creo lista con texto sin filtrar.
    archivo.close()#Cerramos el archivo, pues ya no lo usaremos mas.
    for linea in lineas:#Recorro la lista por linea, para filtrar por linea.
        linea1 = removerEspeciales(linea)#Limpio linea de caracteres especiales. OJO TAMBIEN ENTRAN LINEAS DE SOLO ESPACIOS.
        if(soloLetras(linea1) == True):#Dado que el archivo posee lineas en blanco, verificamos que sean lineas de texto y no solo de espacios.
            linea2 = elminarReciduos(linea1)#Limpio la linea de las i's que quedan en algunas frases, por ejemplo: <i>Daly... Daly...</i> .
            linea3 = borrarEspaciosSeguidos(linea2)#Elimino espacios extras, dado que cuento una palabra cada espacio, tener dos espacios seguidos genera problemas.
            largoDeLinea = cuentaPalabras(linea3)#Agrego esta variable y funcion para saber la cantidad de palabras que tiene una linea.
            if(largoDeLinea > n): #Agregamos linea si posee 3 palabras o mas.
                subtitulo.append(linea3.lower())#Finalmente la linea esta limpia en el tercer filtro, y es agregada a la lista subtitulo.

#Hasta aqui las funciones que sirven para limpiar archivo

#----------------------------------------------------------------------------------------------------#
#Funciones para elegir las frases que se mostraran en pantalla
def seleccion(subtitulo):
    lista = [] #Declaramos la lista que contendra las frases que se veran por pantalla.
    principal = random.randrange(len(subtitulo) - 1)#Elegimos la frase principal y nos haceguramos que no sea la ultima de la pelicula.
    lista.append(subtitulo[principal])#Agregamos frase principal a lista, y queda en lista[0].
    lista.append(subtitulo[principal + 1])#Agregamos la frase siguiente, es decir la correcta, y queda en lista[1].
    otro = random.randrange(len(subtitulo))#Buscamos una posicion random para la frase trampa.
    while(otro == principal):#Verificamos que otro no sea igual a principal.
        otro = random.randrange(len(subtitulo))#Si otro es igual a principal se sortea otra vez, hasta que no sean iguales.
    lista.append(subtitulo[otro])#Agregamos la frase trampa,y queda en lista[2].
    return lista #Retornamos la lista con las 3 frases.

def aparece(elem,lista): #Funcion simple que recibe una lista y un elemento, y retorna True si el elemento pertence a lista.
    for elemento in lista:
        if(elem == elemento):
            return True
    return False
#Para la implementacion de la funcionalidad "sin repetidos" considere necesario el uso de una lista extra, la lista de "subsUsados" y la funcion aparece(elem,lista).
#El criterio de no repetidos que usa es: cuando una frase aparece como principal, ya no saldra otra vez, con la intencion de que no exitan las preguntas repetidas.
def sinSubRepetidos(subsUsados,subsCompleto):#Recibe una lista de subtitulos usados, y la lista de todos los subtitulos, y rotorna una lista que nunca repite preguntas.
    subsRandom = seleccion(subsCompleto)#Obtengo una lista de randoms.
    buscando = True #Bandera para ciclo.
    vueltas = 0 #Variable que cuenta las vueltas, con el motivo de saber cuando se han mostrado todas las frases.
    while buscando:
        if(aparece(subsRandom[0],subsUsados)):#Verificamos que la frase principal no aparesca la lista "subsUsados".
            subsRandom = seleccion(subsCompleto)#Si se da el caso que ya exista, se buscaran nuevos subtitulos random.
        else:
            subsUsados.append(subsRandom[0])#Se agrega frase principal para que no vuelvan a repetirse las jugadas.
            buscando = False#Cerramos el ciclo.
        if(vueltas == len(subsCompleto) * 3):#Verificamos que aun hallan frases sin aparecer.
            subsRandom = ["Muchas Gracias Por Jugar", "GAME", "OVER"]#Si ya no quedan frases por aparecer, vemos esas frases por pantalla.
        vueltas = vueltas + 1 #Contamos vueltas.
    return subsRandom#Lista de sub sin usar.

#----------------------------------------------------------------------------------------------------#
#Funciones para verificar jugada y puntaje

#La funcion aparece(elem,lista) usada en el punto anterios, es aqui reutilizada.

def deCadenaALista(cadena):#Funcion que recibe una cadena y retorna una lista, con la intencion de manejar las frases por palabras.
    palabra  = "" #Cadena vacia para armar palabras.
    palabras = [] #Cadena que retornara con las palabras de la cadena.
    for char in cadena:#Se recorre la cadena por caracter.
        if(char == " " ):#Si el caracter es igual a espacio, significa que hay una palabra completa.
            palabras.append(palabra)#Se agrega una palabra completa a la lista palabras.
            palabra = ""#Se vacia la cadena para armar la siguiente palabra.
        else:
            palabra = palabra + char#Se arma caracter por caracter la palabra.
    return palabras#Lista con palabras.

def puntos(n):
    #devuelve el puntaje, segun seguidilla
    return 2**n

def longitudMinima(palabraUsuario):
    return len(palabraUsuario) < 3

def procesar(palabraUsuario, mostrada,siguiente, otra, correctas,acierta,falla,screen):
    bien = pygame.image.load("Check.png")#Carteles que aparece cuando se responde bien
    mal = pygame.image.load("fail.png")#Carteles que aparece cuando se responde mal
    #chequea que sea correcta, que pertenece solo a la frase siguiente. Devuelve puntaje segun seguidilla
    listaSiguiente = deCadenaALista(siguiente)#La funcion llamada deCadenaALista(cadena), toma una cadena y rotorna una lista con una palabra por posicion.
    listaOtra = deCadenaALista(otra)#Hago lo mismo que arriba pero con la frase random.
    if(aparece(palabraUsuario,listaSiguiente) and aparece(palabraUsuario,listaOtra)):#Se utiliza la funcion aparece() para buscar si la palabra ingresada por el usuario
    #aparece en ambas frases, lo que resultaria en un descuento de puntos, al ser tomado como un error.
        falla.play()#Efecto de sonido correspondiente al opcional "Efectos de sonidos".
        c = 0 #Variable contador
        while c < 25:#Agregamos este ciclo para mostrar por un tiempo mas largo la imagen de falla.
            screen.blit(mal,(810,400))
            pygame.display.flip()
            c = c + 0.10
        return -3 #Retorna un -3 en concepto de los puntos perdidos.

    if(aparece(palabraUsuario,listaSiguiente)):#Se verifica si la palabra ingresada por el usuario es la correcta o no.
        acierta.play()#Efecto de sonido correspondiente al opcional "Efectos de sonidos".
        b = 0 #Variable contador
        while b < 20:#Agregamos este ciclo para mostrar por un tiempo mas largo la imagen de acierto.
            screen.blit(bien,(810,400))
            pygame.display.flip()
            b = b + 0.10
        return puntos(correctas)#Se llama a la funcion puntos(n), la cual retorna una cantidad de puntos en razon de la cantidad seguida de aciertos.

    if(longitudMinima(palabraUsuario)):#Verificamos que la longitud de la palabra ingresada. El criterio utilizado es: se da aviso y se restan puntos al igual a como si fuera un error.
        cartelLongitudMin = pygame.image.load("AtencionLen.png")
        i = 0
        while i < 30:#Agregamos este ciclo para mostrar por un tiempo mas largo la imagen de longitud minima.
            screen.blit(cartelLongitudMin,(200,220))
            pygame.display.flip()
            i = i + 0.10
        return -3

    else:#Se asume que la persona o escribio una palabra de la frase random o no escribio ninguna palabra correcta.
        falla.play() #sonido error.
        a = 0 #Variable contador
        while a < 25:
            screen.blit(mal,(810,400))#se agrega una imagen
            pygame.display.flip()#se actualiza la ventana
            a = a + 0.10
        return -3 #Retorna un -3 en concepto de los puntos perdidos


