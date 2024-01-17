mystudents={
    "stud" :{
        "name" : "Sachin",
        "year" : 2003
    },
    "stud2": {
    "name": "Laxman",
    "year" : 2007
    },
    "stud3": {
        "name": "Rahul",
        "year": 2008
    }
    
}

print(mystudents["stud"]["name"])
print()
for x , y in mystudents.items():
    print(x,y)
    
    