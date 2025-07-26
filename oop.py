class Student():
    def __init__ (self,name,grade,section,dept):
        self.name=name
        self.grade=grade
        self.section=section
        self.dept=dept
    
    def __str__ (self):
        return f"{self.name} is in  {self.grade} in {self.section} in {self.dept}"
    
dept1="Artificial intelligence"
dept2="Mbbs"
dept3="one class"
    
student1=Student("Zoia","second semester","A section",dept1)
student2=Student("Sidra","third year ","A section",dept2)
student3=Student("Hoorain fatima", 1 ,"E section",dept3)

print(student1)
print(student2)
print(student3)