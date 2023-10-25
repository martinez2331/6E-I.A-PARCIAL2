
#La l�gica difusa es un enfoque de la l�gica que permite manejar la incertidumbre y la imprecisi�n en la representaci�n del conocimiento y el 
#razonamiento. A diferencia de la l�gica cl�sica, en la que una proposici�n es verdadera o falsa de manera binaria, la l�gica difusa permite que 
#una proposici�n tenga un valor de verdad que var�a continuamente en un rango entre 0 y 1. En otras palabras, la l�gica difusa permite la
#representaci�n de grados de verdad.



import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Crear variables de entrada y salida difusas
temperatura = ctrl.Antecedent(np.arange(0, 101, 1), 'temperatura')
velocidad = ctrl.Consequent(np.arange(0, 101, 1), 'velocidad')

# Definir funciones de membres�a para las variables difusas
temperatura['fr�o'] = fuzz.trimf(temperatura.universe, [0, 0, 40])
temperatura['c�modo'] = fuzz.trimf(temperatura.universe, [30, 50, 70])
temperatura['caliente'] = fuzz.trimf(temperatura.universe, [60, 100, 100])

velocidad['baja'] = fuzz.trimf(velocidad.universe, [0, 0, 50])
velocidad['media'] = fuzz.trimf(velocidad.universe, [20, 50, 80])
velocidad['alta'] = fuzz.trimf(velocidad.universe, [50, 100, 100])

# Definir reglas difusas
regla1 = ctrl.Rule(temperatura['fr�o'], velocidad['alta'])
regla2 = ctrl.Rule(temperatura['c�modo'], velocidad['media'])
regla3 = ctrl.Rule(temperatura['caliente'], velocidad['baja'])

# Crear el sistema de control difuso
controlador = ctrl.ControlSystem([regla1, regla2, regla3])

# Crear una simulaci�n de controlador difuso
simulacion = ctrl.ControlSystemSimulation(controlador)

# Ingresar un valor de temperatura
simulacion.input['temperatura'] = 70  # Por ejemplo, temperatura de 70 grados

# Evaluar el sistema de control difuso
simulacion.compute()

# Obtener la velocidad resultante
print("Velocidad del ventilador:", simulacion.output['velocidad'])

# Mostrar las funciones de membres�a y la salida difusa
temperatura.view()
velocidad.view()

#Este c�digo utiliza la l�gica difusa para ajustar la velocidad de un ventilador en funci�n de la temperatura de una habitaci�n. 
#Define las funciones de membres�a, las reglas difusas y utiliza un controlador difuso para calcular la velocidad del ventilador
