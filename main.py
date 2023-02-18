from pywebio.input import *
from pywebio.output import *

def bmicalculator():
    name = input("Instroduce tu nombre")
    height=input("Introduce tu altura en cm",type=FLOAT)
    weight=input("Introduce tu peso en Kg",type=FLOAT)
    
    bmi=weight/(height/100)**2
    
    bmi_output=[(16, 'Extremadamente delgado'), (18.5, 'Delgado'),
                  (25, 'Peso adecuado'), (30, 'Sobrepeso'),
                  (35, 'Sobrepeso moderado'), (float('inf'), 'Obeso')]
    
    for tuple1,tuple2 in bmi_output:
        if bmi<=tuple1:
            put_text('Hola {}, tu índice de masa corporal es :{} y por lo tanto tu estado es de  {}'.format(name, bmi, tuple2))
            bmicalculator()
        
        
    
if __name__=='__main__':
    bmicalculator()