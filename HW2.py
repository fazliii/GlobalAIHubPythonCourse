listeisim=[]
listesoyisim=[]
listenot=[]
listeort=[]
information={}
dic1={}


for i in range(5):

  Isim=input("İsmi Gir : ")
  Soyisim=(input("Soyismi Gir: "))
  listeisim.append(Isim)
  listesoyisim.append(Soyisim)

  midterm=float(input("Midterm notu gir :"))
  listenot.append(midterm)
  final=float(input("Final notu gir :"))
  listenot.append(final)
  homework=float(input("Homework notu gir :"))
  listenot.append(homework)
  ortalama=((midterm+final+homework)/3)
  listeort.append(ortalama)
  #dic[listeisim[i]] = listenot[i]
  information["ögrenci {}".format(i+1)] = {(listeisim[i]+" "+listesoyisim[i]):[str(midterm),str(final),str(homework)]}
  dic1 = {"str(ortalama)":[listeisim[i]+""+listesoyisim[i]]}
  maxort=max(listeort)
  maxindex = listeort.index(maxort)



print("\n İsimler : ",listeisim)
print("\n Soyisimler : ",listesoyisim)
print("\n not {}".format(listenot))
print("\n ortalama {}".format(listeort))
print("\n",information)
print("\n Max. Ortalama: ",maxort)
print("\n\n Tebrikler ",(dic1.get(maxort,listeisim[maxindex]+" "+listesoyisim[maxindex]).upper())+"\n")