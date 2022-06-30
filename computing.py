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
# Це Знаходження відносної частоти
class RelativeFrequencies(StatisticalDistribution):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, data: list, n: int) -> list:
        return [(k, v / n) for k, v in data]
    
# Це Знаходження нак. частоти
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
    
# Це Знаходження відносної нак частоти
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

#Вибіркове середнє
class SelectiveAverage:
    def __init__(self, step: int = 1) -> None:
        self.__step = step

    def __call__(self, data: list, n: int) -> float:
        result = 0
        for k, v in data:
            result += (k**self.__step) * v
        return result / n
    
    @property
    def name(self) -> str:
        return "Вибіркове середнє"

#Дисперсія
class Dispersion:
    def __call__(self, data: list, n: int) -> float:
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
    def __call__(self, data: list, n: int) -> float:
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

class TwoDimensionsFashionOfSample:
    def __call__(self, data: list, n: int) -> int:
        result = None
        mx = -1
        for k, v in data:
            for k2, v2 in data:
                if v2 > mx:
                    mx = v2
                    result = (k, k2)
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
        return selective_standard_deviation / selective_average * 100

    @property
    def name(self) -> str:
        return "Коефіцієнт варіації"


# [('a', ('b', 1), ('c', 2))]
class TwoDimensionsComputing:
    def __init__(self, method) -> None:
        self.__method = method

    def __call__(self, data: list):
        data1 = {}
        data2 = {}
        n = 0

        for k1, v1 in data:
            sum1 = 0
            for k2, v in v1:
                if not k2 in data2:
                    data2[k2] = 0
                data2[k2] += v
                sum1 += v
                n += v
            data1[k1] = sum1
        
        result_data_1 = [(k, v) for k, v in data1.items()]
        result_data_2 = [(k, v) for k, v in data2.items()]

        return [self.__method(result_data_2, n), self.__method(result_data_1, n)]

class CorrelationCoefficient:
    def __call__(self, data: list) -> float:
        result = 0

        selective_standard_deviation = TwoDimensionsComputing(SelectiveStandardDeviation())(data)
        selective_average = TwoDimensionsComputing(SelectiveAverage())(data)

        n = 0
        for k, v in data:
            for k2, v2 in v:
                result += k * k2 * v2
                n += v2
        result /= n
        result -= (selective_average[0] * selective_average[1])
        result /= (selective_standard_deviation[0] * selective_standard_deviation[1])
        return result
    
    @property
    def name(self) -> str:
        return "Коефіцієнт кореляції"

class LazyComputation:
    def __init__(self, method):
        self.__method = method
        self.__result = None
    
    def __call__(self, data: list, n: int):
        if self.__result:
            return self.__result
        self.__result = self.__method(data, n)
        return self.__result