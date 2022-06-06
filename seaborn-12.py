# https://www.youtube.com/watch?v=eG663qYKjVw
# https://www.youtube.com/watch?v=ooqXQ37XHMM

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import seaborn as sns
sns.set()

# Definimos las columnas que nos interesan
fields = ['country', 'points','price', 'variety']

# Cargamos el DataFrame solo con esas columnas
wine_reviews = pd.read_csv('wine_reviews.csv', usecols = fields)
print(wine_reviews.head())


# en matplotlib usamoss vectores, en seaborn es mucho ams facil


#?ax = sns.scatterplot(x="price", y="points", hue="country" , data=wine_reviews)
#?plt.show()

#La ventaja de utilizar esta libreria radica en que podemos indicarle a la función `scatterplot` 
# de seaborn cual es el Dataframe del cual queremos tomar los datos para graficar
# a traves del argumento `data` (`data=wine_reviews`).

#De esta forma, al darle los nombres de las columnas que queremos usar en los ejes `x` e `y`, 
# la librearia ya interpreta que debe tomar los valores correspondientes 
# a esas columnas para graficar (en este caso, `x="price"` e `y="points"`).


#? scatter plot 
lista_paises = ['Argentina','Chile','Spain']
wine_reviews_filtradas = wine_reviews[wine_reviews['country'].isin(lista_paises)]
wine_reviews_filtradas.head()
# solo son interesan vinos de argentina chile y espana


#?ax = sns.scatterplot(x="price", y="points", hue="country" , data=wine_reviews_filtradas)
#?plt.show()


#En este caso, le estamos indicando a la funcion `scatterplot` que no solo queremos que tome la columna `price` como eje `x`
# y la columna `points` como eje `y`, sino que además queremos que indique con colores distintos los puntos segun su valor
# de la columna `country`.
# Esto lo hacemos mediante el argumento `hue` (`hue="country"`).

#Esperamos con estos primeros ejemplos haberlos convencido que el uso de Seaborn facilita la visualización de 
# datos provienentes de un DataFrame respecto a la utilización de (solo) Matplotlib. A continuación vamos a explorar
# algunas de las funciones de visualización que nos ofrece esta libreria.


# CATEGORICAL PLOTS
iris_data = pd.read_csv('iris_dataset.csv')
iris_data.drop(columns = ['fila'], inplace= True)
iris_data.head()

### 2.1. Categorical plot básico

#Como su nombre lo indica, los categorical plots son gráficos donde una de las variables a graficar es de tipo categórica. 
# Este tipo de gráficos son muy usados en Data Science y Seaborn tiene una función especial dedicada a ellos, `catplot`.

#Primero veamos un ejemplo de cómo hacer para realizar un grafico de este tipo en Matplotlib. 
# El objetivo es graficar el ancho del petalo según la especie .
especie = iris_data['species']
ancho_petalo = iris_data['sepal_length']

fig = plt.figure()
ax = plt.axes()
ax.scatter(especie,ancho_petalo)
plt.show()


#Como podemos observar el resultado no es muy satisfactorio. 
# Al estar todos los puntos sobre una misma linea, no se pueden distinguir entre sí. 
#Veamos ahora como realizar el mismo gráfico son seaborn:
sns.catplot(data = iris_data, x = "species", y = "sepal_length",ci = "sd",estimator=np.median)
plt.show()


#Como se puede observar, Seaborn le da automáticamente distintos colores a las categorías y además los separa para poder identificar la cantidad de puntos en cada grupo con facilidad.

#? **Ejercicos**:

#! 1. Realizar con Seaborn un gráfico del ancho del petalo según la especie
#! 2. Realizar el mismo gráfico, pero ahora como gráfico de barras. **Pista**: ver el parametro `kind`
#! 3. ¿Que representan las barritas negras?
#! 4. Averiguar la utilidad de los parámetros `ci` y `estimator`.


#### 2.2. Boxplot (https://seaborn.pydata.org/generated/seaborn.boxplot.html)

# Volvamos al dataset de vinos. Vamos a armar un nuevo dataset solo con los vinos de Argentina, Chile y España,
# pero esta vez sólo con las siguietnes variedades: 'Malbec', 'Red Blend' y 'Cabernet Sauvignon'.

lista_variedades = ['Malbec','Red Blend','Cabernet Sauvignon']
vinos = wine_reviews_filtradas[wine_reviews_filtradas['variety'].isin(lista_variedades)].dropna()
vinos.head()

# Queremos realizar un único gráfico que muestre el precio de los vinos en gráfico de cajas (boxplots) 
# para los 3 distintos paises y las 3 variedades de vinos. Debemos entonces usar el parámetro `kind='box'` 
# para determinar que queremos un gráfico de cajas y el parámetro `col='country'` 
# para indicar que queremos tantos ejes en el gráfico como valores distintos hay en el campo `country`.

sns.catplot(x="country", y="price", col="variety", kind='box' , data=vinos)
#sns.boxplot(x="country", y="price", data=vinos)

sns.catplot(x="country", y="price", col="variety", kind='box' , data=vinos[vinos['price'] < 100])

# **Ejercicios**:

