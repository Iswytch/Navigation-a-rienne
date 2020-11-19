from math import *
import matplotlib.pyplot as plt


def degreToRadiant(pointDegre):
    return radians(pointDegre)


def radiantToDegre(pointRadiant):
    return degrees(pointRadiant)


def calculDistanceOrtho(latM, longM, latN, longN):
    return acos(sin(latM)*sin(latN)+cos(latM)*cos(latN)*cos(longM-longN))
    
    
def calculDistanceLoxo(latPt, longPt, latPtArrive, longPtArrive):
    suiteFormule = log ( tan ( ( 2 * latPtArrive + pi ) / 4 ) ) - log ( tan ( ( 2 * latPt + pi ) / 4 ) ) 
    ArcAB = ( latPtArrive - latPt ) / ( cos ( atan ( ( longPtArrive - longPt ) / suiteFormule ) ) )
    return 6371 * abs(ArcAB)


def calculCap(latM, longM, latN, longN, distance, estOuOuest):
    V=(sin(latN)-sin(latM)*cos(distance))/(cos(latM)*sin(distance))
    if estOuOuest(longPt,longPtArrive)=="e":
        return acos(V)
    elif estOuOuest(longPt,longPtArrive)=="o":
        return 2*pi*(-acos(V))
    else:
        exit()
    
    
def latNextPoint(latM, longM, capInitial, l):
    Q = pi/(1.852*60*180)
    return latM+cos(cap)*l*Q
    
def longNextPoint(latM, longM, capInitial, l):
    Q = pi/(1.852*60*180)
    return longM+sin(cap)/cos(latM)*l*Q


def estOuOuest(longPt,longPtArrive):
    if(longPt<longPtArrive):
        print("on va de l'ouest vers l'est")
        return "e"
    else:
        print("on va de l'est vers l'ouest")
        return "o"
        
    

im = plt.imread("equi.jpg")

#Point de départ
#latPt = float(input("Entrez la latitude du point de départ : "))
#longPt = float(input("Entrez la longitude du point de départ : "))

#Point d'arrivé
#latPtArrive=float(input("Entrez la latitude du point d'arrivé : "));
#longPtArrive=float(input("Entrez la longitude du point d'arrivé : "));


#Distance à parcourir entre les 2 points

l = 100
latPt = 48.8534
longPt =  2.3488
latPtArrive = 35.689487
longPtArrive = 139.691706


distanceOrtho = 0
i=0
listeLat = []
listeLong = []

latPt = degreToRadiant(latPt)
longPt = degreToRadiant(longPt)
latPtArrive = degreToRadiant(latPtArrive)
longPtArrive = degreToRadiant(longPtArrive)





# Distance loxodromique

distanceLoxo = calculDistanceLoxo(latPt, longPt, latPtArrive, longPtArrive)
print("Distance loxodromique = ",distanceLoxo)




# Distance orthodromique

distance=calculDistanceOrtho(latPt, longPt, latPtArrive, longPtArrive)
cap=calculCap(latPt, longPt, latPtArrive, longPtArrive, distance, estOuOuest)


print("Cap initial = ",(radiantToDegre(cap))%360) 

longPtSuivant=longNextPoint(latPt, longPt, cap, l)
latPtSuivant=latNextPoint(latPt, longPt, cap, l)      


check=True

while check:
    
     print("latPt = ",(round(radiantToDegre(latPt),1)))
     print("longPt = ",(round(radiantToDegre(longPt),1)))
     print("latPtArrive = ",(round(radiantToDegre(latPtArrive),1)))
     print("longPtArrive = ",(round(radiantToDegre(longPtArrive),1)))
           
     #TODO changer et mettre des degre?
     if (round(latPt,1)==round(latPtArrive,1) and round(longPt,1)==round(longPtArrive,1)or i>1000):
        check=False
           
     i=i+1;
    
     coordXCarte=512.5-((512.5*radiantToDegre(latPt))/90)
     coordYCarte=1024+((1024*radiantToDegre(longPt))/180)
     listeLat.append(coordXCarte)
     listeLong.append(coordYCarte)


     distanceOrtho=distanceOrtho+calculDistanceOrtho(latPt, longPt, latPtSuivant, longPtSuivant)
    
     latPt=latPtSuivant
     longPt=longPtSuivant
   
     longPtSuivant=longNextPoint(latPtSuivant, longPtSuivant, cap, l)
     latPtSuivant=latNextPoint(latPtSuivant, longPtSuivant, cap, l)
     
     distance=calculDistanceOrtho(latPt, longPt, latPtArrive, longPtArrive)
     
     cap=calculCap(latPt, longPt, latPtArrive, longPtArrive, distance, estOuOuest)
    

    
     

print("Distance orthodromique = ",distanceOrtho*6371)


plt.scatter(x=[listeLong], y=[listeLat], c='r', s=10)


implot = plt.imshow(im)
