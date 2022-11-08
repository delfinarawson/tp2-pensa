
# 1 listo

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

# 2 esta parte esta bien 

for fecha in dict['Date']:
    fecha_split = fecha.split('-') # ['2021', '10', '04],['2021', '10', '03]
    ano_mes = fecha_split[0]+"-"+fecha_split[1]
    if ano_mes not in lista_meses:
        lista_meses.append(ano_mes)
        lista_fechas.append(fecha) # logramos tener la primer secuencia de fechas

# 2 esta parte no nos sale

dict_satl = {}
dict_meli = {}
dict_mhvyf = {}
dict_rtx = {}

lista_valores=[]

for mes in lista_meses: # mes es '2021-10, 2021-11, 2021,12 ...'
    dict[mes]= 0

for linea in lineas[1:]:
    linea_split = linea.strip().split(',') # ['2022-08-24', '5.050000190734863', '917.4400024414062', '35.63999938964844', '93.58000183105469']
    m = linea_split[0][0:7] # 2022-08    
    if mes == m:
        dict_satl[mes] = lista_valores

