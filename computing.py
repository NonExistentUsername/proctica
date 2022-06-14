from abc import abstractclassmethod

class StatisticalDistribution:
    @abstractclassmethod
    def __call__(self, data: dict) -> dict:
        pass

class RelativeFrequencies(StatisticalDistribution):
    def __init__(self) -> None:
        super().__init__()
    
    def __call__(self, data: dict) -> dict:
        n = sum(data.values())
        result = {}
        for k, v in data.items():
            result[k] = v / n
        return result
