#taille image = (1025, 2048)

#paris = 48.8534, 2.3488
#tokyo = 35.689487, 139.691706
#new york = 40.7808, -73.9772
#le cap = -33.908736, 18.414032
#mexico = 19.724695, -99.407723
#punta arenas = -52.859958, -22.870934

import matplotlib.pyplot as plt
im = plt.imread("equi.jpg")


latPt = float(input("Entrez la latitude du point : "))
longPt = float(input("Entrez la longitude du point M : "))


x=1024+((1024*longPt)/180)
y=512.5-((512.5*latPt)/90)


print("x = ",x)
print("y = ",y)

plt.scatter(x=[x], y=[y], c='r', s=10)


implot = plt.imshow(im)