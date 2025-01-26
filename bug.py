def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Unsupported operand type(s) for / ")
        return None

#Example of the error
result1 = function_with_uncommon_error(10, 2)  #Output 5.0
result2 = function_with_uncommon_error(10, 0)  #Output Error: Division by zero, None
result3 = function_with_uncommon_error(10, "hello") #Output Error: Unsupported operand type(s) for /, None