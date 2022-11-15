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
            if i != 0:
                valor = float(valor)
            clave = claves[i]
            dict[clave].append(valor)
    return dict

dict = read_file('bolsa.csv')

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

for diccionario in dict[moneda][m]:
    suma= 0
    for valores in diccionario:
        suma += float(valores)
    promedio = suma / len(diccionario[moneda])
    precios_prom.append(promedio)

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

    precios_prom = []
    
    for valores in dict.values():                               # ['9.930000305175781', '9.920000076293945', '9.90999984741211', '9.914999961853027', '9.930000305175781', '9.90999984741211', '9.930000305175781', '9.9399995803833', '9.930000305175781', '9.930000305175781', '9.925999641418457', '9.930000305175781', '9.930000305175781', '9.920000076293945', '9.920000076293945', '9.930999755859375', '10.039999961853027']
        largo = len(valores)
        suma = 0
        for valor in valores:
            valor = float(valor)
            suma += valor
        promedio = suma/largo
        precios_prom.append(promedio)
    

    return lista_meses, precios_prom

monthly_average('SATL', read_file('bolsa.csv'))

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

# 4 
def max_gain (accion, dict, fecha_venta):
    
    ind_precio_venta = dict["Date"].index(fecha_venta)
    precio_venta = dict[accion][ind_precio_venta]

    minimo = dict[accion][0]
    ind_fecha_compra = 0
    precios = dict[accion][0:ind_precio_venta]
    for i, num in enumerate(precios):
        if num < minimo:
            minimo = num
            ind_fecha_compra = i
    
    precio_compra = minimo
    fecha_compra = dict["Date"][ind_fecha_compra]

    ganancia = (precio_venta - precio_compra) / precio_compra

    return fecha_compra, ganancia

"""     lista = list(dict[accion[1:]])
    minimo = min(lista)
    print(minimo) """

max_gain('RTX', dict, "2021-12-17")

# 5 
def report_max_gains(dict, fecha_venta):
    
    archivo = open('resumen_mejor_compra.txt', 'w')

    for accion in list(dict.keys())[1:]:
        fecha_compra, ganancia = max_gain(accion, dict, fecha_venta)
        line1 = f"{accion} genera una ganancia de {ganancia*100}% habiendo comprado en  {fecha_compra} y vendiendose en {fecha_venta}"
        line2 = 'la accion ' + accion + ' solo genera perdidas'
        if ganancia > 0:
            archivo.write(line1 + '\n')
        elif ganancia < 0:
            archivo.write(line2 + '\n')

    archivo.close()

    return archivo

report_max_gains(dict,"2022-06-06" )

# 6 
import matplotlib.pyplot as plt

def plot_price(accion, dict):

    ejex = dict['Date']
    ejey= dict[accion]
    plt.plot(ejex, ejey)
    plt.xlabel("Fechas")
    plt.ylabel("Precios")
    return plt.savefig(f'price_{accion}.png')

""" ganancia = (pv-pc) / pc
    for i, in enumerate()
 """
plot_price('MELI', dict)

# 7 
def monthly_average_bar_plot(accion, dict):
    average, fechas = monthly_average(accion, dict)
    plt.bar(average, fechas)
    plt.savefig(f"monthly_average_bar_plot{accion}.png")

monthly_average_bar_plot("MELI", dict)

