thisDict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}

thisDict.pop("model")

print(thisDict)


thisDict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}

thisDict.popitem()
print(thisDict )


# del thisDict["brand"]
# print(thisDict)

thisDict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}

thisDict.clear()
print(thisDict)