from readers import *
from converters import *
from computing import *

calculator = CumulativeFrequencies()

converter = SimpleConverter()

reader = SimpleReader()

print(converter(reader()))

a = calculator(converter(reader()))

print(a)
