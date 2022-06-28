from abc import abstractmethod
from collections import Counter
import re

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

class CountConverterWithoutDecrypt(Converter):
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
        return data

class TwoDimensionsConverter(Converter):
    def __init__(self, alphabet1: list[str], alphabet2: list[str]) -> None:
        super().__init__()
        if len(alphabet1) == 0:
            raise ValueError()
        if len(alphabet2) == 0:
            raise ValueError()
        
        self.__alphabet1 = []
        self.__alphabet_to_id1 = {}
        self.__id_to_alphabet1 = {}
        curid = 1
        tmp = set()
        for key in alphabet1:
            if not key in tmp:
                self.__alphabet1.append(key)
                self.__alphabet_to_id1[key] = curid
                self.__id_to_alphabet1[curid] = key
                curid += 1
                tmp.add(key)

        self.__alphabet2 = []
        self.__alphabet_to_id2 = {}
        self.__id_to_alphabet2 = {}
        curid = 1
        tmp = set()
        for key in alphabet2:
            if not key in tmp:
                self.__alphabet2.append(key)
                self.__alphabet_to_id2[key] = curid
                self.__id_to_alphabet2[curid] = key
                curid += 1
                tmp.add(key)
    
    def __call__(self, data: str) -> list:
        data = data.lower()
        result = []
        for i in range(len(self.__alphabet1)):
            temp = []
            for j in range(len(self.__alphabet2)):
                temp.append((self.__alphabet_to_id2[self.__alphabet2[j]], data.count(self.__alphabet1[i] + self.__alphabet2[j])))
            result.append((self.__alphabet_to_id1[self.__alphabet1[i]], temp))
        return result
    
    @property
    def id_to_alphabet1(self) -> dict:
        return self.__id_to_alphabet1
    
    @property
    def id_to_alphabet2(self) -> dict:
        return self.__id_to_alphabet2

    def decrypt_default(self, data: list) -> list:
        result = []
        for k, v in data:
            tmp = []
            for k2, v2 in v:
                tmp.append((self.__id_to_alphabet2[k2], v2))
            result.append((self.__id_to_alphabet1[k], tmp))
        return result

    def decrypt(self, data: list) -> list:
        data1, data2 = data
        new_data1 = []
        new_data2 = []
        for k, v in data1:
            new_data1.append((self.__id_to_alphabet1[k], v))
        for k, v in data2:
            new_data2.append((self.__id_to_alphabet2[k], v))
        return [new_data1, new_data2]

class WordslenConverter(Converter):
    def __init__(self, alphabet) -> None:
        super().__init__()
        self.__alphabet = alphabet
    
    def __call__(self, data: str) -> list:
        w = dict(Counter(map(lambda x: len(x), re.split(" |\,|\!|\?|\.|\...|\n|\t|:", data))))
        result = []
        for k, v in w.items():
            result.append((k, v))
        result.sort(key = lambda x: x[0])
        return result
    
    def decrypt(self, data: list) -> list:
        return data

class LengthOfSentencesConverter(Converter):
    def __init__(self, alphabet) -> None:
        super().__init__()
        self.__alphabet = alphabet
    
    def __call__(self, data: str) -> list:
        w = dict(Counter(map(lambda x: len(x), re.split("\! |\? |\. |\... ", data))))
        result = []
        for k, v in w.items():
            result.append((k, v))
        result.sort(key = lambda x: x[0])
        return result
    
    def decrypt(self, data: list) -> list:
        return data
class LazyConverter(Converter):
    def __init__(self, converter) -> None:
        super().__init__()
        self.__converter = converter
        self.__result = None
    
    def __call__(self, data: str) -> list:
        if self.__result:
            return self.__result
        self.__result = self.__converter(data)
        return self.__result
