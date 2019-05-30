import random

turns = 10000
count = 990

a=[]
b=[]

while count>0:
    win = 0
    win_subs = 0
    
    for i in range(turns):
        car = random.choice(range(3))
        choose = random.choice(range(3))
        if car != choose:
            win_subs += 1
        else:
            win += 1
    
    b.append(win)
    a.append(win_subs)
    count -= 1

print("Trocando")
p = 0
for num in a:
   p += num 
print("A media foi de :",p/len(a), "desvia:", abs(p/len(a)-2*turns/3))

print()

print("Mantendo")
q = 0
for num in b:
   q += num
print("A media foi de :",q/len(b), "desvia:", abs(q/len(b)-1*turns/3))
