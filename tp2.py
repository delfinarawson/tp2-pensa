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
    return(dict)

print(read_file("bolsa.csv"))


def monthly_average (accion, dict):
    for fecha in dict['Date']:
        fecha_split = fecha.split('-')
        mes = fecha_split[1] 
        lista_meses = []
        for mes in dict['Date']:
            if mes not in lista_meses:
                lista_meses.append(fecha_split)






    return(fecha,precios_promedio )
