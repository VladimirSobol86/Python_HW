def reverse(**kwargs):
    dict = kwargs
    print(dict)
    return {value if value.__hash__ is not None else str(value):key for key,value in kwargs.items()}
               
print(reverse(arg1="qwerty",arg2="vtoroi arg",arg3=[1,2,3],arg4=4444,arg5=12345))