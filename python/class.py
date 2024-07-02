#create class
class sum:
    x = 5

print(sum)

#crete object
class num:
    x=5
p1=num()
print(p1.x)

class person:
    def __init__(self,name,age,location):
        self.name=name
        self.age=age
        self.location=location

p1=person("salman",21,"iringal")
print(p1.name)
print(p1.age)
print(p1.location)
