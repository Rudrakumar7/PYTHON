# WAP to accept marks of 6 subjects and display them in sorted manner.
Marks = []

f1 = int(input("Enter Marks  :"))
Marks.append(f1)
f2 = int(input("Enter Marks  :"))
Marks.append(f2)
f3 = int(input("Enter Marks  :"))
Marks.append(f3)
f4 = int(input("Enter Marks  :"))
Marks.append(f4)
f5 = int(input("Enter Marks  :"))
Marks.append(f5)
f6 = int(input("Enter Marks  :"))
Marks.append(f6)

Marks.sort()
print(Marks)