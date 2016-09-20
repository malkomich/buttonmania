#!/usr/bin/python
# -*- coding: utf-8 -*-

#.......................................................#
#               Grupo de laboratorio : L3               #
#               Gonz√°lez Cabrero, Juan Carlos           #
#               Marciel Mateos, Tania                   #
#.......................................................#

import random
import gtk
VECT=20

class Interfaz():
        """ 
                Clase responsable de la interfaz
        """
        def __init__(self):
                """ Inicializaci√≥n """
                # Cargamos la interfaz generada con glade
                self.glade=gtk.Builder()
                self.glade.add_from_file('buttonmania.glade')
                # Podemos extraer algunos de los objetos que forman la interfaz
                # Utilizamos para ello el nombre que identifica al widget en glade
                self.ventana=self.glade.get_object('window1')
                self.ayuda=self.glade.get_object('ayuda')
                self.niveles=self.glade.get_object('window2')
                self.rank=self.glade.get_object('dialog2')
                self.meter_nombre=self.glade.get_object('dialog1')
		self.ventana_final=self.glade.get_object('window3')

        # La lista de los botones que aparecen dentro del tablero
                self.pulsadores=self.glade.get_object('table1').get_children()

		self.entradas_ranking=self.glade.get_object('vbox3').get_children()

        # Conectamos todos los eventos descritos en la interfaz con sus
        # correspondientes manejadores. Cuando se active la se√±al (al pulsar
        # el bot√≥n, por ejemplo, se llamar√° al correspondiente m√©todo de
        # esta clase.
                self.glade.connect_signals(self)

        # Si no hemos hecho visible la ventana desde glade, podemos hacerlo
        # desde el c√≥digo
                self.ventana.show()
                self.tablero=Tablero()
                self.tablero.inicializar()
                self.album={0:"0.png",1:"1.png",2:"2.png",3:"3.png"}
        # Tambi√©n podemos cambiar la etiqueta e imagen que aparecen en el bot√≥n
                for i in range(len(self.pulsadores)):
                        imagen=gtk.Image()
                        imagen.set_from_file(self.album[self.tablero.matriz[(35-i)//6][(35-i)%6]])
                        self.pulsadores[i].set_image(imagen)
                        self.pulsadores[i].set_label("")
            
                self.niveles.show()


        def nuevo_juego(self,widget):
		""" Muestra la ventana de niveles de juego """
                print "Ventana de niveles"
                self.niveles.show()

        def on_cancelar1_clicked(self,widget):
		""" Boton de cancelar en la ventana de nivel, con el cual sale de dicha ventana """
                print "Cancelada la selecci¬¥on de nivel"
                self.niveles.hide()
		self.ventana_final.show()

        def on_aceptar1_clicked(self,widget):
		""" Boton de aceptar en la ventana de nivel, al pulsarlo crea un nuevo juego segun el nivel introducido """
                nivel=self.glade.get_object('spinbutton1').get_text()
		#Aqu√ hay un error, ya que aunque valga 0 se cierra la ventana
		if (nivel!=0):
                  self.tablero=Tablero()
                  self.tablero.inicializar()
                  self.tablero.IniciarJuego(nivel)
		  # Se puede colocar una imagen
		  # Pero hay que crear una nueva para cada bot√≥n
                  for i in range(len(self.pulsadores)):
                       	imagen=gtk.Image()
                       	imagen.set_from_file(self.album[self.tablero.matriz[(35-i)//6][(35-i)%6]])
                       	self.pulsadores[i].set_image(imagen)
		  self.niveles.hide()
        
        def on_window1_delete_event(self,widget,event):
                """ Gesti√≥n del borrado de la ventana principal """
                # Para los eventos adem√°s del widget nos env√≠an el evento
                # Este evento contiene informaci√≥n extra sobre lo que ha ocurrido en
                # la ventana (tecla pulsada, bot√≥n pulsado,...)
                print "Se√±al para cerrar la ventana"
                gtk.main_quit()
                # Si no devolvemos nada, el evento no se considera procesado, se
                # retransmite y acaba siendo una destrucci√≥n de la ventana. Si
                # quisieramos evitar la destrucci√≥n de la ventana. (mediante una
                # ventana para pedir informaci√≥n, por ejemplo) habr√≠a que devolver
        # True
                print "Fuera del bucle de control de eventos"

        def on_ayuda_activado(self,widget):
                """ Gesti√≥n del bot√≥n de ayuda """
                print "Ayuda"
                self.ayuda.show()

        def on_ayuda_response(self,widget,event):
                """ Gesti√≥n del cierre del di√°logo de ayuda """
                # Han pulsado el bot√≥n close del di√°logo de ayuda
        # o han cerrado la ventana de ayuda con el aspa
                print "Cerrando ayuda"
                self.ayuda.hide()

        def on_ayuda_delete_event(self,widget,event):
                """ Gesti√≥n de la destrucci√≥n del di√°logo de ayuda """
        # Intentan destruir el di√°logo de ayuda
                print "No destruyo el di√°logo de ayuda"
        # Si no devuelves True, el evento se transforma en un evento destroy
        # que elimina la ventana, al volver a pedir ayuda aparecer√° un
        # error.
                return True

        def on_pulsador_clicked(self,widget):
                """ Gesti√≥n de la pulsaci√≥n de alguno de lo36 botones de la caja """
        # Un √∫nico manejador para todos los botones. Podemos distinguir el
        # bot√≥n pulsado porque nos pasan el widget, de modo que lo
        # comparamos con los de la lista pulsadores
                print "Click sobre el pulsador",
                for i in range(len(self.pulsadores)):
                        if self.pulsadores[i]==widget:
                # Pero ojo, porque los pulsadores han entrado en orden
                # inverso
                                print 35-i,
                # Una sencilla f√≥rmula permite deducir sus coordenadas
                                print "esto es el pulsador (", 
                                print (35-i)//6+1,
                                print ",",
                                print (35-i)%6+1,
                                print ")"
                                print (35-i)//6+1
                                print (35-i)%6+1
                                self.tablero.GolpeDirecto((35-i)//6,(35-i)%6)
                                self.tablero.GuardarMovimiento((35-i)//6,(35-i)%6)
                for i in range(len(self.pulsadores)):
                        # Actualizamos las im√°enes en cada bot√n
                        imagen=gtk.Image()
                        imagen.set_from_file(self.album[self.tablero.matriz[(35-i)//6][(35-i)%6]])
                        self.pulsadores[i].set_image(imagen)
                        self.pulsadores[i].set_label("")
		self.tablero.ComprobarResuelto()
                if self.tablero.resuelto:
                        self.meter_nombre.show()

        def deshacer_movimiento(self,widget):
		""" Elimina el √ltimo movimiento realizado, actualizando el vector donde guardamos los movimientos """
                self.tablero.Deshacer()
		# Aqu√≠tambi√©nactualizamos las im√genes de los botones 
                for i in range(len(self.pulsadores)):
                        imagen=gtk.Image()
                        imagen.set_from_file(self.album[self.tablero.matriz[(35-i)//6][(35-i)%6]])
                        self.pulsadores[i].set_image(imagen)
                        self.pulsadores[i].set_label("")

        def mostrar_ranking(self,widget):
		""" Muestra la ventana d√nde se registran las puntuaciones """
                print "Mostrar Ranking"
                self.tablero.fich=open("ranking.txt","r")
		i=0
		salir=False
		lineas=1
		while (not salir) or (lineas<=10) :
		  archivo=self.tablero.fich.readline().strip()
		  if len(archivo) !=0:
                    self.entradas_ranking[i].set_text(archivo)
		    i+=1
		  lineas+=1
		  if not archivo:
		    salir=True
		self.tablero.fich.close()
                self.rank.show()
		self.ventana_final.hide()
        
        def on_cancelar2_clicked(self,widget):
		""" Bot√n de cancelar en la ventana de introducci√n del nombre, evitando guardar la puntuaci√n """
		self.ventana_final.show()
		self.meter_nombre.hide()

        def on_aceptar2_clicked(self,widget):
		""" Bot√≥n de aceptar en la ventana de introducci√n del nombr, guardando √ste junto con la puntuaci√n obtenida en caso de que no exista el nombre del jugador con una puntuaci√n mayor """
		nombre=self.glade.get_object('nom').get_text()
                nivel=self.glade.get_object('spinbutton1').get_digits()
                self.tablero.CrearRanking(nivel,nombre)
		self.ventana_final.show()
                self.meter_nombre.hide()
	
	def on_limpiar_clicked(self,widget):
		""" Elimina del fichero de ranking todas las puntuaciones registradas """
		self.tablero.fich=open("ranking.txt","w")
		self.tablero.fich.write("")
		self.tablero.fich.close()
		for i in range(10):
			self.entradas_ranking[i].set_text("")

	def on_dialog2_delete_event(self,widget,event):
		""" Cierra la ventana de ranking """
		self.ventana_final.show()
		self.rank.hide()
		return True

        def nuevo_juego_2(self,widget):
		""" Muestra la ventana de niveles de juego """
		print "Ventana de niveles"
		self.niveles.show()
		self.ventana_final.hide()
		return True


class Tablero():
  """
    Clase responsable de la creaciÔøΩn y modificaciÔøΩn de la matriz del juego
  """
  def __init__(self):
    """ Inicializaci√n de la clase Tablero """
    self.filas=7
    self.columnas=7
    self.matriz=[]
    self.vector=[]
    self.golpes=0
    for i in range(VECT):
      self.vector.append([0,0])

  def IniciarJuego (self,nivel):
    """ Introduce valores a posiciones aleatorias en la matriz, seg√n el nivel introducido """
    i=0
    while i<(int(nivel)*3):
      x=random.randrange(1,6,1)
      y=random.randrange(1,6,1)
      self.GolpeInverso(x,y)
      i+=1

  def inicializar(self):
    """ Iguala todos los valores de la matriz a cero """
    i=0
    j=0
    while i<=self.filas:
      self.matriz.append([])
      while j<=self.columnas:
        self.matriz[i].append(0)
        j+=1
      i+=1
      j=0
  
  def GolpeDirecto(self,x,y):
    """ Resta 1, o se iguala a 3 si vale 0, a cada posici√n de la matriz con la que se interact√a y a las posiciones adyacentes """
    self.golpes+=1
    if self.matriz[x][y]==0:
      self.matriz[x][y]=3 
    else: 
      self.matriz[x][y]-=1
    if self.matriz[x-1][y]==0:
      self.matriz[x-1][y]=3 
    else:
      self.matriz[x-1][y]-=1
    if self.matriz[x+1][y]==0:
      self.matriz[x+1][y]=3 
    else:
      self.matriz[x+1][y]-=1
    if self.matriz[x][y-1]==0:
      self.matriz[x][y-1]=3 
    else:
      self.matriz[x][y-1]-=1
    if self.matriz[x][y+1]==0:
      self.matriz[x][y+1]=3
    else:
      self.matriz[x][y+1]-=1
    #Muestra matriz por consola, s√lo para comprobaci√n
    i=0
    j=0
    while i < self.filas:
      while j< self.columnas:
        print self.matriz [i][j],
        j+=1
      print 
      j=0
      i+=1

  def GolpeInverso(self,x,y):
    """ Suma 1, o se iguala a 0 si vale 3, a cada posici√n de la matriz a la que afecta y a las posiciones adyacentes """
    if self.matriz[x][y]==3:
      self.matriz [x][y]=0 
    else: 
      self.matriz [x][y]+=1
    if self.matriz[x-1][y]==3:
      self.matriz [x-1][y]=0 
    else:
      self.matriz [x-1][y]+=1
    if self.matriz[x+1][y]==3:
      self.matriz [x+1][y]=0 
    else:
      self.matriz [x+1][y]+=1
    if self.matriz[x][y-1]==3:
      self.matriz [x][y-1]=0 
    else:
      self.matriz [x][y-1]+=1
    if self.matriz[x][y+1]==3:
      self.matriz [x][y+1]=0 
    else:
      self.matriz [x][y+1]+=1

  def GuardarMovimiento(self,x,y):
    """ Introduce en una lista las coordenadas del √ltimo golpe realizado """
    i=VECT-1
    while i>0:
      self.vector[i] =self.vector[i-1]
      i-=1
    self.vector[0] = [x,y]

  def Deshacer (self):
    """ Elimina de la lista de movimientos el primer dato, que son las coordenadas del √ltimo golpe realizado """
    self.GolpeInverso(self.vector[0][0],self.vector[0][1])
    self.golpes-=1
    i=1
    while i<VECT:
      self.vector[i-1] = self.vector[i]
      i+=1

  def ComprobarResuelto(self):
    """ Recorre todas las posiciones relevantes de la matriz, para comprobar si todas valen 0 """
    self.resuelto=False
    resueltos=0
    for i in range(6):
      for j in range(6):
        if self.matriz[i][j]==0:
          resueltos+=1
    if resueltos==36:
      self.resuelto=True
      print "Enhorabuena, ha terminado el juego en "+str(self.golpes)+" golpes"

  def CrearRanking(self,nivel,nombre):
    """ Crea un fichero de texto que guarda los nombres y puntuaciones de los jugadores """
    puntuacion=int((float(nivel*3)/float(self.golpes))*10)
    lista_fich=[]
    try:
      self.fich=open("ranking.txt","r")
      encontrado=False
      salir=False
      while not salir:
        linea=self.fich.readline()
	if linea!="\n":
    	  	lista_fich.append(linea)
        	cadenas=linea.split("\t")
        if cadenas[0]==nombre:
	  encontrado=True
	  if puntuacion>=int(cadenas[1]):
	    lista_fich[-1]=(nombre+"\t"+str(puntuacion))
	if not linea:
	  salir=True
      self.fich.close()
      self.fich=open("ranking.txt","w")
      for i in range(len(lista_fich)):
        lista_fich[i].replace("\n","")
        self.fich.write(lista_fich[i]+"\n")
      if not encontrado:
        self.fich.write(nombre+"\t"+str(puntuacion)+"\n")
      self.fich.close()
      print 1
      self.OrdenarRanking()
      print 2
    except:
      self.fich=open("ranking.txt","w")
      self.fich.write(nombre+"\t"+str(puntuacion))
      self.fich.close()

  def OrdenarRanking(self):
  	""" 
		Accede al fichero de ranking creado para ordenar las lineas seg√n la puntuaci√n 
	"""
  	lista=[]
  	self.fich=open("ranking.txt", "r")
	salir=False
  	while not salir:
	  linea=self.fich.readline()
	  cadenas=linea.split("\t")
	  if len(cadenas)>1:
	    lista.append((str(cadenas[1]))+"\t"+(str(cadenas[0])))
	  if not linea:
	    salir=True
  	self.fich.close()
	lista.sort()
	self.fich=open("ranking.txt","w")
	while len(lista)>0:
	  cadenas=lista[0].split("\t")
	  self.fich.write((str(cadenas[1]))+"\t"+(str(cadenas[0])))
	  lista.pop(0)
	self.fich.close()


# Para lanzar la aplicaci√≥n.
if __name__=='__main__':
    # Instanciamos la interfaz
    app=Interfaz()
    # Lanzamos el bucle de gesti√≥n de eventos
    gtk.main()
    print "Termina el programa"
