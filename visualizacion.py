#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 22:58:15 2019

@author: josevergara
"""
import tkinter as tk
from PIL import Image,ImageTk
import tkinter.messagebox as msj

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
    
    def nivelSuperado(self):
        self.ventanaSuperada.destroy()
        ventanaNivelSuperado = self.crearVentana('Nivel Superado')
        canvas,ancho,largo=self.agregarImagenFondo(ventanaNivelSuperado,
                                                   self.imagen)
        boton = self.crearBoton(ventanaNivelSuperado,"Siguiente Nivel",
                                self.ventanaSiguienteNivel)
        botonVentana = canvas.create_window(ancho/2-500,largo-150,
                                            anchor='center',window=boton) 
        
    def opcionIncorrecta(self):
        self.contador += 1
        if self.contador > self.nivel:
            intentosRestantes = 0
            if self.test == 0:
                msj.showerror("Fin del juego", "Te has quedado sin vidas",icon='error')
        else:
            intentosRestantes = self.nivel - self.contador + 1
            if self.test == 0:
                msj.showerror("Has perdido una vida",
                              "Te quedan %s intentos para este nivel"%str(intentosRestantes),
                              icon='warning')
        return intentosRestantes
        
    def ventanaPrincipal(self):
        self.ventanaInicial = self.crearVentana('Rumbo Al Olimpo')
        canvas,ancho,largo=self.agregarImagenFondo(self.ventanaInicial,
                                                   "./images/VentanaPrincipal.ppm")
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
        
    def ventanaSegundoNivel(self):
        self.contador = 0
        
        pass
        

            
    
    
if __name__=="__main__":
    App = Visualizacion()
    App.ventanaPrincipal().mainloop()
        
        
        
                       
                                   