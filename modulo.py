# Función que muestra el menú principal y verifica la opción válida
def Menu_Principal(n):
    print("MENÚ PRINCIPAL\n\nEscoge una opción de juego:\n1. Partida modo solitario\n2. Partida 2 jugadores\n3. Estadística\n4. Salir\n")
    while (n<1 or n>4):
        n=input("Escoja una opción: ")
        #Verificamos que la cadena ingresada sólo contenga números
        n=verificacion_numero(n,1,4)
    print("")
    return n

# Función que muestra el menú de opciones para ambos modos de juego y verifica que sean opciones válidas
def Menu_Dificultad(p):
    print("Elija la dificultad:\n1. Fácil (20 intentos)\n2. Medio (12 intentos)\n3. Difícil (5 intentos)\n4. Regresar\n")
    while (p<1 or p>4):
        p=input("Escoja una dificultad: ")
        print("")
        #Se verifica que la opción de dificultad sea una opción válida
        p=verificacion_numero(p,1,4)
    return p

# Función que muestra el menú de estadísticas y verifica que las opciones ingresadas sean válidas
def Menu_estadisticas(q):
    print("Ecoja una opción de estadística:\n1. Estadística general (modo solitario)\n2. Estadísticas por nombre (modo solitario)\n3. Estadística general (modo 2 jugadores)\n4. Salir al menu")
    while (q<1 or q>4):
        q=input("Escoja una opción de estadística: ")
        print("\n")
        q=verificacion_numero(q,1,4)
    return q

#Función con la lógica de juego de un jugador
def juego_1jugador(random,pygame,sonido_victoria,sonido_perdida,x):
    #Dependiendo de la dificultad escogida en el programa principal, se establencen los intentos con el input x
    intentos=x
    acierto=0
    num=random.randint(1,1000)
    # Mientras los intentos no lleguen a 0 ni se acierte, ocurre la lógica de comparación del jugador con el número aleatorio
    while intentos!=0 and acierto!=1:
        jugador=0
        while jugador<1 or jugador>1000:
            jugador=input("Intente adivinar el número(entre 1 y 1000): ")
            jugador=verificacion_numero(jugador,1,1000)
            
        #Si el jugador aún no adivina
        if jugador!=num:
            print("¡Error!")
            #Si el número ingresado es mayor que el número a adivinar
            if jugador>num:
                print("El número ingresado es mayor")
            #Si el número ingresado es menor que el número a adivinar
            else:
                print("El número ingresado es menor")
            #Se va restando la cantidad de intentos
            intentos=intentos-1
            #EVALUAR - Muestra los intentos restantes
            print("Intentos restantes: "+str(intentos)+"\n")
        # Cuando acierte
        else:
            acierto=1
    #Cuando se termina la evaluación del while se verifica si el jugador ganó o perdió
    if jugador==num:
        print("Correcto! HAS GANADO!"+"\n")
        pygame.mixer.music.pause()
        sonido_victoria.play()
        nombre=input("Por favor, ingrese su nombre/alias: ")
        print("")
        pygame.mixer.music.unpause()
    elif intentos==0:
        sonido_perdida.play()
        print("Ha perdido, el número correcto era: "+str(num)+"\n")
        nombre=input("Por favor, ingrese su nombre/alias: ")
        print("")
    return nombre, acierto, intentos


