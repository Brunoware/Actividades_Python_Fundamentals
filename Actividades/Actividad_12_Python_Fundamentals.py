#############################################################################################################
##########################################ACTIVIDAD: Básica##################################################
#############################################################################################################
print('\nACTIVIDAD: Básica\n')
# Funcion que reciba como inrgeso los parametros reales de una funcion cuadratica y rgerese x1 y x2
def cortes_funcion(a,b,c):
    x1=(-b-pow(pow(b,2)-4*a*c,0.5))/(2*a)
    x2=(-b+pow(pow(b,2)-4*a*c,0.5))/(2*a)
    return x1,x2
# Pedir que ingrese los parámetros
parametros=['a','b','c']
parametros_in=[float(input(f'Ingrese parámetro {i}: ')) for i in parametros]
# calcular la salida
x1,x2=cortes_funcion(parametros_in[0],parametros_in[1],parametros_in[2])
# mostrar la salida
print(f'El valor de x1 es complejo: {x1:.2f}' if isinstance(x1,complex) else f'El valor de x1 es real: {x1:.2f}')
print(f'El valor de x2 es complejo: {x2:.2f}' if isinstance(x2,complex) else f'El valor de x2 es real: {x2:.2f}')

#############################################################################################################
##########################################ACTIVIDAD: Avanzada################################################
#############################################################################################################
print('\nACTIVIDAD: Avanzada\n')
# Funcion que reciba como inrgeso los parametros reales e imaginarios de una funcion cuadratica y rgerese x1 y x2
def cortes_funcion_complex(a,ai,b,bi,c,ci):
    # convertir a complejo
    a=complex(a,ai)
    b=complex(b,bi)
    c=complex(c,ci)
    # calcular raices
    x1=(-b-pow(pow(b,2)-4*a*c,0.5))/(2*a)
    x2=(-b+pow(pow(b,2)-4*a*c,0.5))/(2*a)
    return x1,x2
    # Pedir que ingrese los parámetros

parametros=['a','ai','b','bi','c','ci']
parametros_in=[float(input(f'Ingrese parámetro {i}: ')) for i in parametros]
# calcular la salida
x1,x2=cortes_funcion_complex(parametros_in[0],parametros_in[1],parametros_in[2],parametros_in[3],parametros_in[4],parametros_in[5])
# mostrar la salida
print(f'Parte real de la variable x1: {x1.real:.2f}; parte compleja de la variable x1: {x1.imag:.2f}' if x1.imag!=0 else f'La variable x1 es real cuyo valor es {x1.real:.2f}' )
print(f'Parte real de la variable x2: {x2.real:.2f}; parte compleja de la variable x2: {x2.imag:.2f}' if x2.imag!=0 else f'La variable x2 es real cuyo valor es {x2.real:.2f}')