# spam detection if following messg is their "makes a lot of money ......"
p1 = "Makes a lot  of money"
p2 = "buy now "
p3 = "subscribe this "
p4 = "click this"

message  = input("Enter a comment :")

if ((p1 in message) or (p2 in message) or (p3 in message)):
    print("This comment  is a spam")

else:
    print("This comment is not a spam")