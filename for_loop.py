'''l=[1,2,3,4,5]
for i in l:
    print(i)'''
    
'''s="harry"
for i in s:
    print(i)'''
    
'''
l=[1,2,3,4]
for i in l:
    print(i)
else:
    print("done")'''
    
#break
for  i in range(20):
    if(i==3):
        break
    print(i)
    
#continue
for  z in range(20):
    if(z==3):
        continue
    print(z)
    
#table  
z=int(input("Enter the number="))
for i in range(1,11):
    print(f"{z} * {i} = {z*i}")
    
    
#reverse table
z= int(input("Enter the number="))
for i in range(10,0,-1):
    print(f"{z} * {i} = {z*i}")    
    