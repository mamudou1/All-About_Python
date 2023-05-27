"""
def my_func(f, arg):
  return f(arg)

my_func(lambda x: 2*x*x, 5)
"""
def poly(x):
    return x**2 + 5*x + 4
print(poly(4))

# lambda
print((lambda x:  x**2 + 5*x + 4)(4))