#Función con la lógica de juego de dos jugadores
def juego_2jugadores(random,getpass,pygame,sonido_victoria,sonido_perdida,x):
    intentos=x
    acierto=0
    jug1=0
    #se verifica que el jugador 1 ingrese un número entre 1 y 1000
    while jug1<1 or jug1>1000:
        jug1=getpass("Jugador 1, ingrese el número a adivinar(entre 1 y 1000): ")
        jug1=verificacion_numero(jug1,1,1000)
    while intentos!=0 and acierto!=1:
        jug2=0
        #Se verifica que el jugador 2 ingrese un número entre 1 y 1000
        while jug2<1 or jug2>1000:
            jug2=input("Jugador 2, intente adivinar el número(entre 1 y 1000): ")
            jug2=verificacion_numero(jug2,1,1000)
        if jug1!=jug2:
            print("¡Error!")
            if jug1>jug2:
                print("El número ingresado es menor")
            else:
                print("El número ingresado es mayor")
            intentos=intentos-1
            print("Intentos restantes: "+str(intentos)+"\n")
        # Cuando JG2 acierte
        else:
            acierto=1
    if jug1==jug2:
        print("JUGADOR 2 GANA")
        pygame.mixer.music.pause()
        sonido_victoria.play()
        nombre_jg1=input("J1, Ingrese su nombre/alias: ")
        nombre_jg2=input("J2, Ingrese su nombre/alias: ")
        print("")
        pygame.mixer.music.unpause()
    elif intentos==0:
        print("JUGADOR 1 GANA, el número correcto era: "+str(jug1)+"\n")
        sonido_perdida.play()
        nombre_jg1=input("J1, Ingrese su nombre/alias: ")
        nombre_jg2=input("J2, Ingrese su nombre/alias: ")
        print("")
    return nombre_jg1, nombre_jg2, acierto, intentos


# Creamos una función para verificar que los inputs durante el programa sean numéricos y se encuentren en el rango a evaluar y muestren un mensaje cuando
# no se cumpla
def verificacion_numero(op,rango_inferior,rango_superior):
    if op.isdigit()==False:
        print("Debe ingresar un número")
        #n se reinicia a un valor 1 fuera del rango para volver a intentar las opciones
        op=0
    #Si la cadena n sólo contiene números
    else:
        #Se convierte al formato int para compararlo
        op=int(op)
        #Si no está entre el rango de opciones, envía un mensaje
        if op<rango_inferior or op>rango_superior:
            print("Opción inválida")
    #op se regresa siempre como un int para que se utilice en comparaciones fuera de la función
    return op

# Función que carga los sonidos de la música y efectos al ganar o perder. Inicializa la música bajo un configuración
def cargar_musica_y_sonidos(pygame):
    # Inicializar pygame y su módulo de sonido
    pygame.mixer.init()
    
    # Reproduce la música de fondo en bucle
    pygame.mixer.music.load("006- Earthbound - Choose a File.mp3")
    pygame.mixer.music.set_volume(0.5) #Se configura el nivel de volumen
    pygame.mixer.music.play(-1)  # Con el valor '-1' se indica que la música sonará en bucle
    
    # Cargar efecto de sonido para el acierto
    sonido_victoria = pygame.mixer.Sound("004- Earthbound - Title Screen.mp3")
    sonido_perdida = pygame.mixer.Sound("031- Earthbound - Ambush!.mp3")

    return sonido_victoria, sonido_perdida
    
