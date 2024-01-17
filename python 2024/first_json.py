import json
d= {
    
    'course': 'Python',
    'fees': '2,000',


}

f = json.dumps(d)

print(type(f))
print(f)
