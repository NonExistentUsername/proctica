from itertools import accumulate
from converters import *
from readers import *
from computing import *
from alphabets import *

def create_reader(file_path: str):
    if file_path.endswith(".pdf"):
        return PDFReader(file_path)
    elif file_path.endswith(".docx"):
        return DOCXReader(file_path)
    else:
        return TXTReader(file_path)

def create_lazy_reader(file_path: str):
    return LazyReader(create_reader(file_path))

class ComputingManager:
    def __init__(self) -> None:
        self.__id_to_method = {
            0: StatisticalFrequencyDistribution(),
            1: RelativeFrequencies(),
            2: CumulativeFrequencies(),
            3: RelativeAccumulatedFrequencies(),
            4: SelectiveAverage(),
            5: Dispersion(),
            6: SelectiveStandardDeviation(),
            7: FashionOfSample(),
            8: MedianOfSample(),
            9: None,
            10: DimensionOfSample(),
            11: CovariationCoefficient(),
        }
    @property
    def methods(self) -> dict:
        return self.__id_to_method

class ConvertersManager:
    def __init__(self) -> None:
        self.__id_to_converter = [
            lambda alphabet: AlphabetConverter(alphabet),
            lambda alphabet: AlphabetConverter(alphabet),
            lambda alphabet: AlphabetConverter(alphabet),
            lambda alphabet: AlphabetConverter(alphabet),
            lambda alphabet: WordslenConverter(alphabet),
            lambda alphabet: LengthOfSentencesConverter(alphabet),
        ]
        self.__id_to_alphabet_type = {
            0: lambda: ID_TO_ALPHABET,
            1: lambda: ID_TO_VOWELS_LETTERS,
            2: lambda: ID_TO_CONSONANT_LETTERS,
            3: lambda: ID_TO_ALPHABET,
            4: lambda: ID_TO_ALPHABET,
            5: lambda: ID_TO_ALPHABET,
        }

    @property
    def one_demension_converters(self) -> dict:
        return self.__id_to_converter
    
    @property
    def alphabets(self) -> dict:
        return self.__id_to_alphabet_type

class AppController:
    def __init__(self, file_path) -> None:
        self.__reader = create_lazy_reader(file_path)
        self.__converters_manager = ConvertersManager()
        self.__computing_manager = ComputingManager()

    def __get_converter(self, alphabet_id, converter_id1, converter_id2):
        alphabet = self.__converters_manager.alphabets[converter_id1]()[alphabet_id]
        return self.__converters_manager.one_demension_converters[converter_id1](alphabet)

    def __call__(self, alphabet_id, converter_id1, converter_id2, method_id) -> None:
        print(alphabet_id, converter_id1, converter_id2, method_id)
        if converter_id2 == 0:
            converter = self.__get_converter(alphabet_id, converter_id1, converter_id2)
            data = converter(self.__reader())
            n = 0
            for k, v in data:
                n += v
            result = self.__computing_manager.methods[method_id](data, n)
            if isinstance(result, list):
                return converter.decrypt(result)
            return (self.__computing_manager.methods[method_id].name, result)
        else:
            pass
