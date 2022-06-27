from abc import abstractclassmethod
import math

class StatisticalDistribution:
    @abstractclassmethod
    def __call__(self, data: list, n: int) -> list:
        pass

class StatisticalFrequencyDistribution(StatisticalDistribution):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, data: list, n: int) -> list:
        return data

class RelativeFrequencies(StatisticalDistribution):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, data: list, n: int) -> list:
        return [(k, v / n) for k, v in data]

class CumulativeFrequencies(StatisticalDistribution):
    def __init__(self) -> None:
        super().__init__()
    
    def __call__(self, data: list, n: int) -> list:
        result = []
        i = 0
        for k, v in data:
            result.append((k, i))
            i += v
        return result

class RelativeAccumulatedFrequencies(StatisticalDistribution):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, data: list, n: int) -> list:
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
    
    @property
    def name(self) -> str:
        return "Вибіркове середнє"

class Dispersion:
    def __init__(self, selective_average_calculator = None) -> None:
        self.__selective_average_calculator = selective_average_calculator

    def __call__(self, data: list, n: int) -> float:
        if self.__selective_average_calculator:
            selective_average = self.__selective_average_calculator(data, n)
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

    @property
    def name(self) -> str:
        return "Дисперсія"

class SelectiveStandardDeviation:
    def __init__(self, dispersion_calculator = None) -> None:
        self.__dispersion_calculator = dispersion_calculator
    
    def __call__(self, data: list, n: int) -> float:
        if self.__dispersion_calculator:
            dispersion = self.__dispersion_calculator(data, n)
        else:
            dispersion = Dispersion()(data, n)
        return math.sqrt(dispersion)

    @property
    def name(self) -> str:
        return "Вибіркове стандартне відхилення"

class FashionOfSample:
    def __call__(self, data: list, n: int) -> int:
        result = None
        mx = -1
        for k, v in data:
            if v > mx:
                mx = v
                result = k
        return [(result, mx)]

    @property
    def name(self) -> str:
        return "Мода"
class MedianOfSample:
    def __call__(self, data: list, n: int) -> float:
        l = n // 2
        sum = 0
        pos = None
        for i in range(len(data)):
            k, v = data[i]

            sum += v
            if sum >= l:
                pos = i
                break
        
        if n > 0 and n % 2 == 1:
            return data[pos][0]
        else:
            if sum > l:
                return data[pos][0]
            else:
                return (data[pos][0] + data[pos + 1][0]) / 2

    @property
    def name(self) -> str:
        return "Медіана"

class DimensionOfSample:
    def __call__(self, data: list, n: int) -> int:
        xmax = data[0][0]
        xmin = data[0][0]
        for k, v in data:
            xmax = max(xmax, k)
            xmin = min(xmin, k)
        return xmax - xmin

    @property
    def name(self) -> str:
        return "Розмах"

class CovariationCoefficient:
    def __call__(self, data: list, n: int) -> float:
        selective_average = SelectiveAverage()(data, n)
        selective_standard_deviation = SelectiveStandardDeviation()(data, n)
        return selective_standard_deviation / selective_average

    @property
    def name(self) -> str:
        return "Коефіцієнт варіації"

class LazyComputation:
    def __init__(self, method):
        self.__method = method
        self.__result = None
    
    def __call__(self, data: list, n: int):
        if self.__result:
            return self.__result
        self.__result = self.__method(data, n)
        return self.__result