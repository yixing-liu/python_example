import python_example as m

assert m.__version__ == '0.0.1'
print(m.__version__)
assert m.add(1, 2) == 3
print("m.add(100,200)=", m.add(100, 200))
assert m.subtract(1, 2) == -1
print("m.subtract(100,200)=", m.subtract(100, 200))
print(m.__doc__)
