a = int(input("Enter  your Age:"))

#if statement no : 1
if(a%2==0):
    print("a is even")
#end of of statement no :1

#if statement no : 2
if (a>=18):
    print("You are above the age of  consent ")
    print("Good for you")

elif(a<0):
    print("You entering an invalid age")

elif(a==0):
    print("You entering 0 which is not a valid age")

else:
    print("You are below the age of  consent ")
#end of of statement no : 2


print ("End of program ")
