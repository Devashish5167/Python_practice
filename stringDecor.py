def decorfun(fun):
    def inner(name):  # Accept the same argument as the original function
        result = fun(name)  # Pass the argument to the original function
        result += " How are you"
        return result
    return inner

@decorfun
def hello(name):
    return "Hello " + name

print(hello("John"))
