from itertools import *

print("""************************************************************

Transactions:

1-Show list elements

2-Add element

3-Calculate the maximum value

4-Delete element


Press q to exit


************************************************************""")


class algorithm():

    def __init__(self,name_list=["x","y" ,"z"],weight_list=[5,7,3],price_list=[100,150,70],true_weight_list=[] #Burda bana verilen temel değerleri girdim
                 ,final_list=[]
                 ):
        self.name_list=name_list #Listeleri ilerde kullanmak için self. methoduyla tanımlıyorum
        self.weight_list=weight_list
        self.price_list=price_list  
        self.true_weight_list = true_weight_list
        self.main_list = list(zip(self.name_list, self.weight_list, self.price_list))
        self.final_list=final_list
 
    def possibilities(self):
        a = self.weight_list
        i = 0
        try:
            number=int(36//int(min(self.weight_list)))#Burda ağırlık listesindeki en küçük değeri 36 ya tam bölerek en fazla hangi sayının tekrar edeceğini buluyorum
            while (int(i) <= int(number)):
                l = list(combinations_with_replacement(a, i + 1))#Tüm olasılıkları alıyorum eski kodda olduğu gibi
                for eleman in l:
                    if int(sum(eleman) <= 36):
                        self.true_weight_list.append(eleman)#Toplamı 36yı geçmeyen değerleri gerçek ağırlık listesine atıyorum 
                i += 1
        except ZeroDivisionError:
            print("ZeroDivisionError")
        return


    def ekle(self,name,weight ,price):#Burda aldığım değerleri listelere ekliyorum ve ilerde işlemde kullanmak için verilen değerleri self. methodu kullanarak tanımlıyorum
        self.new_weight = int(weight)
        self.new_price = int(price)
        self.name_list.append(name)
        self.weight_list.append(self.new_weight)
        self.price_list.append(self.new_price)
        self.main_list = list(zip(self.name_list, self.weight_list, self.price_list))
        print("Addition completed.")
        return self.main_list

    def delete_element(self,name):
        print("First List:",self.main_list)#Kişiden aldığım ismi ana listeden siliyorum
        for i in self.main_list:
            i=list(i)
            if (name == i[0]):
                i=tuple(i)
                self.main_list.remove(i)
                print("Final List:",self.main_list)


    def show_elements(self):
        print(self.main_list)

    def deneme(self):
        for i in self.true_weight_list:#Burda verilen temel değerleri olasılıklar içinden sayıp değerleriyle çarpıyorum
            count_five = i.count(5)
            count_three = i.count(3)
            count_seven = i.count(7)
            self.final_list.append((count_three * 70) + (count_seven * 150) + (count_five * 100))
            if (len(self.weight_list)>3):#Burda eğer temel değerler harici değer girilirse yukarda self. methodu kullanarak alınan yeni değerleri saydırıp hesaplatıyorum
                count_five = i.count(5)
                count_three = i.count(3)
                count_seven = i.count(7)
                count_new= i.count(self.new_weight)
                self.final_list.append(
                    (count_three * 70) + (count_seven * 150) + (count_five * 100) + (count_new * self.new_price))
        print(max(self.final_list))

Algorithm=algorithm()


while True:
    transaction=input("Please enter your transaction:")
    if (transaction =="q"):
        break
    elif(transaction =="1"):
        Algorithm.show_elements()
    elif(transaction=="2"):
        name=input("Please enter name:")
        weight = input("Please enter weight:")
        price= input("Please enter price:")
        Algorithm.ekle(name,weight,price)
    elif (transaction == "3"):
        Algorithm.possibilities()
        Algorithm.deneme()
    elif (transaction == "4"):
        name = input("Please enter the value you want to delete:")
        Algorithm.delete_element(name)
    else:
        print("Invalid transaction")
