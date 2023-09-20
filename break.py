list1=["hi","hola","namaste"]
name1=["shailesh","kartik","shubhang"]
for item in list1:
    for name in name1:
        print(item,name)
        if item=="hola" and name=="shubhang":
            break
    print("out from inner loop")  
print("out from outer loop")      