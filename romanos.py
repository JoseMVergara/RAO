#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 13:35:53 2019

@author: josevergara
"""
import re

class Romano(object):
    
    """
    0 a 4000
    
    """

    def __init__(self,numeroRomano):
        self.numeroRomano = numeroRomano
        self.__baseRomanos = {
        'M' : 1000,
        'D' : 500,
        'C' : 100,
        'L' : 50,
        'X' : 10,
        'V' : 5,
        'I' : 1
        }
        
    def verificarCaracteresRomanos(self):
        caracteresAceptados = self.__baseRomanos.keys()
        caracteresDesconocidos = filter(lambda x: x not in caracteresAceptados,
                                        self.numeroRomano)
        if len(list(caracteresDesconocidos))>0:
            raise ValueError('Ha introducido algún caracter desconocido')
            
    def verificarSintaxisRomana(self):
        
        reglas = re.compile("""M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})
                (IX|IV|V?I{0,3})$""",re.VERBOSE)
        
        buscarRomano = reglas.search(self.numeroRomano)
        valoresAgrupados = ""
        
        if buscarRomano:
            valoresAgrupados = buscarRomano.group()
            
        if valoresAgrupados != self.numeroRomano:
            raise ValueError('La sintaxis del número ingresado es incorrecta')
            
    def romanoAArabigo(self):
        
        self.verificarCaracteresRomanos()
        self.verificarSintaxisRomana()
        
        numeroArabigo = 0
        valorAnterior = 0
            
        for letra in self.numeroRomano:
            valorActual = self.__baseRomanos[letra]
            
            if valorAnterior < valorActual:
                numeroArabigo = numeroArabigo + valorActual - (valorAnterior * 2) 
            else:
                numeroArabigo += valorActual
            valorAnterior = valorActual
            
        return numeroArabigo
            
        
            
        
    