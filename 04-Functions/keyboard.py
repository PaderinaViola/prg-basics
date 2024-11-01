###
# Functions to read any data type from the keyboard
#
def input_string(message):
    string_a = input(message)
    return string_a

def input_integer(message):
    integer = int(input(message))
    return integer

def input_real(message):
    real = float(input(message))
    return real

def input_boolean(message):
    boolean = input(message)
    if boolean == 'y':
        return True
    elif boolean == 'n':
        return False

