import random as rnd

alt = 1 
ust = 100
liste=[]

for sayi in range(alt,ust+1):  
    #Alt ve üst değerlerimin arasındaki sayıları kontrol ettirdim.
   if sayi > 1:  
       for i in range(2,sayi):  
           if (sayi % i) == 0:  
               break  
       else:               
                  liste.append(sayi) #Asal sayıları listeme ekledim

for i in range(1):        
  for j in range(3):
     print("      ",rnd.sample(set(liste), 3)) 
   #Random değerleri birbirinden farklı olacak şekilde liste olarak yazdırdım.   