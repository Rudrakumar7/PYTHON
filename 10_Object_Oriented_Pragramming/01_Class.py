class Employee:
    language = "py" #This is a  class attribute
    Salary = 120000 

rudra  = Employee()
rudra.name = "Rudra"  #This is an instance  attribute
print(rudra.name , rudra.language , rudra.Salary )

ritu = Employee()
ritu.name = "Ritu"
print(ritu.name , ritu.language , ritu.Salary )

#here name is instance attribute and salary and language attributes as they directly belong to the class 