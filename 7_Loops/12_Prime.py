n = int(input("Enter a Number :"))


for i in range (2,n):
    if(n%i==0):
        print("Numner is not Prime")
        break
else:
    print("Number is Prime")