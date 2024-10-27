import random

jurnal=[]

for i in range(5):
    x=random.randint(2,5)
    jurnal.append(x)

print(sum(jurnal)/(i+1)) 
print(jurnal) 
jurnal.insert(3, 5)
print(jurnal[1])
jurnal.pop(1)
x = jurnal.count(5)
print(jurnal)
print(x)
