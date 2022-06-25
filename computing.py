from abc import abstractclassmethod
import math

class StatisticalDistribution:
    @abstractclassmethod
    def __call__(self, data: list, n: int) -> dict:
        pass

class RelativeFrequencies(StatisticalDistribution):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, data: list, n: int) -> dict:
        return [(k, v / n) for k, v in data]

class CumulativeFrequencies(StatisticalDistribution):
    def __init__(self) -> None:
        super().__init__()
    
    def __call__(self, data: list, n: int) -> dict:
        result = []
        i = 0
        for k, v in data:
            result.append((k, i))
            i += v
        return result

class RelativeAccumulatedFrequencies(StatisticalDistribution):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, data: list, n: int) -> dict:
        result = []
        i = 0
        for k, v in data:
            result.append((k, i / n))
            i += v
        return result

class SelectiveAverage:
    def __call__(self, data: list, n: int) -> float:
        data.sort(key = lambda a: a[0])
        result = 0
        for k, v in data:
            result += k * v
        return result / n

class Dispersion:
    def __init__(self, selective_average_calculator = None) -> None:
        self.__selective_average_calculator = selective_average_calculator

    def __call__(self, data: list, n: int) -> float:
        if self.__selective_average_calculator:
            selective_average = self.__selective_average_calculator
        else:
            selective_average = SelectiveAverage()(data, n)
        result = 0
        for k, v in data:
            result += ((k - selective_average)**2)*v
        if n <= 30:
            result /= n - 1
        else:
            result /= n
        return result

class SelectiveStandardDeviation:
    def __init__(self, dispersion_calculator = None) -> None:
        self.__dispersion_calculator = dispersion_calculator
    
    def __call__(self, data: list, n: int) -> float:
        if self.__dispersion_calculator:
            dispersion = self.__dispersion_calculator(data, n)
        else:
            dispersion = Dispersion()(data, n)
        return math.sqrt(dispersion)

class SelectiveAverageR:
    def __init__(self, r: int = 1) -> None:
        self.__r = r
    
    def __call__(self, data: list, n: int) -> float:
        data.sort(key = lambda a: a[0])
        result = 0
        for k, v in data:
            result += (k**self.__r) * v
        return result / n

class DispersionR:
    def __init__(self, r: int = 1, selective_average_calculator = None) -> None:
        self.__r = r
        self.__selective_average_calculator = selective_average_calculator
    
    def __call__(self, data: list, n: int) -> float:
        if self.__selective_average_calculator:
            selective_average = self.__selective_average_calculator
        else:
            selective_average = SelectiveAverage()(data, n)
        result = 0
        for k, v in data:
            result += ((k - selective_average)**self.__r)*v
        if n <= 30:
            result /= n - 1
        else:
            result /= n
        return result