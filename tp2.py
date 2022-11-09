
# 1

def read_file (archivo):
    archivo = open(archivo, "r")
    lineas = archivo.readlines()
    archivo.close()
    dict = {}

    claves = lineas[0].strip().split(',') 
    for clave in claves:
        dict[clave] = []

    for linea in lineas[1:]: 
        valores = linea.strip().split(',')  
        for i, valor in enumerate(valores):
            clave = claves[i]
            dict[clave].append(valor)
    return dict

# 2

def monthly_average(accion, diccionario):

    dict = {}
    
    precios = diccionario[accion]
    fechas = diccionario['Date']
    lista_meses = []

    i = 0
    while i < len(fechas):
        fecha = fechas[i] 
        precio = precios[i]
        i += 1
        fecha_split = fecha.split('-')
        ano_mes = fecha_split[0]+"-"+fecha_split[1] 
        if ano_mes not in dict:
            lista_meses.append(fecha)
            dict[ano_mes] = []
        dict[ano_mes].append(precio)
    
    precios_prom = []
    
    for valores in dict.values(): # ['9.930000305175781', '9.920000076293945', '9.90999984741211', '9.914999961853027', '9.930000305175781', '9.90999984741211', '9.930000305175781', '9.9399995803833', '9.930000305175781', '9.930000305175781', '9.925999641418457', '9.930000305175781', '9.930000305175781', '9.920000076293945', '9.920000076293945', '9.930999755859375', '10.039999961853027']
        largo = len(valores)
        suma = 0
        for valor in valores:
            valor = float(valor)
            suma += valor
        promedio = suma/largo
        precios_prom.append(promedio)

    return lista_meses, precios_prom

monthly_average('SATL', read_file('bolsa.csv'))
print(monthly_average('SATL', read_file('bolsa.csv')))

# 3
archivo = open("monthly_average_SATL.csv", "w")

archivo.write("fechas promedios"+ "\n")
lista_meses, precios_prom = monthly_average('SATL', read_file('bolsa.csv'))
i = 0
while i < len(lista_meses):
    line = str(lista_meses[i]) +","+ str(precios_prom[i]) + "\n"
    i += 1
    archivo.write(line)
    

archivo.close()

def max_gain (accion,dict,fecha_venta):
    # precios = dict[accion]
    # fechas = dict["Date"]
    # tuplas = zip(precios, fechas)



    minimo = 10000000
    index = 0
    for i, num in enumerate(dict[accion[1:]]):
        if num < minimo:
            minimo = num
            index += i
    fecha_compra = dict[accion[index]]

    
"""     lista = list(dict[accion[1:]])
    minimo = min(lista)
    print(minimo) """

max_gain("SATL", read_file("bolsa.csv"), "2021-10-04")


    # valores_accion = dict[accion]
    # fecha = dict["date"]
    # indice = fecha.index(fecha[venta])



    """ ganancia = (pv-pc) / pc
    for i, in enumerate()
 """



