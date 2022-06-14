from abc import abstractclassmethod
from functools import reduce

class StatisticalDistribution:
    @abstractclassmethod
    def __call__(self, data: list) -> dict:
        pass

class RelativeFrequencies(StatisticalDistribution):
    def __init__(self) -> None:
        super().__init__()
    
    def __call__(self, data: list) -> dict:
        n = sum(map(lambda a: a[1], data))
        result = []
        for k, v in data:
            result.append((k, v / n))
        return result

class CumulativeFrequencies(StatisticalDistribution):
    def __init__(self) -> None:
        super().__init__()
    
    def __call__(self, data: list) -> dict:
        n = sum(map(lambda a: a[1], data))
        result = []
        i=0
        for k, v in data:
            result.append((k, i))
            i = + v
        return result