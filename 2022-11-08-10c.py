a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
b = a.split(",")
print(b[1])
c = a[1]
print(c)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
