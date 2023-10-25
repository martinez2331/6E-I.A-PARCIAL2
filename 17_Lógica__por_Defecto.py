#La l�gica por defecto es una forma de l�gica no mon�tona que se utiliza en inteligencia artificial para representar razonamientos que permiten 
#asumir que algo es cierto a menos que se demuestre lo contrario. En otras palabras, se parte de una base de conocimiento inicial que se asume 
#como verdadera y se pueden hacer inferencias basadas en esa base de conocimiento, pero estas inferencias pueden ser revisadas o modificadas en 
#funci�n de nueva informaci�n o excepciones.
#Un ejemplo cl�sico de l�gica por defecto es el "problema de los p�jaros" de John McCarthy. En este problema, se asume que los p�jaros pueden volar
# a menos que se demuestre lo contrario.


class BaseConocimiento:
    def __init__(self):
        self.hechos = set()
        self.reglas_por_defecto = []

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)

    def agregar_regla_por_defecto(self, regla):
        self.reglas_por_defecto.append(regla)

    def verificar_hecho(self, hecho):
        if hecho in self.hechos:
            return True
        else:
            for regla in self.reglas_por_defecto:
                if regla.aplicar(self, hecho):
                    return True
            return False

class ReglaPorDefecto:
    def __init__(self, condicion, conclusion):
        self.condicion = condicion
        self.conclusion = conclusion

    def aplicar(self, base_conocimiento, hecho):
        if all(base_conocimiento.verificar_hecho(cond) for cond in self.condicion):
            base_conocimiento.agregar_hecho(self.conclusion)
            return True
        else:
            return False

# Crear una base de conocimiento con l�gica por defecto
base_de_conocimiento = BaseConocimiento()

# Agregar un hecho inicial
base_de_conocimiento.agregar_hecho("p�jaros_pueden_volar")

# Agregar una regla por defecto
regla = ReglaPorDefecto(["p�jaros_pueden_volar"], "p�jaros_vuelan")
base_de_conocimiento.agregar_regla_por_defecto(regla)

# Verificar si los p�jaros vuelan
if base_de_conocimiento.verificar_hecho("p�jaros_vuelan"):
    print("Los p�jaros vuelan.")
else:
    print("No se sabe si los p�jaros vuelan.")

# Retirar el hecho inicial (simulando nueva informaci�n)
base_de_conocimiento.hechos.remove("p�jaros_pueden_volar")

# Verificar nuevamente si los p�jaros vuelan
if base_de_conocimiento.verificar_hecho("p�jaros_vuelan"):
    print("Los p�jaros vuelan.")
else:
    print("No se sabe si los p�jaros vuelan.")



#En este ejemplo, hemos creado una base de conocimiento que asume que "p�jaros_pueden_volar", pero tambi�n hemos definido una regla por defecto
# que establece que "p�jaros_pueden_volar" implica "p�jaros_vuelan". Cuando retiramos el hecho inicial, la l�gica por defecto no puede confirmar
#  si los p�jaros vuelan o no.En este ejemplo, hemos creado una base de conocimiento que asume que "p�jaros_pueden_volar", pero tambi�n hemos 
#  definido una regla por defecto que establece que "p�jaros_pueden_volar" implica "p�jaros_vuelan". Cuando retiramos el hecho inicial, la l�gica
#   por defecto no puede confirmar si los p�jaros vuelan o no.