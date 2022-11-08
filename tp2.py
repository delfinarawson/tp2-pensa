
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

print(read_file("bolsa.csv"))

def monthly_average(accion, diccionario):

    dict = {}
    
    precios = diccionario[accion]
    fechas = diccionario['Date']

    i = 0
    while i < len(fechas):
        fecha = fechas[i] 
        precio = precios[i]
        i += 1
        fecha_split = fecha.split('-')
        ano_mes = fecha_split[0]+"-"+fecha_split[1] 
        if ano_mes not in dict:
            dict[ano_mes] = []
        dict[ano_mes].append(precio)
        
    precios_prom = []

# lo del promedio aca 

    # for diccionario in dict_monedas[moneda][m]:
    #     suma = 0 
    #     for valores in diccionario:
    #         suma += float(valores)
    #     promedio = suma / len(diccionario[moneda])
    #     precios_prom.append(promedio)


    """ for linea in lineas[1:]:
        linea_split = linea.strip().split(',') # ['2022-08-24', '5.050000190734863', '917.4400024414062', '35.63999938964844', '93.58000183105469']
        m = linea_split[0][0:7] # 2022-08  
        for i, moneda in enumerate(nombres_monedas):  
            dict_monedas[accion][m].append(linea_split[i+1])   """
    
monthly_average('SATL', read_file('bolsa.csv'))