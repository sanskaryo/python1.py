def modify_dict(d):
    d['new_key'] = 'new_value'
    print("Inside the Function", d)
    
    
my_dict = {'key': 'value1' , 'key2' : 'value2'}
modify_dict(my_dict)
print("outside the dict", my_dict)