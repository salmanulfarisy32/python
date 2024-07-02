fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[x for x in fruits if "a" in x]
print(newlist)
#not apple
newlist=[x for x in fruits if x!="apple"]
print(newlist)
#no if statement
newlist=[x for x in fruits]
print(newlist)
#range()
newlist=[x for x in range(10)]
print(newlist)
range with condition
newlist=[x for x in range(10) if x<9]
print(newlist)
