friends = ["Apple", "Orange " , 5 , 345.06, False , "Aakash"  ," Rohan"]
print(friends)
print(friends[0])
friends[0]="Grapes"#Unlike Strings  lists are mutable

print(friends[0])
print(friends[1:4])

friends.append("Rudra")

l1 = [1,32,53,5,4,22,6]
l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.insert(3,50)
print(l1)

value = l1.pop(3)
print(value)
print(l1)

l1.remove(32)
print(l1)
