
num=int(input("Enter the number:"))
if(num%2==0):
    print("This is even number")
else:
    print("This is odd number")
    
    
    
#another way
num=int(input("Enter the number:"))
if(num%2==0):
    if(num>0):
        print("This is positive even number")
    elif(num<0):
        print("This is negative even number ")
    elif(num==0):
        print("This is zero which is even number")
else:
        print("This is an odd number")