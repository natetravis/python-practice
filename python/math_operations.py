def addition(a, b):
    return a + b


def subtraction(x, y):
    return x-y


def multiplication(c, d):
    return c*d


def division(e, f):
    if f != 0:  # Avoid division by zero
        return e / f
    else:
        return "Division by zero is undefined"
