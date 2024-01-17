import json
d = '{"course": "Python", "fees": 2000,"duration": "2 months"}'

x = json.loads(d)   

print(x)
print(type(x))