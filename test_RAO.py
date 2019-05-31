#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 13:35:28 2019

@author: josevergara
"""

import tkinter as tk
import romanos as roma
import visualizacion as vis
import unittest

class testRAO(unittest.TestCase):
    
    def test_instanciado_romanos(self):
        try:
            romano=roma.Romano('I')
        except NameError:
            raise AssertionError("La clase Romano no está definida")
        return True
    
    def test_atributos_romanos(self):
        romano = roma.Romano('X')
        self.assertEqual(romano.numeroRomano,'X')
        
    def test_baseRomanos(self):
        romano = roma.Romano('X')
        listaRomanos=[1000,500,100,50,10,5,1]
        baseRomanos = list(romano._Romano__baseRomanos.values())
        
        for i in range(len(baseRomanos)):
            self.assertEqual(baseRomanos[i],listaRomanos[i])
            
    def test_VerificarCaracteresRomanos(self):
        try:
            romano = roma.Romano('TMMMCM')
            romano.verificarCaracteresRomanos()
        except ValueError:
            pass
        except:
            raise AssertionError("No esta verificando caracteres Romanos")
            
    def test_VerificarSintaxisRomana(self):
        try:
            romano = roma.Romano('-IMMM')
            romano.verificarSintaxisRomana()
        except ValueError:
            pass
        except:
            raise AssertionError("No esta verificando sintaxis romana")
            
    def test_RomanoAArabigo_9(self):
        romano = roma.Romano('IX')
        arabigo = romano.romanoAArabigo()
        self.assertEqual(arabigo,9)
        
        
    def test_RomanoAArabigo_14(self):
        romano = roma.Romano('XIV')
        arabigo = romano.romanoAArabigo()
        self.assertEqual(arabigo,14) 
        
        
    def test_RomanoAArabigo_357(self):
        romano = roma.Romano('CCCLVII')
        arabigo = romano.romanoAArabigo()
        self.assertEqual(arabigo,357)
        
        
    def test_RomanoAArabigo_(self):
        romano = roma.Romano('MMMCM')
        arabigo = romano.romanoAArabigo()
        self.assertEqual(arabigo,3900)
        
        
        
    def test_instanciado_Visualizacion(self):
        try:
            vis.Visualizacion()
        except NameError:
            raise AssertionError("La clase Visualizacion no está definida")
        return True
    
    def test_instanciado_RevisionRespuestas(self):
        try:
            vis.RevisionRespuestas(3,'XX')
        except NameError:
            raise AssertionError("La clase RevisiónRespuestas no está definida")
        return True
    
    def test_revisionNivelTresAcertado(self):
        revision = vis.RevisionRespuestas(3,'CCCLXV').revision()
        self.assertTrue(revision,True)
        
    def test_revisionNivelTresIncorrecto(self):
        revision = vis.RevisionRespuestas(3,'XX').revision()
        self.assertFalse(revision)
        
    def test_revisionNivelTresIngresoErroneo(self):
        revision = vis.RevisionRespuestas(3,'caas').revision()
        self.assertFalse(revision)
        
    def test_revisionNivelCuatroAcertado(self):
        revision = vis.RevisionRespuestas(4,'MMMDC').revision()
        self.assertTrue(revision,True)
        
    def test_revisionNivelCuatroIncorrecto(self):
        revision = vis.RevisionRespuestas(4,'XX').revision()
        self.assertFalse(revision)
        
    def test_revisionNivelCuatroIngresoErroneo(self):
        revision = vis.RevisionRespuestas(4,'caas').revision()
        self.assertFalse(revision)
        
    def test_revisionNivelQuintoAcertado(self):
        revision = vis.RevisionRespuestas(5,'II').revision()
        self.assertTrue(revision,True)
        
    def test_revisionNivelQuintoIncorrecto(self):
        revision = vis.RevisionRespuestas(5,'XX').revision()
        self.assertFalse(revision)
        
    def test_revisionNivelQuintoIngresoErroneo(self):
        revision = vis.RevisionRespuestas(5,'caas').revision()
        self.assertFalse(revision)
        
    def test_revisionNivelSextoAcertado(self):
        revision = vis.RevisionRespuestas(6,'M+CC-XLV').revision()
        self.assertTrue(revision,True)
        
    def test_revisionNivelSextoIncorrecto(self):
        revision = vis.RevisionRespuestas(6,'XX+XX+XX+XX').revision()
        self.assertFalse(revision)
        
    def test_revisionNivelSextoIngresoErroneo(self):
        revision = vis.RevisionRespuestas(6,'caas').revision()
        self.assertFalse(revision)
        
    def test_revisionNivelSeptimoAcertado(self):
        revision = vis.RevisionRespuestas(7,'X+X-X+X-X').revision()
        self.assertTrue(revision,True)
        
    def test_revisionNivelSeptimoIncorrecto(self):
        revision = vis.RevisionRespuestas(7,'XX+XX+XX+XX').revision()
        self.assertFalse(revision)
        
    def test_revisionNivelSeptimoIngresoErroneo(self):
        revision = vis.RevisionRespuestas(7,'caas').revision()
        self.assertFalse(revision)
        
    def test_revisionNivelOchoAcertado(self):
        revision = vis.RevisionRespuestas(8,'DX-DVI').revision()
        self.assertTrue(revision,True)
        
    def test_revisionNivelOchoIncorrecto(self):
        revision = vis.RevisionRespuestas(8,'XX+XX+XX+XX').revision()
        self.assertFalse(revision)
        
    def test_revisionNivelOchoIngresoErroneo(self):
        revision = vis.RevisionRespuestas(8,'caas').revision()
        self.assertFalse(revision)
    def test_operacion(self):
        revision = vis.RevisionRespuestas(6,'XX+L-V+M-C')
        resultado = revision.operacion()
        self.assertEqual(resultado,965)
        
    def test_destruirVentana(self):
        app=vis.Visualizacion()
        ventana=app.crearVentana('test_destruirVentana')
        ventana = app.destruirVentana(ventana)
        try:
            ventana.attributes()
            verificador = True
        except:
            verificador = False
        self.assertFalse(verificador)
    
    def test_crearVentana(self):
        app=vis.Visualizacion()
        ventana=app.crearVentana('test_ventana')
        self.assertIsInstance(ventana,tk.Tk)
        app.destruirVentana(ventana)
        
    def test_crearBoton(self):
        app=vis.Visualizacion()
        ventana=app.crearVentana('test_boton')
        boton=app.crearBoton(ventana,'test_boton',None)
        self.assertIsInstance(boton,tk.Button)
        app.destruirVentana(ventana)
        
        
    def test_agregarImagenFondo(self):
        app=vis.Visualizacion()
        ventana = app.crearVentana('test_agregarImagenFondo')
        canvas,ancho,largo = app.agregarImagenFondo(ventana,"./images/VentanaPrincipal.ppm")
        self.assertIsInstance(canvas,tk.Canvas)
        app.destruirVentana(ventana)
        
    def test_opcionIncorrectaVidaMenos(self):
        app = vis.Visualizacion()
        app.contador = 0
        app.nivel = 3
        app.test = 1
        intentosRestantes = app.opcionIncorrecta()
        self.assertEqual(intentosRestantes,3)
        
    def test_opcionIncorrectaSinVidas(self):
        app = vis.Visualizacion()
        app.contador = 3
        app.nivel = 3
        app.test = 1 
        intentosRestantes = app.opcionIncorrecta()
        self.assertEqual(intentosRestantes,0)
        
    def test_nivelSuperado(self):
        app=vis.Visualizacion()
        ventana=app.crearVentana('test_nivelSuperado')
        app.ventanaSuperada = ventana
        app.ventanaSiguienteNivel = app.ventanaPrincipal
        app.imagen = "./images/PrimerNivelSuperado.ppm"
        ventanaNivelSuperado = app.nivelSuperado()
        self.assertIsInstance(ventanaNivelSuperado,tk.Tk)
        self.assertEqual(ventanaNivelSuperado.title(),'Nivel Superado')
        app.destruirVentana(ventanaNivelSuperado)
        
    def test_crearEntrada(self):
        app=vis.Visualizacion()
        ventana=app.crearVentana('test_Entrada')
        entrada=app.crearEntrada(ventana)
        self.assertIsInstance(entrada,tk.Entry)
        app.destruirVentana(ventana)
        
    def test_ingresarTexto(self):
        app=vis.Visualizacion()
        ventana=app.crearVentana('test_IngresarTexto')
        entrada=app.crearEntrada(ventana)
        nivel = app.nivel = 3
        app.test = 1
        textoIngresado = app.ingresarTexto()
        self.assertEqual(textoIngresado,'')
        app.destruirVentana(ventana)
        
        
    def test_ventanas(self):
        app=vis.Visualizacion()
        ventanaPrincipal = app.ventanaPrincipal()
        self.assertIsInstance(ventanaPrincipal,tk.Tk)
        self.assertEqual(ventanaPrincipal.title(),'Rumbo Al Olimpo')
        
        ventanaIntro = app.ventanaIntro()
        self.assertIsInstance(ventanaIntro,tk.Tk)
        self.assertEqual(ventanaIntro.title(),'Introducción')
        
        ventanaPrimerNivel = app.ventanaPrimerNivel()
        self.assertIsInstance(ventanaPrimerNivel,tk.Tk)
        self.assertEqual(ventanaPrimerNivel.title(),'Nivel 1')
        
        ventanaNivelSuperado = app.nivelSuperado()
        ventanaSegundoNivel = app.ventanaSegundoNivel()
        self.assertIsInstance(ventanaSegundoNivel,tk.Tk)
        self.assertEqual(ventanaSegundoNivel.title(),'Nivel 2')
        
        ventanaNivelSuperado = app.nivelSuperado()
        ventanaTercerNivel = app.ventanaTercerNivel()
        self.assertIsInstance(ventanaTercerNivel,tk.Tk)
        self.assertEqual(ventanaTercerNivel.title(),'Nivel 3')
        
        ventanaNivelSuperado = app.nivelSuperado()
        ventanaCuartoNivel = app.ventanaCuartoNivel()
        self.assertIsInstance(ventanaCuartoNivel,tk.Tk)
        self.assertEqual(ventanaCuartoNivel.title(),'Nivel 4')
        
        ventanaNivelSuperado = app.nivelSuperado()
        ventanaQuintoNivel = app.ventanaQuintoNivel()
        self.assertIsInstance(ventanaQuintoNivel,tk.Tk)
        self.assertEqual(ventanaQuintoNivel.title(),'Nivel 5')
        
        ventanaNivelSuperado = app.nivelSuperado()
        ventanaSextoNivel = app.ventanaNivelSeis()
        self.assertIsInstance(ventanaSextoNivel,tk.Tk)
        self.assertEqual(ventanaSextoNivel.title(),'Nivel 6')
        
        ventanaNivelSuperado = app.nivelSuperado()
        ventanaSeptimoNivel = app.ventanaNivelSiete()
        self.assertIsInstance(ventanaSeptimoNivel,tk.Tk)
        self.assertEqual(ventanaSeptimoNivel.title(),'Nivel 7')
        
        ventanaNivelSuperado = app.nivelSuperado()
        ventanaOchoNivel = app.ventanaNivelOcho()
        self.assertIsInstance(ventanaOchoNivel,tk.Tk)
        self.assertEqual(ventanaOchoNivel.title(),'Nivel 8')
        
        ventanaNivelSuperado = app.nivelSuperado()
        ventanaComprar = app.comprarJuego()
        self.assertIsInstance(ventanaComprar,tk.Tk)
        self.assertEqual(ventanaComprar.title(),'Comprar Juego')
        app.destruirVentana(ventanaComprar)
        

        

    