# Se crea una función que muestran la tasa de éxito por dificultad de todos los jugadores que han jugado el juego
def estadistica(pd,plt):
    # Se leen los datos desde el archivo Excel
    archivo_excel = "D:\\Escritorio\\Master\\APUNTES\\TAREA 4\\Resultados_juego.xlsx"
    # Extraemos los datos de la primera hoja
    datos = pd.read_excel(archivo_excel, sheet_name=0)

    # En el recuadro se quiere tener las dicultades ordenadas de izquierda a derecha de fácil a difícil y se crea una lista 
    orden_dificultades = ["Fácil", "Medio", "Difícil"]
    
    # Se agrupan las dificultades y se agregan las columnas de partidas jugadas (se cuentan todas las filas de las partidas en cada dificultad 
    # y partidas parrtidas jugadas (se suman aquellas partidas que se acertaron, en este caso las que se acertó tendrán un 1, 0 en caso contrario)
    estadisticas = datos.groupby("dificultad").agg(
        partidas_jugadas=("acierto", "count"),
        partidas_ganadas=("acierto", "sum")
    ).reset_index() #Para que "dificultad" no sea el índice se usa el reset.index()
    
    # Queremos un orden especíco de las dificultades. Usamos categorical para definir una jerarquía de orden según la lista orden_dificultades
    estadisticas["dificultad"] = pd.Categorical(estadisticas["dificultad"], categories=orden_dificultades, ordered=True)
    # Luego de la jerarquía podemos hacer un sort por dificultad
    estadisticas = estadisticas.sort_values("dificultad").reset_index(drop=True)
    # Creamos y calculamos la tasa de éxito
    estadisticas["tasa_exito"] = (estadisticas["partidas_ganadas"] / estadisticas["partidas_jugadas"]) * 100

    # CREAMOS EL GRÁFICO Y DEFINIMOS SUS PROPIEDADES
    # Tamaño del recuadro
    plt.figure(figsize=(8, 6))
    
    plt.bar(estadisticas["dificultad"], estadisticas["tasa_exito"], color=["green", "orange", "red"])
    plt.title("Tasa de Éxito por Dificultad", fontsize=16)
    #Título del eje x
    plt.xlabel("Dificultad", fontsize=12)
    #Título del eje y
    plt.ylabel("Tasa de Éxito (%)", fontsize=12)
    #El rango de % que se va a mostrar en el recuadro. Se ajustó hasta 110% para que no haya colisión de texto
    plt.ylim(0, 110)
    #Tamaño de la fuente de cada barra
    plt.xticks(fontsize=10)
    #Tamaño de la fuente de cada hito de porcentaje en el eje y
    plt.yticks(fontsize=10)
    #Líneas punteadas horizontales, tipo y transparencia (alpha)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    
    # Agregamos los porcentajes encima de las barras. Usamos iterrows() para tener 'i' como indice de la fila y 'fila' como los valores de cada fila
    for i, fila in estadisticas.iterrows():
         plt.text(i, fila["tasa_exito"] + 2, f"{fila['tasa_exito']:.1f}%", ha="center", fontsize=10)
    # Explicación de cada elemento en el for:     
    #    i :   coordenada x, corresponde a la posición de cada barra en cada iteración. Anteriormente se ordenó los índices con las dificultades
    #    fila["tasa_exito"] +2 :  Obtenemos el valor de "tasa_exito" de la fila en la iteración actual como valor de la coordenada 'y' + 2 (altura de la barra + 2)
    #    f"{fila['tasa_exito']:.1f}%"  :  se imprime el valor de "tasa_exito" y se usa :.1f para darle formato con 1 decimal
    #    ha="center" :  se aplica centrado al texto
    #    fontsize=10:   se usa una fuente tamaño 10
    
    # Mostramos el gráfico
    plt.tight_layout()
    plt.show()
    print("")

