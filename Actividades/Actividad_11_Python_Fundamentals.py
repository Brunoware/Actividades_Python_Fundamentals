#############################################################################################################
##########################################ACTIVIDAD: Básica##################################################
#############################################################################################################

print('ACTIVIDAD: Básica\n')
## Ingresar montos de cliente, cuando es 0 sale del bucle
monto_compra=1
monto_compras=list()
n_compra=1
print('Ingrese las compras hechas (salir con 0)')
while monto_compra!=0:
    monto_compra=float(input(f'Ingrese el monto de la compra {n_compra}: '))
    if monto_compra<0:
        print(f'Ingrese de nuevo el valor de la compra {n_compra}, no se admite numeros negativos')
    else:
        monto_compras.append(monto_compra)
        n_compra+=1
### Imprimir salida
monto_compras=monto_compras[:-1]
print(f'Cantidad de articulos: {len(monto_compras)}')
print(f'Subtotal: ${sum(monto_compras)}')
print(f'Descuento: ${0.1*sum(monto_compras)}' if sum(monto_compras)>1000 else 'Sin dcto.' )
print(f'Total: ${0.9*sum(monto_compras)}'if sum(monto_compras)>1000 else f'Total: ${sum(monto_compras)}' )

#############################################################################################################
##########################################ACTIVIDAD: Avanzada################################################
#############################################################################################################

print('\nACTIVIDAD: Avanzada\n')
## Ingresar tiempo de cliente en estacionamiento, cuando es 0 sale del bucle
tiempo=1
tiempos=list()
n_ticket=1
print('Ingrese los tiempos en minutos (salir con 0)')
while tiempo!=0:
    tiempo=float(input(f'Ingrese el tiempo {n_ticket}: '))
    if tiempo<0:
        print(f'Ingrese de nuevo el valor del tiempo {n_ticket}, no se admite numeros negativos')
    else:
        tiempos.append(tiempo)
        n_ticket+=1
## Quitar 0
tiempos=tiempos[:-1] 
## cantidad de horas
cant_horas=sum(tiempos)/60
## tarifa a pagar por la horas
tarifa=25+12*(cant_horas-1) if cant_horas>1 else 25*cant_horas
## monto a pagar si se pasa las 8horas
monto_total=tarifa+200 if cant_horas>8 else tarifa
## imprimir resultados
print(f'Cantidad de horas en el estacionamiento: {cant_horas:.2f}')
print(f'Subtotal a pagar por la cantidad de horas: ${tarifa:.2f}')
print(f'Total a pagar (incluyendo si se paso de 8 horas): ${monto_total:.2f}')