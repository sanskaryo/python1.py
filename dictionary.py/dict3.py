car={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
    
}

x = car.keys()  #car_values

print(x) #before the change 
car["color"]="red"
print(car)
print(x)
print()
thisDict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964   
}

x = thisDict.items()

print(x)
print()
print(thisDict)