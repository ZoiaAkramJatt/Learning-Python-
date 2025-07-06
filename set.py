
set1={1,2,3,4,5}
print(set1)

          #methods of set
#add
set1={1,2,3,4,5}
set1.add(55)
print(set1)

#add multiple set
set1={1,2,3,4}
set2={"apple","banana","cat"}
set3={98,87,54}
print(set1|set2|set3)#|this is an another addition sign in pyhton(add the sets)

#remove
set1={"apple","banana","cherry"}
set1.remove("banana")
print(set1)

#update
set1={"apple","banana","cherry"}
set2={"dragon fruit","mango"}
set1.update(set2)
print(set1)

#union
set1={"apple","banana","cherry",}
set2={"dragon fruit","apple","mango"}
set1.update(set2)
print(set1)

#intersection
set1={1,2,3,4,5}
set2={2,4,7,8,9}
print(set1.intersection(set2))

#use & to to find intersection
set1={1,2,3,8}
set2={2,5,7,8}
set3=set1 & set2
print(set3)

#Acess set
set1={1,2,3,4,5}
for x in set1:
  print(x)
  
#pop
set1={1,2,3,4}
print(set1.pop())