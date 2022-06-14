from abc import abstractmethod
from collections import Counter

class Converter:
    @abstractmethod
    def __call__(self, data: str) -> list:
        pass

class SimpleConverter(Converter):
    def __init__(self) -> None:
        super().__init__()
    
    def __call__(self, data: str) -> list:
        return list(dict(Counter(data.split(' '))).items())
class AlphabetConverter(Converter):
    def __init__(self, alphabet: list) -> None:
        super().__init__()
        self.__alphabet = alphabet
    
    def __call__(self, data: str) -> list:
        ppp = dict(Counter(data.split('')))
        result = {}
        for k in self.__alphabet:
            if k in ppp:
                result[k] = ppp[k]
        return result