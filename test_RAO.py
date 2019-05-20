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
        
        
        
    def test_instanciado_visualizacion(self):
        try:
            app = vis.Visualizacion()
        except NameError:
            raise AssertionError("La clase visualizacion no está definida")
        return True
    
        
        
    
    
    
        
if __name__=="__main__":
    unittest.main()
    