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
    def __init__(self, alphabet: list[str]) -> None:
        super().__init__()
        if len(alphabet) == 0:
            raise ValueError()
        
        self.__alphabet = []
        self.__alphabet_to_id = {}
        self.__id_to_alphabet = {}
        curid = 1
        tmp = set()
        for key in alphabet:
            if not key in tmp:
                self.__alphabet.append(key)
                self.__alphabet_to_id[key] = curid
                self.__id_to_alphabet[curid] = key
                curid += 1
                tmp.add(key)

    def __call__(self, data: str) -> list:
        data = data.lower()
        result_dict = {}
        for key in self.__alphabet:
            result_dict[self.__alphabet_to_id[key]] = data.count(key)

        self.__copy_alphabet = self.__alphabet.copy()
        self.__copy_alphabet.sort(key = lambda x: len(x), reverse = True)

        for i in range(len(self.__copy_alphabet) - 1):
            for j in range(i + 1, len(self.__copy_alphabet)):
                cnt = self.__copy_alphabet[i].count(self.__copy_alphabet[j])
                result_dict[self.__alphabet_to_id[self.__copy_alphabet[j]]] -= cnt * result_dict[self.__alphabet_to_id[self.__copy_alphabet[i]]]

        result = []
        for key in self.__alphabet:
            result.append((self.__alphabet_to_id[key], result_dict[self.__alphabet_to_id[key]]))
        return result

    def decrypt(self, data: list) -> list:
        result = []
        for k, v in data:
            result.append((self.__id_to_alphabet[k], v))
        return result

class CountConverter(Converter):
    def __init__(self, alphabet: list[str]) -> None:
        super().__init__()
        if len(alphabet) == 0:
            raise ValueError()
        
        self.__alphabet = []
        self.__alphabet_to_id = {}
        self.__id_to_alphabet = {}
        curid = 1
        tmp = set()
        for key in alphabet:
            if not key in tmp:
                self.__alphabet.append(key)
                self.__alphabet_to_id[key] = curid
                self.__id_to_alphabet[curid] = key
                curid += 1
                tmp.add(key)

    def __call__(self, data: str) -> list:
        data = data.lower()
        result = []
        for key in self.__alphabet:
            result.append((self.__alphabet_to_id[key], data.count(key)))
        return result

    def decrypt(self, data: list) -> list:
        result = []
        for k, v in data:
            result.append((self.__id_to_alphabet[k], v))
        return result

class WordslenConverter(Converter):
    def __init__(self) -> None:
        super().__init__()
    
    def __call__(self, data: str) -> list:
        pass
    