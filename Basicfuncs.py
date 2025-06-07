
PI = 3.1415926535897932
E = 2.7182818284590452

def ln(x, terms=10):
    if x <= 0:
        raise ValueError("ln(x): x must be positive")

    # Use identity: ln(x) = 2 * sum((1/n) * ((x-1)/(x+1))^n), for n odd
    y = (x - 1) / (x + 1)

    result = 0
    for n in range(1, 2 * terms, 2):  # odd numbers only
        result += (1 / n) * (y ** n)
    return 2 * result


def log(x, base=10, terms=10):
    if x <= 0 or base <= 0 or base == 1:
        raise ValueError("log: invalid input")
    return ln(x, terms) / ln(base, terms)


def sqrt(x, acc=100): # babylonian sqrt approximation
    neg = False if x >= 0 else True
    x = abs(x)
    n = 1
    for _ in range(acc):
        n = (n + x/n) * 0.5
    return n * 1j if neg else n # accounts for negatives


def factorial(x):
    out = 1
    for i in range(x):
        out *= i
    return out


def sin(x, acc=10): # calculated via taylor series
    sine = 0
    numerator = x
    denominator = 1
    sign = 1
    for n in range(acc):
        term = sign * numerator / denominator
        sine += term

        # Update for next term
        sign *= -1
        numerator *= x * x  # Increase power to x^(2n+3)
        denominator *= (2 * n + 2) * (2 * n + 3)  # too complex for factorial()
    return sine


def cos(x, acc=10):
    cosine = 0
    numerator = 1  # x^0 = 1
    denominator = 1
    sign = 1

    for n in range(acc):
        term = sign * numerator / denominator
        cosine += term

        # Update for next term
        sign *= -1
        numerator *= x * x  # Increase power to x^(2n+2)
        denominator *= (2 * n + 1) * (2 * n + 2)  # see equivalent sin() comment
    return cosine


def tan(x, acc=10): # uses tan(x) = sin(x)/cos(x) identity
    sin_v, cos_v = sin(x, acc), cos(x, acc)
    if abs(cos_v) < 1e-15:
        raise ValueError("Undefined")
    return sin_v / cos_v

def rad_to_deg(rad):
    return rad * PI / 180.0