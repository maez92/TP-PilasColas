# -*- coding: utf-8 -*-
"""TP Pilas y colas - Matias Monteagudo y Florencia Dias

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17cWZCgdPFR4kTsFNMvmWb1L3uA16YX3I

# Implementación del TDA GeneroLibro
"""

from enum import Enum

class GeneroLibro(int,Enum):
  Teatro = 0
  Poesia = 1
  Narracion = 2

Teatro = GeneroLibro.Teatro
Poesía = GeneroLibro.Poesia
Narración = GeneroLibro.Narracion

print('Nombre:',Teatro.name)
print('Valor:',Teatro.value)
print('Tipo:',Teatro)

"""# Implementación del TDA TipoLibro"""

from enum import Enum

class TipoLibro(int,Enum):  
  Nacional= 0
  Internacional = 1

Internacional = TipoLibro.Internacional
Nacional = TipoLibro.Nacional

print('Tipo:',Internacional)
print('Nombre:',Internacional.name)

"""# Implementación del TDA Libro"""

class Libro():
  def __init__(self, codigo, genero, nacionalidadDeAutor, nombre = None):
    self.codigo = validaCodigo(codigo)
    self.genero = validaGenero(genero)
    self.nacionalidadDeAutor = validaNacionalidad(nacionalidadDeAutor)
    self.nombre = nombre

  def __repr__(self):
    if self.nombre:
      cadenaPrint = str(self.nombre)
    else:
      cadenaPrint = str(self.codigo)
    return cadenaPrint

  def nacionalidadDeAutor(self):
    return self.nacionalidadDeAutor

  def genero(self):
    return self.genero

  def codigo(self):
    return self.codigo

def validaCodigo(codigo):
  if codigo[0:3].isalpha() and codigo[3:8].isnumeric() and len(codigo) == 8:
    return codigo
  else:
    raise Exception('El codigo "' + str(codigo) + '" invalido, el codigo debe estar compuesto por 3 letras y 5 números')

def validaGenero(genero):
  if isinstance(genero,GeneroLibro):
    return genero
  else:
    raise Exception( 'El genero "' + str(genero) + '" invalido, el genero debe ser GeneroLibro.Teatro / GeneroLibro.Poesia / GeneroLibro.Narración')

def validaNacionalidad(tipoNacionalidad):
  if isinstance(tipoNacionalidad,TipoLibro):
    return tipoNacionalidad
  else:
    raise Exception( 'El tipo nacionalidad "' + str(tipoNacionalidad) + '" invalido, el tipo de nacionalidad debe ser TipoLibro.Nacional / TipoLibro.Internacional')

"""# Implementación del TDA Pila"""

class Pila:
  def __init__(self,elemento = None):
    self.pila = []
    if elemento:
      for valor in elemento:
        self.pila.append(valor)

  def vaciarPila(self):
    for elemento in range(len(self.pila)):
      self.pila.pop()

  def apilar(self,elemento):
    self.pila.append(elemento)

  def desapilar(self):
    if not self.esVacía():
      return self.pila.pop()

  def obtener(self):
    return self.pila[len(self.pila) -1]

  def clonarPila(self):
    clonDePila = Pila()
    for elemento in self.pila:
      clonDePila.apilar(elemento)
    return clonDePila

  def tamaño(self):
    return len(self.pila)

  def esVacía(self):
    return len(self.pila) == 0
    
  def __repr__(self):
    return str(self.pila)

"""# Implementación del TDA Estanteria"""

