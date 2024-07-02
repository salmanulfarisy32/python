car={
    "brand": "ford",
    "model": "mustang",
    "year": 1999
}
print(car)
#dictionary item
print(car["model"])
#length
print(len(car))
#type
print(type(car))
#accessing items
x=car["year"]
print(x)
#change values
car["year"]=2000
print(car)
#adding item
car["color"]="red"
print(car)
#removing item
car.pop("color")
print(car)
car.popitem()
print(car)
#for loop
car1={
    "brand": "ford",
    "model": "mustang",
    "year": 1999
}
for x,y in car1.items():
    print(x,y)
#copy
suv=car1.copy()
print(suv)


