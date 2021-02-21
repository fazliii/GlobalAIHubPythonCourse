liste=[]
liste1=[]

def prime_first():


 for sayi in range(500):  
   if sayi > 1:  
       for i in range(2,sayi):  
           if (sayi % i) == 0:  
               break  
       else:               
                  liste.append(sayi) #Asal sayıları listeme ekledim
 return ("0-500 arasindaki asal sayilar: ", liste)
   

               
def prime_second():
    

 for sayi in range(500,1000):  
   if sayi > 1:  
       for i in range(2,sayi):  
           if (sayi % i) == 0:  
               break  
       else:               
                  liste1.append(sayi) #Asal sayıları listeme ekledim
 return ("500-1000 arasindaki asal sayilar: ", liste1)

print("\n",prime_first())
print("\n",prime_second())
