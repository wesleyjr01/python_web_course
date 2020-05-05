# What are Python Decorators?
* A decorator is a function that returns another function, and the inner function runs the function that was passed to the decorator as an argument.
* It allows us to extend the original function with extra things. A decoratir is for extending the functionality of na existing function. Example:
```
user = {"name":"Rolf", "password":"1234", "acess_level":"admin"}

def my_function():
    return "Password for admin panel is 1234."

def user_has_permission(func):
    def inner_func(func):
        if user["acess_level"] == "admin":
            return func()
    return inner_func

my_function = user_has_permission(my_function)
my_function()
```