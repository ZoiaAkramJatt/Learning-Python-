def avg():
   a=int(input("Enter the number:"))
   b=int(input("Enter the number:"))
   c=int(input("Enter the number:"))
   
   average=(a+b+c)/3
   print( "The average number is:",average)

avg()
avg()
avg()


#write name of two person
def goodday(name):
    print("Hello ,how are you",name)
    
goodday("Zoia ")
goodday("sidra")


#write name with different fathername

def goodday(name,fathername):
    print("Hello ,how are you" ,name,fathername)
    
goodday("Zoia","Akram Ali")
goodday("Sidra","baba")


#write name with common father name and caste

def goodday(name,fathername="Akram Ali",caste="Jatt"):
    print("Nice to meet you",name,fathername,caste )
    
goodday("Zoia")
goodday("sidra")


#local variable
def greeting ():
    x=5
    print(x) 
greeting()

#lacal varaible
x=10
def zoia():
    print(x)
zoia()




x=" Zoia"
def myname():
    print("Nice to meet you",x)
myname()


x=" Zoia"
def myname():
    print()
myname()
print("Nice to meet you",x)




#local x    global x
x=" Zoia"
def myname():
    global x
myname()
print("Nice to meet you",x)





x="Zoia"
def myname():
    y="Akram Ali"
    print(x,y)
myname()

  # output Akram Ali
  #Zoia
x="Zoia"
def myname():
    y="Akram Ali"
    print(y)
myname()
print(x)
















    