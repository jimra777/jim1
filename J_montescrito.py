#Prueba Montoescrito en python de Jimmy Claudio Ramirez Llanos
# Terminado el 6 de Agosto 2020


def ConvierteCifra(CadNumEntero):
    Unidad = CadNumEntero[2]
    Decena = CadNumEntero[1]
    select_variable_0 = CadNumEntero[0] # Centenas
    select_variable_1 = CadNumEntero[1] # Decenas
    select_variable_3 = CadNumEntero[2] # Unidades
    
    txtUnidad = ''
    txtDecena = ''
    txtCentena = ''
    fn_return_value = ''
    #print(CadNumEntero[7:10]) # Halla los 3 ultimos numeros
    # print(Unidad)
    # print(Decena)
    # print(select_variable_0)
    # print(select_variable_1)
    # print(select_variable_3)
    # print('Valor decimales es:' ,decimales)

    
    if (select_variable_0 == '1'):
        txtCentena = 'CIEN '
        if Decena + Unidad != '00':
                txtCentena = 'CIENTO '
    elif (select_variable_0 == '2'):
                txtCentena = 'DOSCIENTOS '
    elif (select_variable_0 == '3'):
                txtCentena = 'TRESCIENTOS '
    elif (select_variable_0 == '4'):
                txtCentena = 'CUATROCIENTOS '
    elif (select_variable_0 == '5'):
                txtCentena = 'QUINIENTOS '
    elif (select_variable_0 == '6'):
                txtCentena = 'SEISCIENTOS '
    elif (select_variable_0 == '7'):
                txtCentena = 'SETECIENTOS '
    elif (select_variable_0 == '8'):
                txtCentena = 'OCHOCIENTOS '
    elif (select_variable_0 == '9'):
                txtCentena = 'NOVECIENTOS '
    select_variable_1 = Decena
    #print('Variable1 Decena: ',select_variable_1)
    if (select_variable_1 == '1' and select_variable_3 == '0' ):
        txtDecena = 'DIEZ'
        
    elif (select_variable_1 == '1' and select_variable_3 == '1' ):
                    txtDecena = 'ONCE '
    elif (select_variable_1 == '1' and select_variable_3 == '2' ):
                    txtDecena = 'DOCE '
    elif (select_variable_1 == '1' and select_variable_3 == '3' ):
                    txtDecena = 'TRECE '
    elif (select_variable_1 == '1' and select_variable_3 == '4' ):
                    txtDecena = 'CATORCE '
    elif (select_variable_1 == '1' and select_variable_3 == '5' ):
                    txtDecena = 'QUINCE'
    elif (select_variable_1 == '1' and select_variable_3 == '6' ):
                    txtDecena = 'DIECISEIS '
    elif (select_variable_1 == '1' and select_variable_3 == '7' ):
                    txtDecena = 'DIECISIETE '
    elif (select_variable_1 == '1' and select_variable_3 == '8' ):
                    txtDecena = 'DIECIOCHO '
    elif (select_variable_1 == '1' and select_variable_3 == '9' ):
                    txtDecena = 'DIECINUEVE '
    elif (select_variable_1 == '2' and select_variable_3 == '0' ):
                txtDecena = 'VEINTE '
    elif (select_variable_1 == '2' and select_variable_3 != '0' ):
                txtDecena = 'VEINTI'
    elif (select_variable_1 == '3' and select_variable_3 == '0' ):
                txtDecena = 'TREINTA '
    elif (select_variable_1 == '3' and select_variable_3 != '0' ):
                    txtDecena = 'TREINTA Y '
    elif (select_variable_1 == '4' and select_variable_3 == '0' ):
                txtDecena = 'CUARENTA'
    elif (select_variable_1 == '4' and select_variable_3 != '0' ):
                    txtDecena = 'CUARENTA Y '
    elif (select_variable_1 == '5' and select_variable_3 == '0' ):
                txtDecena = 'CINCUENTA'
    elif (select_variable_1 == '5' and select_variable_3 != '0' ):
                    txtDecena = 'CINCUENTA Y '
    elif (select_variable_1 == '6' and select_variable_3 == '0' ):
                txtDecena = 'SESENTA '
    elif (select_variable_1 == '6' and select_variable_3 != '0' ):
                    txtDecena = 'SESENTA Y '
    elif (select_variable_1 == '7' and select_variable_3 == '0' ):
                txtDecena = 'SETENTA '
    elif (select_variable_1 == '7' and select_variable_3 != '0' ):
                    txtDecena = 'SETENTA Y '
    elif (select_variable_1 == '8' and select_variable_3 == '0' ):
                txtDecena = 'OCHENTA '
    elif (select_variable_1 == '8' and select_variable_3 != '0' ):
                    txtDecena = 'OCHENTA Y '
    elif (select_variable_1 == '9' and select_variable_3 == '0' ):
                txtDecena = 'NOVENTA '
    elif (select_variable_1 == '9' and select_variable_3 != '0' ):
                    txtDecena = 'NOVENTA Y '

    if (select_variable_3 == '1' and select_variable_1 == '0' and select_variable_0 == '0'):
        txtUnidad = 'UN '
    elif (select_variable_3 == '1' and select_variable_1 != '1' ):
        txtUnidad = 'UNO '
    elif (select_variable_3 == '2' and select_variable_1 != '1'):
                    txtUnidad = 'DOS '
    elif (select_variable_3 == '3' and select_variable_1 != '1'):
                    txtUnidad = 'TRES '
    elif (select_variable_3 == '4' and select_variable_1 != '1'):
                    txtUnidad = 'CUATRO '
    elif (select_variable_3 == '5' and select_variable_1 != '1'):
                    txtUnidad = 'CINCO '
    elif(select_variable_3 == '6' and select_variable_1 != '1'):
                    txtUnidad = 'SEIS'
    elif(select_variable_3 == '7' and select_variable_1 != '1'):
                    txtUnidad = 'SIETE '
    elif (select_variable_3 == '8' and select_variable_1 != '1'):
                    txtUnidad = 'OCHO '
    elif (select_variable_3 == '9' and select_variable_1 != '1'):
                    txtUnidad = 'NUEVE '
    elif (select_variable_3 == '0' and select_variable_1 == '0' and select_variable_0 == '0' and CadMillones == '000' and CadMiles == '000' and CadCientos == '000'):
                    txtUnidad = 'CERO '
    #fn_return_value = txtCentena + ' ' + txtDecena + txtUnidad + ' PESOS CON ' + decimales + '/100' + ' MONEDA CTE.'
    fn_return_value = txtCentena + ' ' + txtDecena + txtUnidad  
    return fn_return_value

