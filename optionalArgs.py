def myfun(x, *args, **kwargs):
     print(x)
     for each_arg in args:
         print(each_arg)
     for key, value in kwargs.items():
         print(key, value)


myfun(10,20,30,40, name= "Deva", salary = 10000000)