# sum 1st n natural numbers using while loop
n = int(input("Enter a number:"))
i=1
sum = 0
while(i<=n):
    sum += i
    i+=1

print(sum)