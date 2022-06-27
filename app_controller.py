from converters import *
from readers import *
from computing import *
from alphabets import *
from PyQt5.QtWidgets import QFileDialog
import re

def create_reader(file_path: str):
    if file_path.endswith(".pdf"):
        return PDFReader(file_path)
    elif file_path.endswith(".docx"):
        return DOCXReader(file_path)
    else:
        return TXTReader(file_path)

def create_lazy_reader(file_path: str):
    return LazyReader(create_reader(file_path))

def read_alphabet(parent = None):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(parent ,"QFileDialog.getOpenFileName()", "","All Files (*);;", options=options)
    
    return re.split(",| |\n|\t", create_reader(fileName)())

class ComputingManager:
    def __init__(self) -> None:
        self.__id_to_method = [
            StatisticalFrequencyDistribution(),
            RelativeFrequencies(),
            CumulativeFrequencies(),
            RelativeAccumulatedFrequencies(),
            SelectiveAverage(),
            Dispersion(),
            SelectiveStandardDeviation(),
            FashionOfSample(),
            MedianOfSample(),
            None,
            DimensionOfSample(),
            CovariationCoefficient(),
        ]
    @property
    def methods(self) -> dict:
        return self.__id_to_method

class ConvertersManager:
    def __init__(self, parent = None) -> None:
        self.__parent = parent
        self.__id_to_converter = [
            lambda alphabet: AlphabetConverter(alphabet),
            lambda alphabet: AlphabetConverter(alphabet),
            lambda alphabet: AlphabetConverter(alphabet),
            lambda alphabet: AlphabetConverter(alphabet),
            lambda alphabet: WordslenConverter(alphabet),
            lambda alphabet: LengthOfSentencesConverter(alphabet),
        ]
        self.__id_to_alphabet_type = [
            lambda: ID_TO_ALPHABET,
            lambda: ID_TO_VOWELS_LETTERS,
            lambda: ID_TO_CONSONANT_LETTERS,
            lambda: read_alphabet(self.__parent),
            lambda: ID_TO_ALPHABET,
            lambda: ID_TO_ALPHABET,
            lambda: read_alphabet(self.__parent),
        ]
        self.__id_to_two_dimensin_converter = [
            [
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                None,
                None,
                None,
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
            ],
            [
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                None,
                None,
                None,
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
            ],
            [
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                None,
                None,
                None,
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
            ],
            [
                None,
                None,
                None,
                None,
                None,
                None,
                None,
            ],
            [
                None,
                None,
                None,
                None,
                None,
                None,
                None,
            ],
            [
                None,
                None,
                None,
                None,
                None,
                None,
                None,
            ],
        ]

    @property
    def one_demension_converters(self) -> list:
        return self.__id_to_converter

    @property
    def two_demension_converters(self) -> list:
        return self.__id_to_two_dimensin_converter
    
    @property
    def alphabets(self) -> list:
        return self.__id_to_alphabet_type

class AppController:
    def __init__(self, file_path, parent = None) -> None:
        self.__reader = create_lazy_reader(file_path)
        self.__converters_manager = ConvertersManager(parent)
        self.__computing_manager = ComputingManager()

    def __get_converter(self, alphabet_id, converter_id1, converter_id2):
        if converter_id2 == 0:
            alphabet = self.__converters_manager.alphabets[converter_id1]()[alphabet_id]
            return self.__converters_manager.one_demension_converters[converter_id1](alphabet)
        else:
            converter_id2 -= 1
            alphabet1 = self.__converters_manager.alphabets[converter_id1]()[alphabet_id]
            alphabet2 = self.__converters_manager.alphabets[converter_id2]()[alphabet_id]
            return self.__converters_manager.two_demension_converters[converter_id1][converter_id2](alphabet1, alphabet2)

    def __call__(self, alphabet_id, converter_id1, converter_id2, method_id) -> None:
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
            converter = self.__get_converter(alphabet_id, converter_id1, converter_id2)
            data = converter(self.__reader())
            if method_id == 0:
                return converter.decrypt_default(data)
            result = TwoDimensionsComputing(self.__computing_manager.methods[method_id])(data)
            if isinstance(result[0], tuple) or isinstance(result[0], list):
                return converter.decrypt(result)
            return ((self.__computing_manager.methods[method_id].name + ' (x)', result[0]), (self.__computing_manager.methods[method_id].name + ' (y)', result[1]))