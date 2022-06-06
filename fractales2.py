import matplotlib.pyplot as plt
import numpy as np

def get_iter(c:complex, thresh:int =4, max_steps:int =25) -> int:
    # Z_(n) = (Z_(n-1))^2 + c
    # Z_(0) = c
    z=c
    i=1
    while i<max_steps and (z*z.conjugate()).real<thresh:
        z=z*z +c
        i+=1
    return i

def plotter(dim, thresh, max_steps=25):
    n = dim[0]
    xi = dim[1]
    yi = dim[2]
    d = dim[3]
    mx = 2.48 / (n-1)
    my = 2.26 / (n-1)
    mapper = lambda x,y: (mx*x - 2, my*y - 1.13)
    
    img=np.full((d,d), 255)
    for x in range(xi, (xi + d)):
        for y in range(yi, (yi + d)):
            it = get_iter(complex(*mapper(x,y)), thresh=thresh, max_steps=max_steps)
            img[(y-yi)][(x-xi)] = 255 - it
    return img

n= [100, 0, 0, 100]
img = plotter(n, thresh=4, max_steps=30)
plt.imshow(img, cmap="plasma")
plt.axis("on")
plt.show()


n= [100, 50, 0, 50] #Nos movemos 50 en x (de izquierda a derecha) y 0 en Y (de arriba a abajo)
img = plotter(n, thresh=4, max_steps=30)
plt.imshow(img, cmap="plasma")
plt.axis("on")
plt.show()

import math 
plt.figure(figsize = (1000,1000))
detalle = 2000
sectores = 4 #Debe ser siempre divisible por 4
lado = math.sqrt(sectores)
delta = int(detalle / lado)
sec = np.arange(0, detalle, delta)

for i in range(sectores):
    plt.subplot(lado,lado,i+1)
    
    si = int(i/lado)
    sj = int(i%lado)
    
    n= [detalle, sec[sj], sec[si], delta]
       
    img = plotter(n, thresh=4, max_steps=20)
    
    #print('Sector: ' + str(i))
    #print('Fila: ' + str(sec[si]))
    #print('Columna: ' + str(sec[sj])) 
        
    plt.title('Sector: ' + str(i))
    plt.imshow(img, cmap="plasma")
    plt.axis("off")
    
plt.tight_layout()
plt.show()

n= [4000, 2000, 0, 2000]
img = plotter(n, thresh=4, max_steps=40)
plt.imshow(img, cmap="plasma")
plt.axis("on")
plt.show()

n= [8000, 6000, 0, 2000]
img = plotter(n, thresh=4, max_steps=40)
plt.imshow(img, cmap="plasma")
plt.axis("on")
plt.show()

n= [16000, 14000, 2000, 2000]
img = plotter(n, thresh=4, max_steps=40)
plt.imshow(img, cmap="plasma")
plt.axis("on")
plt.show()




# https://www.youtube.com/watch?v=MjKK0OqYFog
# https://www.youtube.com/watch?v=6phTUrBzngc