# Se declara primero la funcion y luego la trabajo de aqui adelante. Ojo con la Indentacion de las funciones
# CadNumEntero = CadNumEntero2
# print(ConvierteCifra(CadNumEntero))
# print(ConvierteCifra('0000000001.67'))
# INICIA VALIDACION INPUT
CadNumEntero2 = str(input("(Ingresa entero máximo con 10 digitos, con o sin ceros a la izquierda un punto y dos decimales. Ejemplo: 0000000302.55):    "))
lon = str
sf = str
lon = len(CadNumEntero2)

#print('Valor de long: ' , lon , CadNumEntero2) 

if (str(lon) == '13'):
    print('Okey longitud es de  13 caracteres!')
    
elif (str(lon) == '1'):
    CadNumEntero2 = '0000000000.0' + CadNumEntero2

elif (str(lon) == '2'):
    CadNumEntero2 = '0000000000.' + CadNumEntero2

elif (str(lon) == '3'):
    CadNumEntero2 = '0000000000' + CadNumEntero2

elif (str(lon) == '4'):
    CadNumEntero2 = '000000000' + CadNumEntero2

elif (str(lon) == '5'):
    CadNumEntero2 = '00000000' + CadNumEntero2

elif (str(lon) == '6'):
    CadNumEntero2 = '0000000' + CadNumEntero2

elif (str(lon) == '7'):
    CadNumEntero2 = '000000' + CadNumEntero2
    
elif (str(lon) == '8'):
    CadNumEntero2 = '00000' + CadNumEntero2

elif (str(lon) == '9'):
    CadNumEntero2 = '0000' + CadNumEntero2

elif (str(lon) == '10'):
    CadNumEntero2 = '000' + CadNumEntero2

elif (str(lon) == '11'):
    CadNumEntero2 = '00' + CadNumEntero2

elif (str(lon) == '12'):
    CadNumEntero2 = '0' + CadNumEntero2
else:
    print('!Error la longitud excede 13 caracteres ')
    sf = '1'

print('El valor es: ' + CadNumEntero2)
CadNumEntero = CadNumEntero2

## FIN VALIDACION

CadMilMillones = CadNumEntero[0]
CadMillones = CadNumEntero[1:4]
#print(CadMillones)
CadMiles = CadNumEntero[4:7]
CadCientos = CadNumEntero[7:10]
decimales =  CadNumEntero[11:13]
s1 = '0'
cadena1 = ''
cadenaM = ''
cadena2 = ''
cadena3 = ''
cadena4 = ''
cadena5 = ''

if (CadMilMillones > '0' and sf != '1'):
    CadMilMillones2 = '00' + CadMilMillones
    cadena = (ConvierteCifra(CadMilMillones2))
    cadena1 = cadena + ' MIL '
    s1 = '1'
    #print('Valor de CADENA1:' + cadena1)

if (CadMillones == '000' and s1 == '1' and sf != '1' ):
    cadena1 = cadena + ' MIL MILLONES '

if (CadMillones != '000' and sf != '1'):
    # print('Entro a millones:' + CadMillones )
    cadena = (ConvierteCifra(CadMillones))
    cadena2 = cadena + ' MILLONES '


if (CadMiles != '000' and sf != '1'):
    # print('Entro a miles')
    cadena = (ConvierteCifra(CadMiles))
    cadena3 = cadena + ' MIL '

if (CadCientos != '000' and sf != '1'):
    # print('Entro a cientos')
    cadena = (ConvierteCifra(CadCientos))
    cadena4 = cadena 

if (CadCientos == '000' and sf != '1'):
    # print('Entro a cientos')
    cadena = (ConvierteCifra(CadCientos))
    cadena4 = cadena

if  (CadMilMillones > '0' and CadMillones == '000' and CadMiles == '000' and CadCientos == '000' and sf != '1'):
    cadena1 = cadena1 + ' MIL MILLONES '  

cadena5 = ' PESOS ' + 'CON ' + decimales + '/100' + ' MONEDA CTE.'
if (sf != '1'):
    print(cadena1 + cadena2 + cadena3 + cadena4 + cadena5)