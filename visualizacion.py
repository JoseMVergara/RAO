#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 22:58:15 2019

@author: josevergara
"""
import tkinter as tk
import romanos
import numpy as np
from PIL import Image,ImageTk
import tkinter.messagebox as msj


class RevisionRespuestas(object):
    """
    Clase RevisionRespuestas
    Verifica cada una de las respuestas del juego 'Rumbo Al Olimpo' a partir 
    del nivel 3
    Entradas: 
        nivel: nivel actual del juego
        textoIngresado: respuesta ingresada por el usuario
    Salida:
        SiguienteNivel: Proporciona información (True o False) sobre la respuesta
        del usuario. True- respuesta correcta, False-respuesta Incorrecta. 
    """
    
    def __init__(self,nivel,textoIngresado):
        self.nivel = nivel
        self.textoIngresado = textoIngresado
        self.romano = romanos.Romano(self.textoIngresado)
        
    def revision(self):
        if self.nivel == 3:
            siguienteNivel = self.revisionNivelTres()
        if self.nivel == 4:
            siguienteNivel = self.revisionNivelCuatro()
        if self.nivel==5:
            siguienteNivel = self.revisionNivelCinco()
        if self.nivel==6:
            siguienteNivel = self.revisionNivelSeis()
        if self.nivel==7:
            siguienteNivel = self.revisionNivelSiete()
        if self.nivel==8:
            siguienteNivel = self.revisionNivelOcho()
        return siguienteNivel
    
    def suma(self,textoIngresado):
        divisionTextoIngresado = textoIngresado.split("+")
        return divisionTextoIngresado
    def resta(self,textoIngresado):
        divisionTextoIngresado = textoIngresado.split("-")
        return divisionTextoIngresado
    def operacion(self):
        textoIngresadoSuma = self.suma(self.textoIngresado) 
        total = 0
        self.terminos = 0
        self.terminosNivelOcho = []
        for termino in textoIngresadoSuma:
            try:
                self.terminos += 1
                romano = romanos.Romano(termino)
                total += romano.romanoAArabigo()
                self.terminosNivelOcho+=[romano.romanoAArabigo]
                
            except:
                self.terminos += 2
                textoIngresadoResta = self.resta(termino)
                primerRomano = romanos.Romano(textoIngresadoResta[0])
                segundoRomano = romanos.Romano(textoIngresadoResta[1])
                total += primerRomano.romanoAArabigo()-segundoRomano.romanoAArabigo()
                self.terminosNivelOcho+=[primerRomano.romanoAArabigo(),segundoRomano.romanoAArabigo()]
        
        return total
        
    def revisionNivelTres(self):
        try:
            numeroIngresado = self.romano.romanoAArabigo()
        except:
            siguienteNivel = False
            return siguienteNivel
        if numeroIngresado == 365:
            siguienteNivel = True
        else:
            siguienteNivel = False
        return siguienteNivel
    
    def revisionNivelCuatro(self):
        try:
            numeroIngresado = self.romano.romanoAArabigo()
        except:
            siguienteNivel = False
            return siguienteNivel
        if numeroIngresado == 3600:
            siguienteNivel = True
        else:
            siguienteNivel = False
        return siguienteNivel
    
    def revisionNivelCinco(self):
        try:
            numeroIngresado = self.romano.romanoAArabigo()
        except:
            siguienteNivel = False
            return siguienteNivel
        if numeroIngresado == 2:
            siguienteNivel = True
        else:
            siguienteNivel = False
        return siguienteNivel
    
    def revisionNivelSeis(self):
        try:
            valorIngresado = self.operacion()
        except:
            siguienteNivel = False
            return siguienteNivel
        if valorIngresado == 1155 and self.terminos>1:
            siguienteNivel = True
        else:
            siguienteNivel = False
        return siguienteNivel
    
    def revisionNivelSiete(self):
        try:
            valorIngresado = self.operacion()
        except:
            siguienteNivel = False
            return siguienteNivel
        if valorIngresado == 10 and self.terminos>=5:
            siguienteNivel = True
        else:
            siguienteNivel = False
        return siguienteNivel
    
    def revisionNivelOcho(self):
        try:
            valorIngresado = self.operacion()
            nivelOcho = np.array(self.terminosNivelOcho)
        except:
            siguienteNivel = False
            return siguienteNivel
        if valorIngresado == 4 and len(nivelOcho[nivelOcho>500])==len(nivelOcho):
            siguienteNivel = True
        else:
            siguienteNivel = False
        return siguienteNivel
        
        
class Visualizacion(object):
    ''' 
        Establece GUI para aplicación Rumbo al Olimpo.
        
    '''
    def __init__(self):
        self.contador = 0
        self.test = 0

    def crearVentana(self,titulo):
        ventana = tk.Tk()
        ventana.title(titulo)
        ventana.geometry("1366x768+0+0")
        ventana.config(bg="#641403")
        return ventana
                    
                       
    def destruirVentana(self,ventana):
        if ventana:
            ventana.destroy()
            return ventana
                       
    def agregarImagenFondo(self,ventana,nombreImagen):
        imagen = Image.open(nombreImagen)
        anchoImagen, largoImagen = imagen.size
        canvasImagen = tk.Canvas(ventana, width= anchoImagen, height=largoImagen)
        canvasImagen.pack()

        imagenTk = tk.PhotoImage(file=nombreImagen)
        canvasImagen.create_image(anchoImagen/2.,largoImagen/2.,image=imagenTk)
        canvasImagen.image = imagenTk
        return canvasImagen,anchoImagen,largoImagen
    
    def crearBoton(self,ventana,texto,comando,height=3,width=20):
        boton = tk.Button(ventana, text=texto,anchor='center'
                          ,compound='center',height=height,relief='ridge',width=width,
                          bg='#000000',fg='#FFEC8E',command=comando) 
        return boton
    
    def crearEntrada(self,ventana):
        self.textoEntrada = tk.StringVar()
        entrada = tk.Entry(ventana, font=('Comic Sans MS', 15, 'bold italic'),
                                     width=30,textvariable=self.textoEntrada,
                                     bd=4,insertwidth=4,
                                     justify="right")
        return entrada
    
    def ingresarTexto(self):
        textoIngresado = self.textoEntrada.get()
        siguienteNivel = RevisionRespuestas(self.nivel,textoIngresado).revision()
        
        if siguienteNivel==True:
            self.nivelSuperado()
        else:
            self.opcionIncorrecta()
        return textoIngresado
    
    def nivelSuperado(self):
        self.ventanaSuperada.destroy()
        self.ventanaNivelSuperado = self.crearVentana('Nivel Superado')
        canvas,ancho,largo=self.agregarImagenFondo(self.ventanaNivelSuperado,
                                                   self.imagen)
        boton = self.crearBoton(self.ventanaNivelSuperado,"Siguiente Nivel",
                                self.ventanaSiguienteNivel)
        botonVentana = canvas.create_window(ancho/2-500,largo-150,
                                            anchor='center',window=boton) 
        return self.ventanaNivelSuperado
        
    def opcionIncorrecta(self):
        self.contador += 1
        if self.contador > self.nivel:
            intentosRestantes = 0
            if self.test == 0:
                msj.showerror("Fin del juego","Te has quedado sin vidas",icon='error')
    
        else:
            intentosRestantes = self.nivel - self.contador + 1
            if self.test == 0:
                msj.showerror("Has perdido una vida",
                              "Te quedan %s intentos para este nivel"%str(intentosRestantes),
                              icon='warning')
        return intentosRestantes
        
    def ventanaPrincipal(self):
        self.ventanaInicial = self.crearVentana('Rumbo Al Olimpo')
        canvas,ancho,largo=self.agregarImagenFondo(self.ventanaInicial,"./images/VentanaPrincipal.ppm")
        boton = self.crearBoton(self.ventanaInicial,"Siguiente",self.ventanaIntro)
        botonVentana = canvas.create_window(ancho/2,largo-150,anchor='center',window=boton) 
    
        return self.ventanaInicial

    def ventanaIntro(self):
        self.destruirVentana(self.ventanaInicial)
        self.ventanaIntroduccion = self.crearVentana('Introducción')
        canvas,ancho,largo=self.agregarImagenFondo(self.ventanaIntroduccion,
                                                   "./images/VentanaIntro.ppm")
        boton = self.crearBoton(self.ventanaIntroduccion,"Iniciar Juego",
                                self.ventanaPrimerNivel)
        botonVentana = canvas.create_window(ancho/2,largo-100,anchor='center',
                                            window=boton)
        return self.ventanaIntroduccion
        

    def ventanaPrimerNivel(self):
        self.destruirVentana(self.ventanaIntroduccion)
        self.primerNivel = self.crearVentana('Nivel 1')
        self.nivel = 1
        canvas,ancho,largo=self.agregarImagenFondo(self.primerNivel,
                                                   "./images/ventanaPrimerNivel.ppm")
        
        primeraOpcion = self.crearBoton(self.primerNivel,"V",self.opcionIncorrecta)
        primeraOpcionVentana = canvas.create_window(ancho/4-130,largo-100,
                                        anchor='center',window=primeraOpcion)
        
        segundaOpcion = self.crearBoton(self.primerNivel,"XX",self.opcionIncorrecta)
        segundaOpcionVentana = canvas.create_window(ancho/3+60,largo-100,
                                        anchor='center',window=segundaOpcion)
        
        terceraOpcion = self.crearBoton(self.primerNivel,"L",self.opcionIncorrecta)
        terceraOpcionVentana = canvas.create_window(ancho/2+140,largo-100,
                                        anchor='center',window=terceraOpcion)
        
        self.ventanaSuperada = self.primerNivel
        self.ventanaSiguienteNivel = self.ventanaSegundoNivel
        self.imagen = "./images/PrimerNivelSuperado.ppm"
        cuartaOpcion = self.crearBoton(self.primerNivel,"X",self.nivelSuperado)
        cuartaOpcionVentana = canvas.create_window(ancho-220,largo-100,
                                        anchor='center',window=cuartaOpcion)
        self.opcionCorrecta = cuartaOpcion
        return self.primerNivel
        
    def ventanaSegundoNivel(self):
        self.contador = 0
        self.destruirVentana(self.ventanaNivelSuperado)
        self.segundoNivel = self.crearVentana('Nivel 2')
        self.nivel = 2
        canvas,ancho,largo=self.agregarImagenFondo(self.segundoNivel,
                                                   "./images/VentanaSegundoNivel.ppm")
        
        primeraOpcion = self.crearBoton(self.segundoNivel,"67",self.opcionIncorrecta)
        primeraOpcionVentana = canvas.create_window(ancho/4-100,largo-100,
                                        anchor='center',window=primeraOpcion)
        
        segundaOpcion = self.crearBoton(self.segundoNivel,"32",self.opcionIncorrecta)
        segundaOpcionVentana = canvas.create_window(ancho/3+70,largo-100,
                                        anchor='center',window=segundaOpcion)
        
        terceraOpcion = self.crearBoton(self.segundoNivel,"104",self.opcionIncorrecta)
        terceraOpcionVentana = canvas.create_window(ancho-290,largo-100,
                                        anchor='center',window=terceraOpcion)
        
        self.ventanaSuperada = self.segundoNivel
        self.ventanaSiguienteNivel = self.ventanaTercerNivel
        self.imagen = "./images/SegundoNivelSuperado.ppm"
        cuartaOpcion = self.crearBoton(self.segundoNivel,"54",self.nivelSuperado)
        cuartaOpcionVentana = canvas.create_window(ancho/2+100,largo-100,
                                        anchor='center',window=cuartaOpcion)
        self.opcionCorrecta = cuartaOpcion
        return self.segundoNivel
    
    def ventanaTercerNivel(self):
        self.contador = 0
        self.destruirVentana(self.ventanaNivelSuperado)
        self.tercerNivel = self.crearVentana('Nivel 3')
        self.nivel = 3
        canvas,ancho,largo=self.agregarImagenFondo(self.tercerNivel,
                                                   "./images/VentanaTercerNivel.ppm")
        entrada = self.crearEntrada(self.tercerNivel)
        entradaVentana = canvas.create_window(ancho/2,largo-300,anchor='center',
                                              window=entrada)
        
        self.ventanaSuperada = self.tercerNivel
        self.ventanaSiguienteNivel = self.ventanaCuartoNivel
        self.imagen = "./images/TercerNivelSuperado.ppm"
        
        botonIngresar = self.crearBoton(self.tercerNivel,"Ingresar",self.ingresarTexto) 
        botonIngresarVentana = canvas.create_window(ancho/2.,largo-200,anchor='center',
                                                         window=botonIngresar)
        return self.tercerNivel
        
    def ventanaCuartoNivel(self):
        self.contador = 0
        self.destruirVentana(self.ventanaNivelSuperado)
        self.cuartoNivel = self.crearVentana('Nivel 4')
        self.nivel = 4
        canvas,ancho,largo=self.agregarImagenFondo(self.cuartoNivel,
                                                   "./images/VentanaCuartoNivel.ppm")
        entrada = self.crearEntrada(self.cuartoNivel)
        entradaVentana = canvas.create_window(ancho/2,largo-200,anchor='center',
                                              window=entrada)
        
        self.ventanaSuperada = self.cuartoNivel
        self.ventanaSiguienteNivel = self.ventanaQuintoNivel
        self.imagen = "./images/CuartoNivelSuperado.ppm"
        
        botonIngresar = self.crearBoton(self.cuartoNivel,"Ingresar",self.ingresarTexto) 
        botonIngresarVentana = canvas.create_window(ancho/2.,largo-100,anchor='center',
                                                         window=botonIngresar)
        return self.cuartoNivel
    
    def ventanaQuintoNivel(self):
        self.contador = 0
        self.destruirVentana(self.ventanaNivelSuperado)
        self.quintoNivel = self.crearVentana('Nivel 5')
        self.nivel = 5
        canvas,ancho,largo=self.agregarImagenFondo(self.quintoNivel,
                                                   "./images/VentanaQuintoNivel.ppm")
        entrada = self.crearEntrada(self.quintoNivel)
        entradaVentana = canvas.create_window(ancho/2,largo-200,anchor='center',
                                              window=entrada)
        
        self.ventanaSuperada = self.quintoNivel
        self.ventanaSiguienteNivel = self.ventanaNivelSeis
        self.imagen = "./images/QuintoNivelSuperado.ppm"
        
        botonIngresar = self.crearBoton(self.quintoNivel,"Ingresar",self.ingresarTexto) 
        botonIngresarVentana = canvas.create_window(ancho/2.,largo-100,anchor='center',
                                                         window=botonIngresar)
        return self.quintoNivel
    
    def ventanaNivelSeis(self):
        self.contador = 0
        self.destruirVentana(self.ventanaNivelSuperado)
        self.sextoNivel = self.crearVentana('Nivel 6')
        self.nivel = 6
        canvas,ancho,largo=self.agregarImagenFondo(self.sextoNivel,
                                                   "./images/VentanaNivelSeis.ppm")
        entrada = self.crearEntrada(self.sextoNivel)
        entradaVentana = canvas.create_window(ancho/2,largo-200,anchor='center',
                                              window=entrada)
        
        self.ventanaSuperada = self.sextoNivel
        self.ventanaSiguienteNivel = self.ventanaNivelSiete
        self.imagen = "./images/NivelSeisSuperado.ppm"
        
        botonIngresar = self.crearBoton(self.sextoNivel,"Ingresar",self.ingresarTexto) 
        botonIngresarVentana = canvas.create_window(ancho/2.,largo-100,anchor='center',
                                                         window=botonIngresar)
        return self.sextoNivel
        
    def ventanaNivelSiete(self):
        self.contador = 0
        self.destruirVentana(self.ventanaNivelSuperado)
        self.septimoNivel = self.crearVentana('Nivel 7')
        self.nivel = 7
        canvas,ancho,largo=self.agregarImagenFondo(self.septimoNivel,
                                                   "./images/VentanaNivelSiete.ppm")
        entrada = self.crearEntrada(self.septimoNivel)
        entradaVentana = canvas.create_window(ancho/2,largo-200,anchor='center',
                                              window=entrada)
        
        self.ventanaSuperada = self.septimoNivel
        self.ventanaSiguienteNivel = self.ventanaNivelOcho
        self.imagen = "./images/NivelSieteSuperado.ppm"
        
        botonIngresar = self.crearBoton(self.septimoNivel,"Ingresar",self.ingresarTexto) 
        botonIngresarVentana = canvas.create_window(ancho/2.,largo-100,anchor='center',
                                                         window=botonIngresar)
        return self.septimoNivel
    
    def ventanaNivelOcho(self):
        self.contador = 0
        self.destruirVentana(self.ventanaNivelSuperado)
        self.ochoNivel = self.crearVentana('Nivel 8')
        self.nivel = 8
        canvas,ancho,largo=self.agregarImagenFondo(self.ochoNivel,
                                                   "./images/VentanaNivelOcho.ppm")
        entrada = self.crearEntrada(self.ochoNivel)
        entradaVentana = canvas.create_window(ancho/2,largo-200,anchor='center',
                                              window=entrada)
        
        self.ventanaSuperada = self.ochoNivel
        self.ventanaSiguienteNivel = self.comprarJuego
        self.imagen = "./images/NivelOchoSuperado.ppm"
        
        botonIngresar = self.crearBoton(self.ochoNivel,"Ingresar",self.ingresarTexto) 
        botonIngresarVentana = canvas.create_window(ancho/2.,largo-100,anchor='center',
                                                         window=botonIngresar)
    
        return self.ochoNivel
    
    def comprarJuego(self):
        self.contador = 0
        self.destruirVentana(self.ventanaNivelSuperado)
        self.comprar = self.crearVentana('Comprar Juego')
        self.nivel = 0
        canvas,ancho,largo=self.agregarImagenFondo(self.comprar,
                                                   "./images/ComprarJuego.ppm")        
        return self.comprar
        

if __name__=="__main__":
    App = Visualizacion()
    App.ventanaPrincipal().mainloop()   
        
        
                       
                                   