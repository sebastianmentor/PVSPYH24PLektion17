my_int: int = 5
my_float: float = 5.5
my_str: str = "5"
MY_CONST_INT: int = 10
MY_CONST_FLOAT: float = 3.1415
MY_CONST_STR: str = "Hello!"


def multiply_and_add(number1: int, number2: int, number3: int) -> int:
    return number1 * number2 + number3


print(multiply_and_add(my_int, 2 * my_int, MY_CONST_INT))

print(multiply_and_add(my_int, my_int / 5, MY_CONST_INT))


def greet(name: str) -> str:
    return f"Hello there {name}"


print(greet("Sebastian"))
print(greet(my_float))
print(greet(23))


def random_function(variable):
    return f"{variable=}"


print(random_function("Hello there!"))
