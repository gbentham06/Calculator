import re
from Basicfuncs import *

def tokenise(expr):
  expr = expr.replace(" ", "")
  pattern = r'''
      (?<!\w)-?\d+\.\d+ |      # Floating points
      (?<!\w)-?\d+       |     # Integers
      [a-zA-Z_][a-zA-Z0-9_]* | # Functions/variables
      [+\-*/^(),]              # Operators and parentheses
  '''
  tokens = re.findall(pattern, expr, re.VERBOSE)
  return tokens


def postfix_notation(tokens):  # renamed param to tokens for clarity
  precedence = {'+': 2, '-': 2, '*': 3, '/': 3, '%': 3, '^': 4}
  operators = []
  output = []

  def get_precedence(op):  # prevents key error with '('
    return precedence[op] if op in precedence else 0

  def is_function(token):
    return token.isalpha() and token not in precedence and token not in ('(', ')')

  def is_constant(token):
    return token.upper() == 'PI' or token.upper() == 'E'

  def is_number(token): # checks if a token is a number
    try:
      float(token)
      return True
    except ValueError:
      return False

  while tokens:
    token = tokens.pop(0) # pops from left to right

    if is_number(token) or is_constant(token):
      output.append(token)

    elif is_function(token):
      operators.append(token)

    elif token.isidentifier(): # handles variables etc..
      output.append(token)

    elif token in "+-*/^%":
      while operators and get_precedence(token) <= get_precedence(operators[-1]):
        output.append(operators.pop())
      operators.append(token)

    elif token == '(':
      operators.append(token)

    elif token == ')': # pops through operator for bidmas/pemdas
      while operators:
        top = operators.pop()
        if top == '(':
          break
        output.append(top)
      else:
        raise ValueError("Mismatched parentheses: missing '('")

      if operators and is_function(operators[-1]):
        output.append(operators.pop())

  while operators:
    op = operators.pop()
    if op in '()':
      raise ValueError("Unbalanced parentheses")
    output.append(op)

  return output


def calculate(rpn):
  stack = []
  bin_opers = {
    '+':lambda x, y: x + y,
    '-':lambda x, y: x - y,
    '*':lambda x, y: x * y,
    '/':lambda x, y: x / y,
    '%':lambda x, y: x % y,
    '^':lambda x, y: x ** y
  }

  unary_opers = {
    'sin':lambda x: sin(x),
    'cos':lambda x: cos(x),
    'tan':lambda x: tan(x),
    'log':lambda x: log(x),
    'abs':lambda x: abs(x),
    'sqrt':lambda x: sqrt(x),
    'ln':lambda x: ln(x)
  }

  consts = {
    'PI':PI,
    'E':E
  }

  stack = []
  for token in rpn:

    if token in bin_opers: # handles binary ops
      a = stack.pop()
      b = stack.pop()
      stack.append(bin_opers[token](b, a))

    elif token in unary_opers: # handles unary ops
      a = stack.pop()
      stack.append(unary_opers[token](a))

    elif token.upper() in consts: # handles constants
      stack.append(consts[token.upper()])

    else:
      stack.append(float(token)) # handles numbers
  return stack[0] if stack else None


def basic_calc(expression):
    return calculate(postfix_notation(tokenise(expression)))
