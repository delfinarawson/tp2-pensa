archivo = open('bolsa.csv', "r")
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

lista_meses = [] 
lista_fechas=[]
for fecha in dict['Date']:
    fecha_split = fecha.split('-')
    ano_mes = fecha_split[0]+"-"+fecha_split[1]
    mes = fecha_split[1] 
    if ano_mes not in lista_meses:
        lista_meses.append(ano_mes)
        lista_fechas.append(fecha)


print(lista_fechas)



