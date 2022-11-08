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
    lista_meses = [] 
    lista_fechas=[]

    cada_mes = []
    precios = []
    promedio_meses = []
    
    for fecha in dict['Date']:
        fecha_split = fecha.split('-')
        ano_mes = fecha_split[0]+"-"+fecha_split[1] 
        if ano_mes not in lista_meses:
            lista_meses.append(ano_mes)
            lista_fechas.append(fecha)
            #['2021-10-04', '2021-11-01', ...] 

    for mes in lista_meses:
        if mes == fecha_split[1]:
            cada_mes.append(fecha_split)
        