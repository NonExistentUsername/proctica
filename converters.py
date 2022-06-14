from abc import abstractmethod
from collections import Counter

class Converter:
    @abstractmethod
    def __call__(self, data: str) -> dict:
        pass

class SimpleConverter(Converter):
    def __init__(self) -> None:
        super().__init__()
    
    def __call__(self, data: str) -> dict:
        return dict(Counter(data.split(' ')))

class AlphabetConverter(Converter):
    def __init__(self, alphabet: list) -> None:
        super().__init__()
        self.__alphabet = alphabet
    
    def __call__(self, data: str) -> dict:
        ppp = dict(Counter(data.split('')))
        result = {}
        for k in self.__alphabet:
            if k in ppp:
                result[k] = ppp[k]
        return result