# LLENAR DICCIONARIO
print('LLENE EL DICCIONARIO CON NOMBRES Y UN NUMERO ASOCIADO A ESTE')

## cantidad de personas
cantidad_personas=int(input('Ingrese la cantidad de personas: '))

## llenar diccionario
diccionario=dict([(input(f'Nombre de la persona {i+1}: '),int(input(f'Numero de la persona {i+1}:'))) for i in range(cantidad_personas)])

# ACTIVIDAD BÁSICA
print('\nACTIVIDAD BÁSICA\n')

## imprimir valores
for nombre,numero in diccionario.items():
    print(f'Nombre de la persona: {nombre}, Numero:{numero}')

## imprimir numero mas grande y mas pequeño
print(f'\nEl número más grande es: {max(diccionario.values())}')
print(f'El número más pequeño es: {min(diccionario.values())}')

# ACTIVIDAD AVANZADA
print('\nACTIVIDAD AVANZADA\n')
## importar libreria para numeros aleatorios
from random import randrange

## asignar un numero aleatorio al diccionario de nombres anterior
diccionario=dict([(i,randrange(1,31)) for i in diccionario.keys()])

## imprimir valores del diccionario
for nombre,numero in diccionario.items():
    print(f'Nombre de la persona: {nombre}, Numero:{numero}')
    
## imprimir numero mas grande y mas pequeño
print(f'\nEl número más grande es: {max(diccionario.values())}')
print(f'El número más pequeño es: {min(diccionario.values())}')