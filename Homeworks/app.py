
import random
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
    while (i<=12):
        l = list(combinations_with_replacement(a,i+1))
        for eleman in l:
            if int(sum(eleman)<=36):
                weight_list.append(eleman)
        i += 1
    return
def deneme():
    for i in weight_list:
        i = list(i)
        count_five=i.count(5)
        count_three=i.count(3)
        count_seven=i.count(7)
        numbers_list.append((count_three*70)+(count_seven*150)+(count_five*100))
possibilities()
deneme()
print(max(numbers_list))