# Se define una función que mostrará las estadísticas de victorias y perdidas por dificultad de un jugador al que se le pida su nombre
def estadistica_2(pd,plt):
    # Se carga el archivo excel y 
    archivo_excel = "Resultados_juego.xlsx"
    Hoja1 = "1 JG"
    # Se carga el dataframe
    datos = pd.read_excel(archivo_excel, sheet_name=Hoja1)
    # Se pide el nombre del jugador
    nombre_jugador = input("Ingrese su nombre/alias: ")
    
    # Obtenemos los datos del jugador al compararlo con los datos de la columna "nombre"
    datos_jugador = datos[datos["nombre"] == nombre_jugador]
    #Si no está registrado el jugador, mostrará un mensaje
    if datos_jugador.empty:
        print("No se encontraron datos para el jugador"+nombre_jugador)
    else:
        # Se hace un conteo de las estadísticas del jugador en las 3 dificultades. Para ello, primero se agrupa por la dificultad y acierto y se cuenta
        # la cantidad de veces que un dificultad tiene asignado un valor de acierto o no (0 o 1). Con unstack, tenemos los valores de aciertos como columnas
        # y los conteos como valores. Se usa el fill_value=0 porque puede que un jugador no hay jugado en alguna de las otras dificultades
        resumen = datos_jugador.groupby(["dificultad", "acierto"]).size().unstack(fill_value=0)
    
        # Definimos el orden en el que se verán las dificultades en el gráfico
        orden_dificultades = ["Fácil", "Medio", "Difícil"]
        # Se reordenan el df resumen, por el orden establecido de dificultades
        resumen = resumen.reindex(orden_dificultades, fill_value=0)
    
        # Crear el gráfico de barras agrupadas
        x = range(len(orden_dificultades))  # Índices para las dificultades
        ancho = 0.4  # Ancho de las barras
        # La configuración de las barras de victorias y derrotas
        plt.bar(
            [i - ancho / 2 for i in x],   #La barra se desplaza hacia la izquierda el ancho/2 para dibujarse y se repite x veces esta acción
            resumen[1],  # Columnas de victorias
            width=ancho, # El ancho de las columnas
            label="Victorias",  #El título debajo de la columna
            color="green",  # El color verde para victorias
        )
        # De forma análoga se configura las barras de derrotas
        plt.bar(
            [i + ancho / 2 for i in x],   #La barra se desplaza hacia la derecha el ancho/2 para dibujarse
            resumen[0],  # Columnas de derrotas
            width=ancho,
            label="Derrotas",
            color="red",
        )
    
        # Se configura el gráfico
        plt.xticks(x, orden_dificultades) # Aquí colocamos los nombres de las dificultades de cada grupo de barras. x el índice de la ubicación del par
                                          # y orden_dificultades tiene los nombres en el orden de izquierda a derecha
        plt.xlabel("Dificultad") # Indicamos el nombre del eje x
        plt.ylabel("Número de partidas") # Indicamos el nombre del eje y
        plt.title(f"Resultados de {nombre_jugador}") # Indicamos el título del gráfico
        plt.legend()  #Mostramos la leyenda de victorias y derrotas
    
        # Aquí mostramos los valores encima de las barras
        for i, dificultad in enumerate(orden_dificultades):
            plt.text(i - ancho / 2, resumen.at[dificultad, 1], resumen.at[dificultad, 1], ha="center", fontsize=10)
            plt.text(i + ancho / 2, resumen.at[dificultad, 0], resumen.at[dificultad, 0], ha="center", fontsize=10)
    
        # Mostramos el gráfico ajustado
        plt.tight_layout()
        plt.show()
        print("") # Un espacio para que reaparezca el menú principal

# Función para mostrar una estadística general de victorias de los jugadores 1 vs los jugadores 2
def estadistica_3(pd,plt):
    # Leemos los datos y la hoja
    archivo_excel = "Resultados_juego.xlsx"  # Nombre del archivo
    datos = pd.read_excel(archivo_excel, sheet_name="2 JG")
    
    # Agrupamos los datos por los aciertos y se cuentan
    victorias = datos.groupby("acierto").size()
    victorias.index = ["Jugador 1", "Jugador 2"]  # Cambiamos los nombres de los índices para mostrarlos más legibles
    
    # Configuramos las barras
    plt.figure(figsize=(6, 4))
    plt.bar(victorias.index, victorias.values, color=["red", "green"], width=0.6)
    
    # Configuramos el cuadro
    plt.title("Victorias por jugador", fontsize=14)
    plt.ylabel("Cantidad de victorias", fontsize=12)
    plt.xlabel("Jugador", fontsize=12)
    plt.ylim(0, victorias.max() + 1)  # Ajustar el límite superior del eje Y
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    
    # Colocamos los valores sobre las barras, similar a como se hizo con el modo solitario
    for i, valor in enumerate(victorias.values):
        plt.text(i, valor + 0.1, str(valor), ha="center", fontsize=10)
    
    # Ajustamos y mostramos el gráfico
    plt.tight_layout()
    plt.show()

# Función para registrar los resultados de una partida en una hoja de excel
def registrar_excel(registro, excel, Hoja, dificultad):
    registro=list(registro)
    registro.append(dificultad)
    Hoja.append(registro)
    excel.save('Resultados_juego.xlsx')