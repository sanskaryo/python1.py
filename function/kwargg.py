def info(*args,**kwargs):
    for key, value in kwargs.items():
        print(key,value)
    print(args)
        
info (1,2, name="samay",age=17,passion="calligraphy \n")
info (name="Hina",age=19,passion="classical music")