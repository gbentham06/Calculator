
PI = 3.1415926535897932
E = 2.7182818284590452


def sqrt(x, acc=100): # babylonian sqrt approximation
    neg = False if x >= 0 else True
    x = abs(x)
    n = 1
    for _ in range(acc):
        n = (n + x/n) * 0.5
    return n * 1j if neg else n # accounts for negatives


def ln(x, tol=1e-12, max_terms=100):
    if x <= 0:
        raise ValueError("ln(x): x must be positive")

    # Transform x closer to 1 for better convergence
    k = 0
    while x > 1.5:
        x /= E
        k += 1
    while x < 0.7:
        x *= E
        k -= 1

    y = (x - 1) / (x + 1)

    result = 0
    term = 2 * y  # first term (n=1)
    n = 1
    while abs(term) > tol and n < max_terms:
        result += term
        n += 2
        term = 2 * (y ** n) / n

    return result + k  # ln(x * e^k) = ln(x) + k


def log(x, base=10, terms=10):
    if x <= 0 or base <= 0 or base == 1:
        raise ValueError("log: invalid input")
    return ln(x, terms) / ln(base, terms)


def factorial(x):
    out = 1
    for i in range(x):
        out *= i
    return out


def sin(x, acc=10): # calculated via taylor series
    x = x % (2 * PI)
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
    return sine if abs(sine) > 1e-5 else 0


def cos(x, acc=10):
    x = x % (2 * PI)
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
    return cosine if abs(cosine) > 1e-10 else 0


def tan(x, acc=10): # uses tan(x) = sin(x)/cos(x) identity
    sin_v, cos_v = sin(x, acc), cos(x, acc)
    if abs(cos_v) < 1e-15:
        raise ValueError("Undefined: too close to zero")
    return sin_v / cos_v

def rad_to_deg(rad):
    return rad * PI / 180.0

