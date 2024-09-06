def square(fun):
    def inner():
        n = fun()  # Call the passed function and store the result in n
        return n * n  # Square the result
    return inner

def half(fun):
    def inner():
        n = fun()  # Call the passed function and store the result in n
        return n / 2  # Return half of the result
    return inner

@square
@half
def num():
    return 10  # This is the value returned by the function

# Call the function to see the output
print(num())  # This will now print the output after applying both decorators
