#Öncelikle itertoolsla olasılıkları hesaplayıp boş bir listeye atan fonksiyon yazdım.Daha sonra bu listenin elemanlarını for döngüsüyle çağırıp içindeki elamanlarda kaç tane
#3,7 ve 5 olduğunu hesaplayıp bunu değerleriyle çarpıp hepsini topladım ve bunuda boş bir listeye attım sonra listedeki max değeri aldım.

from itertools import *
capacity = 36
x = {"kg":5,"price":100}
y = {"kg":7,"price":150}
z = {"kg":3,"price":70}
numbers_list=[]
weight_list= []
def possibilities():
    a = [x["kg"],z["kg"],y["kg"]]
    i=0
    while (i<=12):#i değerini 12ye kadar hesaplattım çünkü en fazla tekrar edecek olan sayı 3 ve max 12 kere tekrar edebilir.
        l = list(combinations_with_replacement(a,i+1))
        for eleman in l:
            if int(sum(eleman)<=36):#Burda olasılıklardaki değerlerin ağırlıkları toplamı 36'yı geçip geçmediğini kontrol ediyoruz
                weight_list.append(eleman)
        i += 1
    return
def deneme():
    for i in weight_list:#Ağırlık listesindeki 36'yi aşmayan değerli for döngüsüyle tekrar eden sayıları sayıp değerleriyle çarpıyoruz.Daha sonra fiyat listesine ekliyoruz.                               
        i = list(i)
        count_five=i.count(5)
        count_three=i.count(3)
        count_seven=i.count(7)
        numbers_list.append((count_three*70)+(count_seven*150)+(count_five*100))
possibilities()
deneme()
print(max(numbers_list))#Listeden max değeri çekiyoruz





