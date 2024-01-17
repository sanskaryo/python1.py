try:
    l=[1,5,7,6]
    i=int(input("enter the index : "))
    print(l[i])
except:
    print("some error occured")
finally:
    print("i always execute")