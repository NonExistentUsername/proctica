from readers import *
from converters import *
from computing import *

calculator = RelativeFrequencies()

converter = SimpleConverter()

reader = SimpleReader()

print(converter(reader()))

a = calculator(converter(reader()))

print(a)

a, b = [1, 2]

print(a)
print(b)