# 1. En el último gráfico, era difícil visualizar bien los resultados debido a precios que eran mucho más grandes que los demás. ¿Cómo podría solucionar facilmente este problema? 
# 2. Averigüe cómo cambiar el gráfico si desea que los 3 ejes aparezcan apilados verticalmente en lugar de uno al lado del otro.
# 3. Averigüe cómo hacer un violin plot y conjeture en qué circunstancias podría ser de utilidad.

## 3. Histogramas: Graficar la distribución de una variable aleatoria

#?Seaborn posee una función para graficar la distribución de una variables aleatoria llamada `distplot()`. 
# La misma tiene tres parametros principales
#? * `hist`: Es el parametro que controlo si dibujamos o no el histograma (por default en `True`).
#? * `kde`: permite graficar un estimado de la distribución mediante una técnica llamada Kernel Density Estimation, 
# KDE para los amigos (por default en `True`).
#? * `rug`: Dibuja sobre el eje horizonal una pequeña linea por cada valor, esto se llama rugplot (por default en `False`).
#?Ademas también peude tomar el parámetro `bins`, con el cual determinamos al cantidad de barras del histograma.
#?Para el caso del dataset dataset Iris podriamos graficar, por ejemplo, la distribución del largo de los pétalos:


sns.distplot(iris_data['sepal_length'], hist=True, kde=True, rug=True)

sns.distplot(vinos[(vinos['variety'] == 'Malbec') | (vinos['variety'] == 'Red Blend')].price)
#sns.distplot(vinos[vinos['variety'] == 'Red Blend'].price)
#sns.distplot(vinos[vinos['variety'] == 'Cabernet Sauvignon'].price)

#plt.legend(['Malbec','Red Blend','Cabernet Sauvignon'])
plt.xlim(0,100)

# Otra función interesante de Seaborn es la función `jointplot()`, la cual grafica un scatterplot junto a dos histogramas, 
# uno para cada una de las variables. 
# Dejamos un ejemplo de su uso en el iris dataset,
# y pueden recurrir a su documentación para mas detalles:
# https://seaborn.pydata.org/generated/seaborn.jointplot.html?highlight=jointplot#seaborn.jointplot

sns.jointplot(x="sepal_length", y="petal_length", marginal_kws=dict(bins=15, rug=True), data=iris_data)

# **Ejercicios**:

# 1. Genere un nuevo dataset a partir del dataset de vinos original (wine_reviews) que contenga sólo los vinos cuya variedad es Pinot Noir.
# 2. Descarte de este dataset las instancias que contengan un `NaN` en alguno de sus campos.
# 3. Descarte del dataset los vinos con un precio mayor a 200. Para esto pueden generarse una máscara.
# 4. Graficar en Seaborn un `distplot` con los precios de vinos que contenga el histograma, el KDE y el rugplot.

## 4. Pairplots (https://seaborn.pydata.org/generated/seaborn.boxplot.html)

# La función `pairplot()` de Seaborn será utilizada reiteradas veces durante la cursada, 
# ya que resulta muy cómoda para hacer una primera inspección de un dataset.
# La misma genera una grilla de N x N ejes, 
# donde N es el número de variables numéricas que tiene el dataset (features que toman valores numéricos). 
# Para cada par de variables numéricas, genera un scatterplot y en la diagonal grafica la distribucion de esos valores.
sns.pairplot(data=iris_data)

# Además, podemos diferenciar los datos según alguna de las variables categóricas del dataset mediante el parámetro `hue`. 
# Esto resulta particularmente útil en el caso que querramos usar las variables numericas con el fin de predecir esta varaible categórica
# (ya desarrollaremos esta idea en las próximas clases).

sns.pairplot(data=iris_data, hue="species")

#**Ejercicios:**

#1. Graficar un `pairplot` para el dataset de vinos reducido (3 paises y 3 variedades). Antes de hacerlo, ¿cuantas filas y cuantas columans espera que tenga este gráfico?
#2. Graficar el mismo `pairplot`, pero esta vez distinga los datos según variedad.
#3. Idem al punto anterior, pero distinga según país.

## 5. Heatmaps (y correlación)

# Correr la siguiente celda y googlear: ¿Qué es un heatmap?¿Cómo se hacen en Seaborn?¿Qué hace la función `corr()` de Pandas?
# ¿Cuáles son sus parámetros?¿Qué hace el parámetro `method`? Interpretar el gráfico obtenido.

corr = iris_data.drop(columns = 'species').corr()  #is used for find corelation
plt.figure(figsize=(8,8))
sns.heatmap(corr, cbar = True,  square = True, annot=True, fmt= '.2f',annot_kws={'size': 15},
           xticklabels= iris_data.drop(columns = 'species').columns, 
           yticklabels= iris_data.drop(columns = 'species').columns,
           cmap= 'coolwarm')
plt.xticks(rotation = 45)
plt.yticks(rotation = 45)
plt.show()

sns.pairplot(data=iris_data, hue="species")


###? PYTHON Y SEABORN 
#? https://www.absentdata.com/how-to-user-python-and-power-bi/#:~:text=The%20addition%20of%20Python%20integration%20in%20Power%20BI,also%20utilize%20some%20of%20the%20machine%20learning%20packages.