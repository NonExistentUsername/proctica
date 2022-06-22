from abc import abstractmethod
from collections import Counter

def split(word):
    return [char for char in word]

class Converter:
    @abstractmethod
    def __call__(self, data: str) -> list:
        pass

class SimpleConverter(Converter):
    def __init__(self) -> None:
        super().__init__()
    
    def __call__(self, data: str) -> list:
        return list(dict(Counter(data.split(' '))).items())

class CharactersConverter(Converter):
    def __init__(self) -> None:
        super().__init__()
    
    def __call__(self, data: str) -> list:
        return list(dict(Counter(split(data))).items())

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

class BoostedConverter(Converter):
    DELETED_SYMBOL = '~'

    def __init__(self, alphabet: list[str]) -> None:
        super().__init__()
        if len(alphabet) == 0:
            raise ValueError()
        
        self.__alphabet = []
        tmp = set()
        for key in alphabet:
            if not key in tmp:
                self.__alphabet.append(key)
                tmp.add(key)

    def __z_func(self, substr: list) -> int:
        n = len(self.__data)
        m = len(substr)
        z = [0] * n
        for i in range(m):
            self.__data[i] = substr[i]

        l = 0
        r = 0
        cnt = 0
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and self.__data[z[i]] == self.__data[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1

        stop_clear_pos = 0
        for i in range(m + 1, n):
            if stop_clear_pos > i:
                self.__data[i] = BoostedConverter.DELETED_SYMBOL
            elif z[i] >= m:
                self.__data[i] = BoostedConverter.DELETED_SYMBOL
                stop_clear_pos = i + m
                cnt += 1

        return cnt

    def __call__(self, data: str) -> list:
        self.__data = split(BoostedConverter.DELETED_SYMBOL * (len(self.__alphabet[0]) + 1) + data)
        tmp_result = {}
        sorted_alphabet = self.__alphabet.copy()
        sorted_alphabet.sort(key=lambda x: len(x), reverse=True)
        for substr in sorted_alphabet:
            tmp_result[substr] = self.__z_func(split(substr))
        result = []
        for key in self.__alphabet:
            result.append((key, tmp_result[key]))
        return result

class BoostedConverter2(Converter):
    DELETED_SYMBOL = '~'

    def __init__(self, alphabet: list[str]) -> None:
        super().__init__()
        if len(alphabet) == 0:
            raise ValueError()
        
        self.__alphabet = []
        tmp = set()
        for key in alphabet:
            if not key in tmp:
                self.__alphabet.append(key)
                tmp.add(key)

    def __call__(self, data: str) -> list:
        result = []
        for key in self.__alphabet:
            result.append((key, data.count(key)))
        return result
