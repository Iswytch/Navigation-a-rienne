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
        return 2*pi-acos(V)
    else:
        exit()
    
    
def latNextPoint(latM, longM, capInitial, l):
    Q = pi/(1.852*60*180)
    return latM+cos(cap)*l*Q
    
def longNextPoint(latM, longM, capInitial, l):
    Q = pi/(1.852*60*180)
    return longM+sin(cap)/cos(latM)*l*Q


def estOuOuest(longPt,longPtArrive):
    if calculDistanceLoxo(latPt, longPt, latPtArrive, longPtArrive) > 12500:
        if(longPt<longPtArrive):
            return "o"
        else:
            return "e"
    else:
        if(longPt<longPtArrive):
            return "e"
        else:
            return "o"
        
    

im = plt.imread("equi.jpg")

#Point de départ
# latPt = float(input("Entrez la latitude du point de départ : "))
# longPt = float(input("Entrez la longitude du point de départ : "))

# #Point d'arrivé
# latPtArrive=float(input("Entrez la latitude du point d'arrivé : "));
# longPtArrive=float(input("Entrez la longitude du point d'arrivé : "));


#Distance à parcourir entre les 2 points

l = 100
latPt= 40.8822860825291
longPt= -73.71750689359394
latPtArrive= 35.70503419924903
longPtArrive=139.80218267578786
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
print("")
print("")
print("Distance loxodromique = ",distanceLoxo)




# Distance orthodromique

distance=calculDistanceOrtho(latPt, longPt, latPtArrive, longPtArrive)
cap=calculCap(latPt, longPt, latPtArrive, longPtArrive, distance, estOuOuest)




print("Cap initial = ",(radiantToDegre(cap))%360) 



#Boucle permettant de calculer la distance orthodromique

longPtSuivant=longNextPoint(latPt, longPt, cap, l)
latPtSuivant=latNextPoint(latPt, longPt, cap, l)      
check=True


while check:
    
     print("latPt = ",(round(radiantToDegre(latPt),1)))
     print("longPt = ",(round(radiantToDegre(longPt),1)))
     print("latPtSuivant = ",(round(radiantToDegre(latPtSuivant),1)))
     print("longPtSuivant = ",(round(radiantToDegre(longPtSuivant),1)))
     print("latPtArrive = ",(round(radiantToDegre(latPtArrive),1)))
     print("longPtArrive = ",(round(radiantToDegre(longPtArrive),1)))
     print("--------------------------------------------------")
           
     if (round(latPt,1)==round(latPtArrive,1) and round(longPt,1)==round(longPtArrive,1)or i>150):
        check=False
           
     i=i+1;
    
     coordXCarte=512.5-((512.5*radiantToDegre(latPt))/90)
     coordYCarte=1024+((1024*radiantToDegre(longPt))/180)
     listeLat.append(coordXCarte)
     listeLong.append(coordYCarte)


     distanceOrtho=distanceOrtho+calculDistanceOrtho(latPt, longPt, latPtSuivant, longPtSuivant)
    
    
    
    
     #Check si il faut faire le tour de la carte et le fait si il faut
     
     if(latPtSuivant>degreToRadiant(90)):
         latPtSuivant=latPtSuivant-degreToRadiant(180)
     else:
         latPt=latPtSuivant
         
     if(latPtSuivant<degreToRadiant(-90)):
         latPtSuivant=latPtSuivant+degreToRadiant(180)
     else:
         latPt=latPtSuivant

     
     if(longPtSuivant>degreToRadiant(180)):
         longPtSuivant=longPtSuivant-degreToRadiant(360)
     else:
         longPt=longPtSuivant
         
     if(longPtSuivant<degreToRadiant(-180)):
         longPtSuivant=longPtSuivant+degreToRadiant(360)
     else:
         longPt=longPtSuivant
   
    
   
    
   
     longPtSuivant=longNextPoint(latPtSuivant, longPtSuivant, cap, l)
     latPtSuivant=latNextPoint(latPtSuivant, longPtSuivant, cap, l)
     
     distance=calculDistanceOrtho(latPt, longPt, latPtArrive, longPtArrive)
     
     cap=calculCap(latPt, longPt, latPtArrive, longPtArrive, distance, estOuOuest)
    

    
     

print("Distance orthodromique = ",distanceOrtho*6371)


plt.scatter(x=[listeLong], y=[listeLat], c='r', s=10)


implot = plt.imshow(im)