class Estanteria():
  def __init__(self,nroDeEstanteria, cantidadCritica=50, pilaDeLibros=None):
    self.nroDeEstanteria = validaNroEstanteria(nroDeEstanteria)
    self.cantidadCritica = validaCantidadCritica(cantidadCritica)
    self.pilaDeLibrosNacionales = Pila()
    self.pilaDeLibrosInternacionales = Pila()
    if pilaDeLibros:
      for libro in pilaDeLibros:
        self.guardarLibro(libro)

  def __repr__(self):
    cadenaPrint = 'E' + str(self.nroDeEstanteria) + '(N:' + str(self.pilaDeLibrosNacionales.tamaño()) \
                  + ',I:' + str(self.pilaDeLibrosInternacionales.tamaño()) + ',CC:' + str(self.cantidadCritica) + ')'
    return cadenaPrint
  
  def cantidadTotalDeLibros(self):
    tamaño = self.pilaDeLibrosNacionales.tamaño() + self.pilaDeLibrosInternacionales.tamaño()
    return tamaño

  def esCritica(self):
    return self.pilaDeLibrosNacionales.tamaño() > self.cantidadCritica or self.pilaDeLibrosInternacionales.tamaño() > self.cantidadCritica

  def guardarLibro(self,libro):
    if not self.esCritica():
      if libro.nacionalidadDeAutor == Nacional:
        self.pilaDeLibrosNacionales.apilar(libro)
      elif libro.nacionalidadDeAutor == Internacional:
        self.pilaDeLibrosInternacionales.apilar(libro)
    else:
      if libro.nacionalidadDeAutor == Nacional:
        self.pilaDeLibrosNacionales.apilar(libro)
      elif libro.nacionalidadDeAutor == Internacional:
        self.pilaDeLibrosInternacionales.apilar(libro)
      print("Se guardo el libro pero la capacidad de la estanteria es critica")

  def primerLibroDisponible(self):
    primerLibro = None
    if not self.pilaDeLibrosNacionales.esVacía():
      primerLibro = self.pilaDeLibrosNacionales.obtener()
    elif not self.pilaDeLibrosInternacionales.esVacía():
      primerLibro = self.pilaDeLibrosInternacionales.obtener()
    return primerLibro
    
  def libroParaRecomendar(self, generoDeLibro):
    pilaDeLibrosNacionalesAux = self.pilaDeLibrosNacionales.clonarPila()
    pilaDeLibrosInternacionalesAux = self.pilaDeLibrosInternacionales.clonarPila()
    libroARevisarAhora = None
    libroRecomendado = None
    while not pilaDeLibrosNacionalesAux.esVacía() and not libroRecomendado:
      libroARevisarAhora = pilaDeLibrosNacionalesAux.desapilar()
      if libroARevisarAhora.genero == generoDeLibro:
        libroRecomendado = libroARevisarAhora
    while not pilaDeLibrosInternacionalesAux.esVacía() and not libroRecomendado:
      libroARevisarAhora = pilaDeLibrosInternacionalesAux.desapilar()
      if libroARevisarAhora.genero == generoDeLibro:
        libroRecomendado = libroARevisarAhora
    return libroRecomendado

  def buscarLibro(self,codigoLibro):
    pilaDeLibrosNacionalesAux = self.pilaDeLibrosNacionales.clonarPila()
    pilaDeLibrosInternacionalesAux = self.pilaDeLibrosInternacionales.clonarPila()
    libroARevisarAhora = None
    libroEncontrado = None
    while not pilaDeLibrosNacionalesAux.esVacía() and not libroEncontrado:
      libroARevisarAhora = pilaDeLibrosNacionalesAux.desapilar()
      if libroARevisarAhora.codigo == codigoLibro:
        libroEncontrado = libroARevisarAhora
    while not pilaDeLibrosInternacionalesAux.esVacía() and not libroEncontrado:
      libroARevisarAhora = pilaDeLibrosInternacionalesAux.desapilar()
      if libroARevisarAhora.codigo == codigoLibro:
        libroEncontrado = libroARevisarAhora
    return libroEncontrado

  def prestarLibro(self,codigoLibro):                                    # Desapila libros de la estanteria hasta encontrarlo, luego los vuelve a apilar excepto al que presto.
    pilaDeLibrosNacionalesDesapilados = Pila()
    pilaDeLibrosInternacionalesDesapilados = Pila()
    libroARevisarAhora = None
    libroAPrestar = None
    while not self.pilaDeLibrosNacionales.esVacía() and not libroAPrestar:        # Mientras no es vacia la pila original y no hay libro a prestar:
      libroARevisarAhora = self.pilaDeLibrosNacionales.desapilar()                # Desapila el ultimo libro y lo pone en la variable para revisarlo
      if libroARevisarAhora.codigo == codigoLibro:                                # Si el codigo del libro a revisar ahora coincide
        libroAPrestar = libroARevisarAhora                                        # Lo guarda en la variable de libro a prestar
      else:                                                                       # Sino
        pilaDeLibrosNacionalesDesapilados.apilar(libroARevisarAhora)              # Lo guarda en la variable de libros apilados
    while not pilaDeLibrosNacionalesDesapilados.esVacía():                        # Mientras no esta vacía la pila de libros desapilados:
      libroQueApilar = pilaDeLibrosNacionalesDesapilados.desapilar()              # Desapila un libro de la variable auxiliar en una variable para apilar
      self.pilaDeLibrosNacionales.apilar(libroQueApilar)                          # y lo vuelve a apilar en la pila original.
    while not self.pilaDeLibrosInternacionales.esVacía() and not libroAPrestar:
      libroARevisarAhora = self.pilaDeLibrosInternacionales.desapilar()
      if libroARevisarAhora.codigo == codigoLibro:
        libroAPrestar = libroARevisarAhora
      else:
        pilaDeLibrosInternacionalesDesapilados.apilar(libroARevisarAhora)
    while not pilaDeLibrosInternacionalesDesapilados.esVacía():
      self.pilaDeLibrosInternacionales.apilar(pilaDeLibrosInternacionalesDesapilados.desapilar())
    return libroAPrestar

  def librosPorTipo(self):
    librosNacionalesAux = self.pilaDeLibrosNacionales.clonarPila()
    librosInternacionalesAux = self.pilaDeLibrosInternacionales.clonarPila()
    cantidadNacionales = 0
    cantidadInternacionales = 0
    while not librosNacionalesAux.esVacía():
      librosNacionalesAux.desapilar()
      cantidadNacionales += 1
    while not librosInternacionalesAux.esVacía():
      librosInternacionalesAux.desapilar()
      cantidadInternacionales += 1
    return cantidadNacionales,cantidadInternacionales

  def librosPorGenero(self,generoLibro):
    librosNacionalesAux = self.pilaDeLibrosNacionales.clonarPila()
    librosInternacionalesAux = self.pilaDeLibrosInternacionales.clonarPila()
    cantidadDeLibros = 0
    while not librosNacionalesAux.esVacía():
      libroAMirar = librosNacionalesAux.desapilar()
      if libroAMirar.genero == generoLibro:
        cantidadDeLibros += 1
    while not librosInternacionalesAux.esVacía():
      libroAMirar = librosInternacionalesAux.desapilar()
      if libroAMirar.genero == generoLibro:
        cantidadDeLibros += 1
    return cantidadDeLibros

  def nroEstanteria(self):
    return self.nroDeEstanteria

  def porcentajeOcupaciónNacional(self):
    return int( int(self.pilaDeLibrosNacionales.tamaño()) * 100 // int(self.cantidadCritica) )
  
def validaNroEstanteria(nroDeEstanteria):
  if isinstance(nroDeEstanteria,int) and nroDeEstanteria <= 999:
    return nroDeEstanteria
  else:
    raise Exception('El número de estanteria debe estar comprendido entre 0 y 999')

def validaCantidadCritica(cantidadCritica):
  if isinstance(cantidadCritica,int):
    return cantidadCritica
  else:
    raise Exception('La cantidad critica debe ser un número entero.')

"""# Implementación del TDA Cola"""

class Cola:
  def __init__(self,elemento = None):
    self.cola = []
    if elemento:
      for dato in elemento:
        self.cola.append(dato)

  def vaciar(self):
    for elemento in range(len(self.cola)):
      self.cola.pop()

  def encolar(self,elemento):
    self.cola.insert(0,elemento)

  def desencolar(self):
    if not len(self.cola) == 0:
      return self.cola.pop()

  def obtener(self):
    return self.cola[self.tamañoCola() -1]

  def clonar(self):
    listaAux = []
    for elemento in self.cola:
      listaAux += [elemento]
    clonDeCola = Cola(listaAux)
    return clonDeCola

  def tamañoCola(self):
    return len(self.cola)

  def esVacía(self):
    return len(self.cola) == 0

  def __repr__(self):
    return str(self.cola)

"""# Implementación del TDA EscritorioDeAtención"""

import numpy as np
 
class EscritorioDeAtencion():
  def __init__(self,cantidadDeFilas,cantidadDeColumnas):
    self.deposito = np.zeros([cantidadDeFilas,cantidadDeColumnas],dtype=object)
    for nroFila in range(cantidadDeFilas):
      for nroColumna in range(cantidadDeColumnas):
        self.deposito[nroFila,nroColumna] = None
 
  def __repr__(self):
    return str(self.deposito)
 
  def establecerEstanteria(self,nroFila, nroColumna, estanteria):
    self.deposito[nroFila,nroColumna] = estanteria

  def cantidadDeEstanteriasCriticas(self,nroFila,nroColumna=0):
    cantidadDefilas,cantidadDeColumnas = self.deposito.shape
    if nroColumna == cantidadDeColumnas-1:
      if self.deposito[nroFila,nroColumna] and self.deposito[nroFila,nroColumna].esCritica():
        estanteriasCriticas = 1
      else:
        estanteriasCriticas = 0
    else:
      if self.deposito[nroFila,nroColumna] and self.deposito[nroFila,nroColumna].esCritica():
        estanteriasCriticas = 1 + self.cantidadDeEstanteriasCriticas(nroFila,nroColumna +1)
      else:
        estanteriasCriticas = 0 + self.cantidadDeEstanteriasCriticas(nroFila,nroColumna +1)
    return estanteriasCriticas

  def estanteriaMenosRecargada(self):
    nroFila,nroColumna = self.deposito.shape
    mejorEstanteriaFila,mejorEstanteriaColumna = None,None
    mejorPorcentajeOcupación = 100
    for posFila in range(nroFila):
      for posColumna in range(nroColumna):
        if self.deposito[posFila,posColumna]:
          if self.deposito[posFila,posColumna].porcentajeOcupaciónNacional() < mejorPorcentajeOcupación:
            mejorPorcentajeOcupación = self.deposito[posFila,posColumna].porcentajeOcupaciónNacional() 
            mejorEstanteriaFila,mejorEstanteriaColumna = posFila,posColumna
    return mejorEstanteriaFila,mejorEstanteriaColumna

  def buscaEstanteria(self,nroEstanteria):
    nroFila,nroColumna = self.deposito.shape
    resultadoFila,resultadoColumna = None,None
    for posFila in range(nroFila):
      for posColumna in range(nroColumna):
        if self.deposito[posFila,posColumna] and self.deposito[posFila,posColumna].nroEstanteria() == nroEstanteria:
          resultadoFila,resultadoColumna = posFila,posColumna
    return resultadoFila,resultadoColumna

  def guardarLibros(self,colaDeLibros):
    while not colaDeLibros.esVacía():
      self.deposito[self.estanteriaMenosRecargada()].guardarLibro(colaDeLibros.desencolar())

  def sacarLibros(self,colaDeLibros):
    nroFila,nroColumna = self.deposito.shape
    colaCodigos = colaDeLibros.clonar()
    colaEncontrados = Cola()
    for posFila in range(nroFila):
      for posColumna in range(nroColumna):
        cantidadDeCodigosABuscarAcá = colaCodigos.tamañoCola()
        while self.deposito[posFila,posColumna] and cantidadDeCodigosABuscarAcá > 0:
          libroEncontrado = self.deposito[posFila,posColumna].buscarLibro(colaCodigos.obtener())
          if libroEncontrado:
            colaEncontrados.encolar(libroEncontrado)
            colaCodigos.desencolar()
            libroEncontrado = None
          else:
            codigoNoEncontrado = colaCodigos.desencolar()
            colaCodigos.encolar(codigoNoEncontrado)
          cantidadDeCodigosABuscarAcá -= 1
    return colaEncontrados

  def moverLibro(self,codigoLibro, nroEstanteriaOrigen, nroEstanteriaDestino):
    nroFila,nroColumna = self.deposito.shape
    libroAMover = None
    for posFila in range(nroFila):
      for posColumna in range(nroColumna):
        if self.deposito[posFila,posColumna] and self.deposito[posFila,posColumna].nroEstanteria() == nroEstanteriaOrigen:
          libroAMover = self.deposito[posFila,posColumna].prestarLibro(codigoLibro)
    for posFila in range(nroFila):
      for posColumna in range(nroColumna):
        if libroAMover and self.deposito[posFila,posColumna] and self.deposito[posFila,posColumna].nroEstanteria() == nroEstanteriaDestino:
          self.deposito[posFila,posColumna].guardarLibro(libroAMover)

"""# Entrega
La entrega del trabajo práctico debe ser:

Un informe escrito (doc, pdf. etc), incluyendo:

Descripción de cada una de las estructuras de datos diseñadas e implementadas.
Incluir una descripción escrita de los algoritmos. Pueden incluir diagramas de fujo.

Descripción de la implementación en Python. Explicar claramente que hace cada función y procedimiento implementados.

Código completo y comentado de la implementación.

Opcional: Video explicando cómo funciona el algoritmo.
"""
