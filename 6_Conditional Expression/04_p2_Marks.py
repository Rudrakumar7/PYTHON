m1 =int(input("Enter Marks 1:"))
m2 =int(input("Enter Marks 2:"))
m3 =int(input("Enter Marks 3:"))

total_percen = (m1+m2+m3)/3

if(total_percen >=40 and m1>=33 and m2>=33 and m3>=33):
    print("You passed :",total_percen)
else:
    print("You failed , try next year :", total_percen)