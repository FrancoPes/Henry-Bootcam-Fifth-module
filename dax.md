
# TIPOS DE FUNCIONES
# 1) funciones de agregacion 
Medidasumatotalcantidad = sum(Ventas[Cantidad]) ---> nos suma toda la columna cantidad ---> nos filtra si estamos en una tabla 

Medidasumatotalcantidad = max(Ventas[Cantidad])  ----> nos saca el max cantidad dependiendo con el filtro 
Medidasumatotalcantidad = min(Ventas[Cantidad]) ----> nos saca el min cantidad dependiendo con el filtro 
Medidasumatotalcantidad = average(Ventas[Cantidad])----> nos saca el avg cantidad dependiendo con el filtro 
Medidasumatotalcantidad = count(Ventas[Cantidad]) ----> nos cuenta dependiendo el filtro 
Medidasumatotalcantidad = distinctcount(Ventas[Cantidad]) ----> nos cuentan los registro unicos  dependiendo el filtro


# 2) funciones de conversion 
 Medidasumatotalcantidad = currency(Ventas[Ventas totales]) ----> signo de pesos 


# 3) funciones logicas: IF AND OR SWITCH 
MES NOMBRE = SWITCH(Calendario[Mes], 1, "enero", 2, "febrero", 3, "Marzo", 4, "abril", 5, "Mayo", 6, "Junio" , 7, "julio", 8, "agosto", 9, "septiembre", 10, "octubre", 11, "noviembre", 12, "diciembre", BLANK())


# funcion calculate --> power bi entiende que queremos sumar filas x filas (en columnas calculadas)
medida ---> Medida_sum_calculate = CALCULATE(sum(Ventas[Cantidad]))

# en una medida es lon mismo, pero en una columna nos da resultados distintos. en una columna suma todo con sunm. con calculate filtra 

# calculate 
Medida_sum_calculate = CALCULATE(sum(Ventas[Cantidad]))  ---> primer argumento es lo que quiero sumar o calcular, sewgundo es el filtro 
# SI QUEREMOS TOMAR UNA MEDIDA COMO PRINMER ARGUMENTO PODEMOS HACERLO
Medida_sum_calculate = CALCULATE(sum(Ventas[Cantidad]),Calendario[MES NOMBRE] = "enero")


# https://www.youtube.com/watch?v=Dyev54Q2Rvk __> DIF ENTRE MEDIDA Y TABLA CALCULADA


# FILTER:
NO usar medida como segundo argumento 

la funcion filter nos devuelve una tabla

creo una nueva tabla ---> tabla clientes mayores a 600000 = FILTER(ventas, Ventas[Total] > 600000)

clientes mayores a 80000 = CALCULATE(sum('tabla clientes mayores a 600000'[Total]))  --> hago un filtrob sobre esa tabla 

# previous month
Ventas PM = CALCULATE(Ventas[Ventas totales],PREVIOUSMONTH(Calendario[Date])) 
# aca si puedo tener una medida como primer argumento 

