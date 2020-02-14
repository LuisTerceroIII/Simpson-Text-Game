import pygame
from pygame.locals import *
from configuracion import *
from funciones import *

def dameLetraApretada(key):

    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_SEMICOLON:#Se agrega el manejo de la letra ñ utilizando la tecla "";"" correspondiente a la ñ en teclado español.
        return("ñ")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")


def dibujar(screen, palabraUsuario, lista, azar, puntos, segundos,cuentaRegresiva):

    defaultFont= pygame.font.Font("VCR_OSD_MONO_1.001.ttf", TAMANNO_LETRA)
    titulo = pygame.font.Font("VCR_OSD_MONO_1.001.ttf", 40)
    defaultFontGrande= pygame.font.Font("VCR_OSD_MONO_1.001.ttf", TAMANNO_LETRA_GRANDE)#pygame.font.get_default_font()

    #carga lo que escribe el jugador en pantalla
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (190, 530))
    #carga el puntaje del jugador
    screen.blit(defaultFont.render("Puntos:" + str(puntos), 1, COLOR_TEXTO), (810, 40))

    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        cuentaRegresiva.play()
        ren = defaultFont.render("Tiempo:" + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo:" + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (60, 40))

    #carga el nombre de la Pelicula
    screen.blit(titulo.render("THE SIMPSONS", 1, COLOR_PELI), (350,70))

    #carga los subtitulos en la pantalla
    screen.blit(defaultFontGrande.render(lista[0], 1, COLOR_TEXTO), (ANCHO//2-len(lista[0])*TAMANNO_LETRA_GRANDE//3.5,(TAMANNO_LETRA_GRANDE)*4))
    if azar==0:
        screen.blit(defaultFontGrande.render(lista[1], 1, COLOR_LETRAS), (ANCHO//2-len(lista[1])*TAMANNO_LETRA_GRANDE//3.5,(TAMANNO_LETRA_GRANDE)*6))
        screen.blit(defaultFontGrande.render(lista[2], 1, COLOR_LETRAS), (ANCHO//2-len(lista[2])*TAMANNO_LETRA_GRANDE//3.5,(TAMANNO_LETRA_GRANDE)*8))
    else:
        screen.blit(defaultFontGrande.render(lista[2], 1, COLOR_LETRAS), (ANCHO//2-len(lista[2])*TAMANNO_LETRA_GRANDE//3.5,(TAMANNO_LETRA_GRANDE)*6))
        screen.blit(defaultFontGrande.render(lista[1], 1, COLOR_LETRAS), (ANCHO//2-len(lista[1])*TAMANNO_LETRA_GRANDE//3.5,(TAMANNO_LETRA_GRANDE)*8))

def pantallaInicio(screen):#Carga y ejecuta todo lo necesario para mostrar una ventana de entrada, con reglas y tema del juego.

    inicio = pygame.image.load("Pantalla1_comienzo.jpg")
    enter = pygame.mixer.Sound("star.wav")
    pygame.mixer.music.play(-1)#Se inicia la musica en loop inifinito
    screen.blit(inicio,(0,0))
    pygame.display.flip()
    play = True
    while play:#Mantiene la pantalla visible hasta que se cierre o hasta que la persona presione enter.
        for e in pygame.event.get():
            if e.type == QUIT:
                    pygame.quit()
                    sys.exit(0)#esta linea sirve para que no se desinicialicen los modulos de pygame   https://stackoverflow.com/questions/49845387/pygame-error-video-system-not-initialized-pygame-init-already-called
                    return()
            if e.type == KEYDOWN:
                if e.key == K_RETURN:
                    enter.play()
                    play = False

def pantallaJugando(screen):#Funcion que despliega la pantalla de juego y la siguiente pantalla que nos direcciona a los records

        fondo = pygame.image.load("Pantallas2_juego.jpg")
        acierto = pygame.mixer.Sound("acierto.wav")
        equivocado = pygame.mixer.Sound("equivocado.wav")
        letras = pygame.mixer.Sound("letras.wav")
        cuentaRegresiva = pygame.mixer.Sound("sinTiempo.wav")
        sinTiempo = pygame.mixer.Sound("sinTiempo2.wav")
        puntos = 0
        palabraUsuario = ""

        subtitulo=[]
        subtitulosUsados = []#Lista con los subtitulos usados - Opcional "Sin Repetidos"
        correctas=0

        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        archivo= open("TheSimpsons.srt","r")

        lectura(archivo, subtitulo, N)#lectura del archivo y filtrado de caracteres especiales
        #elige un subtitulo al azar, su s iguiente y otro
        lista=sinSubRepetidos(subtitulosUsados,subtitulo)#Tomamos 3 subtitulos cuidando de no tomar como principal el mismo subtitulo dos veces
        azar=random.randrange(2)
        i = 0.3333 #Agrego esta variable para regular el tiempo en la pantalla jugando.
        while segundos > fps/1000:

            time = gameClock.tick(fps)#Puede ser que si los elimino no pase nada.
            totaltime += gameClock.get_time()

            if True:
            	fps = 3

            for e in pygame.event.get():
                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    sys.exit(0)
                    return()

                if e.type == KEYDOWN:
                    letras.play()
                    letra = dameLetraApretada(e.key)
                    palabraUsuario += letra
                    if e.key == K_BACKSPACE:
                        palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                    if e.key == K_RETURN:
                        sumar=procesar(palabraUsuario, lista[0], lista[1], lista[2],correctas,acierto,equivocado,screen)#chequea si es correcta y suma o resta puntos
                        puntos+=sumar#actualiza el puntaje de la partida
                        if sumar>0:#Si el jugador logra puntos positivos significa que comienza seguidilla para bonos de puntos.
                            correctas=correctas+1
                        else:
                            correctas=0

                        lista=sinSubRepetidos(subtitulosUsados,subtitulo)#Tomamos 3 subtitulos cuidando de no tomar como principal el mismo subtitulo dos veces
                        palabraUsuario = ""
                        #cambia el orden al azar
                        azar=random.randrange(2)

            segundos = TIEMPO_MAX - i
            i = i + 0.333
            #Limpiar pantalla anterior
            screen.blit(fondo,(0,0))
            #Dibujar de nuevo todo
            dibujar(screen, palabraUsuario, lista, azar, puntos, segundos,cuentaRegresiva)
            pygame.display.flip()
        pantallaContinuar(screen,puntos,palabraUsuario)#Llamamos a pantalla continuar con intension de no hacer tan abrupto el paso de una pantalla a otra.

def pantallaContinuar(screen,puntos,palabraUsuario):

    continuar = pygame.image.load("EnterContinuar.png")
    screen.blit(continuar,(320,400))
    pygame.display.flip()
    play = True
    while play: # Ciclo que mantiene la ventana abierta hasta que se cumpla uno de los dos eventos, cierre de venta o enter
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit(0)
                return()
            if e.type == KEYDOWN:
                if e.key == K_RETURN:
                    play = False
                    pantallaRecords(screen,palabraUsuario,puntos)
                    return()

def swapElemento(matriz,a,b):# Funcion auxiliar de swap utilizada en la funcion verificarRecord(palabraUsuario,puntos)
    aux = matriz[a]
    matriz[a] = matriz[b]
    matriz[b] = aux

def deMinAMax(matriz):#Funcion auxiliar de ordenamiento burbuja utilizada en la funcion verificarRecord(palabraUsuario,puntos)
    try:
        for e in range(1,len(matriz)):
            for i in range(len(matriz) - e):
                if(int(matriz[i][1]) > int(matriz[i+1][1])):
                    swapElemento(matriz,i,i+1)
    except ValueError:
        print ("Invalid string found in: {}".format(matriz))

def deMinAMaxList(lista):#Funcion auxiliar de ordenamiento burbuja utilizada en la funcion verificarRecord(palabraUsuario,puntos)
    try:
        for e in range(1,len(lista)):
            for i in range(len(lista) - e):
                if(lista[i]> lista[i+1]):
                    swapElemento(lista,i,i+1)
    except ValueError:
        print ("Invalid string found in: {}".format(var))

def invertirMatriz(matriz):#Funcion auxiliar para invertir matrices utilizada en la funcion verificarRecord(palabraUsuario,puntos)
    copy = []
    for i in range(len(matriz)-1,-1,-1):
        copy.append(matriz[i])
    return copy

def verificarRecord(palabraUsuario,puntos):#Esta funcion se encarga de abrir y escribir los records en el archivo, ademas de evaluar si el puntaje entra entre los diez mejores.

    archivoRecords = open("records.txt","r+")
    listaRecords = archivoRecords.readlines()


    matrizRecords = [["",0],["", 0],["",0],["",0],["",0],["",0],["",0],["",0],["",0],["",0],["",0]]
    nombres = ""
    puntaje = ""
##    if len(listaRecords)>
    for i in range(len(listaRecords)):#En este ciclo leemos el archivo y lo pasamos a la matrizRecords.
        for char in listaRecords[i]:
            if char != "," and (char >= "A" and char <= "Z") or (char >= "a" and char <= "z") or ord(char) == 209 or ord(char) == 241:
                nombres = nombres + char
            if char == "-" or char == "0" or char == "1" or char == "2" or char == "3" or char == "4" or char == "5"or char == "6"or char == "7"or char == "8"or char == "9":
                puntaje = puntaje + char

        matrizRecords[i][0] = nombres
        print(matrizRecords)
        matrizRecords[i][1] = puntaje
        nombres = ""
        puntaje = ""

    i = 0
    while matrizRecords[i][0] != "":#Revisamos en que posicion podemos ingresar para no sobreescribir
        i = i + 1

    if i <= 10:#Regulamos que no hallan mas de diez records
        matrizRecords[i][0] = palabraUsuario #Agregamos el nombre del jugador
        matrizRecords[i][1] = puntos # Agregamos los puntos obtenidos en la partida
        deMinAMax(matrizRecords)#Ordenamos la matriz de menor a mayor
        archivoRecords.write(palabraUsuario+","+str(puntos)+"\n")#Agregamos el nuevo record al archivo
        archivoRecords.close()
        return invertirMatriz(matrizRecords)#Retornamos la matriz ordenada de menor a mayor invertida, es decir con el puntaje mas alto primero
    else:#Evaluamos el caso en que ya esten ocupados los 10 puestos.
        nuevoRecord = 0
        for i in range(len(matrizRecords)):
            nuevoRecord =  matrizRecords[i][1] - puntos # Verificamos si el nuevo puntaje es mayor a alguno ingresado
            if nuevoRecord < 0:# Si la diferencia es menor a cero significa que el nuevo puntaje entra.
                aux = matrizRecords[i]#Guardamos el record que se desplaza un puesto mas abajo
                matrizRecords[i+1][1] = puntos#Agregamos el nuevo records a la matriz
                matrizRecords[i+1][0] = palabraUsuario
                matrizRecords.append(aux) #Volvemos a agregar al final el elemento reemplazado
                archivoRecords.write(palabraUsuario+","+str(puntos)+"\n") # Agregamos el nuevo record al archivo
                archivoRecords.close()
                deMinAMax(matrizRecords)# Ordenamos la matriz de menor a mayor
                records = invertirMatriz(matrizRecords)# Retornamos la matriz ordenada de menor a mayor invertida, es decir con el puntaje mas alto primero
                records.pop(-1) # Eliminamos los records extras
                records.pop(-1) # Eliminamos los records extras
            break
        return records

def dibujarRecords(screen,registroRecord): # Funcion que recibe los records y los pinta en la pantalla

    defaultFont= pygame.font.Font("VCR_OSD_MONO_1.001.ttf", 25)
    ejeY = 0
    i = 0
    puesto = 1
    while i < len(registroRecord): # Recorremos la matriz y la mostramos en pantalla.
        if(registroRecord[i][0] != "" and registroRecord[i][1] != 0):
            screen.blit(defaultFont.render(str(puesto)+".- "+str(registroRecord[i][0]) +" "+ str(registroRecord[i][1]),1,(255,255,255)),(100,130 + ejeY ))
            ejeY = ejeY + 20
            puesto = puesto + 1
            if puesto == 10:
                puesto = 10
            pygame.display.flip()
        i = i + 1

    o = 0
    while o < 10000000:#Ciclo que mantiene visible por un tiempo la pantalla
        o = o + 0.30

    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit(0)
            return()
        if e.type == K_RETURN:
            run = False
            return()

def guardarRecords(registroRecord):
    nuevosRecords = open("records.txt","w")
    lista = []
    print("Estoy en guardar",registroRecord)
    for i in range(len(registroRecord)):
        if not (registroRecord[i][0] == "" and registroRecord[i][1] == 0):
            lista.append(registroRecord[i][0] +","+ str(registroRecord[i][1]))
    print("Soy la lista que va al archivo",lista)
    for record in lista:
        nuevosRecords.write(record + "\n")
    nuevosRecords.close()


def pantallaRecords(screen,palabraUsuario,puntos): # Funcion que tiene todos los datos para desplegar la pantalla record.

    defaultFont= pygame.font.Font("VCR_OSD_MONO_1.001.ttf", TAMANNO_LETRA)
    records = pygame.image.load("Pantalla3_records.jpg")
    letras = pygame.mixer.Sound("letras.wav")
    play = True

    registroRecord = []

    while play:
        screen.blit(records,(0,0))
        screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (320, 540))
        pygame.display.flip()

        #Esperar el QUIT del usuario
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit(0)
                return()
            if e.type == KEYDOWN:
                letras.play()
                letra = dameLetraApretada(e.key)
                palabraUsuario += letra
                if e.key == K_BACKSPACE:
                    palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                if e.key == K_RETURN:
                    registroRecord = verificarRecord(palabraUsuario,puntos)
                    dibujarRecords(screen,registroRecord)
                    guardarRecords(registroRecord)
                    return()
    pygame.display.flip()