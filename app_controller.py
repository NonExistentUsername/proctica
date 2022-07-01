from multiprocessing.sharedctypes import Value
from converters import *
from readers import *
from computing import *
from alphabets import *
from PyQt5.QtWidgets import QFileDialog, QInputDialog
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

def read_alphabet(parent, msg):
    text, ok = QInputDialog.getText(parent, 'Ввід даних', msg)

    if ok:
        alphabet = re.split(",| |\n|\t", text)
    else:
        raise ValueError()
    return alphabet

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
            SelectiveAverage(step = 2),
        ]
        self.__id_to_two_dimension_method = [
            lambda data: StatisticalFrequencyDistribution()(data, 0),
            TwoDimensionsComputing(RelativeFrequencies()),
            TwoDimensionsComputing(CumulativeFrequencies()),
            TwoDimensionsComputing(RelativeAccumulatedFrequencies()),
            TwoDimensionsComputing(SelectiveAverage()),
            TwoDimensionsComputing(Dispersion()),
            TwoDimensionsComputing(SelectiveStandardDeviation()),
            TwoDimensionsComputing(FashionOfSample()),
            TwoDimensionsComputing(MedianOfSample()),
            CorrelationCoefficient(),
            TwoDimensionsComputing(DimensionOfSample()),
            TwoDimensionsComputing(CovariationCoefficient()),
            TwoDimensionsComputing(SelectiveAverage(step = 2)),
        ]
    @property
    def methods(self) -> list:
        return self.__id_to_method
    
    @property
    def two_dimension_methods(self) -> list:
        return self.__id_to_two_dimension_method

class ConvertersManager:
    def __init__(self, parent = None) -> None:
        self.__parent = parent
        self.__id_to_converter = [
            lambda alphabet: AlphabetConverter(alphabet),
            lambda alphabet: AlphabetConverter(alphabet),
            lambda alphabet: AlphabetConverter(alphabet),
            lambda alphabet: CountConverter(alphabet),
            lambda alphabet: WordslenConverter(alphabet),
            lambda alphabet: LengthOfSentencesConverter(alphabet),
            lambda alphabet: CountConverter(alphabet),
        ]
        self.__id_to_alphabet_type = [
            lambda id: ID_TO_ALPHABET[id],
            lambda id: ID_TO_VOWELS_LETTERS[id],
            lambda id: ID_TO_CONSONANT_LETTERS[id],
            lambda id: read_alphabet(self.__parent, 'Введіть літери через пробіл або кому:'),
            lambda id: ID_TO_ALPHABET[id],
            lambda id: ID_TO_ALPHABET[id],
            lambda id: read_alphabet(self.__parent, 'Введіть буквосполучення через пробіл або кому:'),
        ]
        self.__id_to_two_dimensin_converter = [
            [
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                None,
                None,
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
            ],
            [
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                None,
                None,
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
            ],
            [
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                None,
                None,
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
            ],
            [
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
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
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
                None,
                None,
                lambda alphabet1, alphabet2: TwoDimensionsConverter(alphabet1, alphabet2),
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
            alphabet = self.__converters_manager.alphabets[converter_id1](alphabet_id)
            return self.__converters_manager.one_demension_converters[converter_id1](alphabet)
        else:
            converter_id2 -= 1
            alphabet1 = self.__converters_manager.alphabets[converter_id1](alphabet_id)
            alphabet2 = self.__converters_manager.alphabets[converter_id2](alphabet_id)
            return self.__converters_manager.two_demension_converters[converter_id1][converter_id2](alphabet1, alphabet2)

    def read_data(self, alphabet_id, converter_id1, converter_id2):
        converter = self.__get_converter(alphabet_id, converter_id1, converter_id2)
        data = converter(self.__reader())
        return [converter, data]

    def calc(self, alphabet_id, converter_id1, converter_id2, method_id, converter, data):
        if converter_id2 == 0:
            n = 0
            for k, v in data:
                n += v
            result = self.__computing_manager.methods[method_id](data, n)
            if isinstance(result, list):
                return converter.decrypt(result)
            return (self.__computing_manager.methods[method_id].name, result)
        else:
            result = self.__computing_manager.two_dimension_methods[method_id](data)
            if method_id == 0:
                return converter.decrypt_default(result)
            if method_id == 9:
                return (self.__computing_manager.two_dimension_methods[method_id].name, result)
            if isinstance(result[0], tuple) or isinstance(result[0], list):
                return converter.decrypt(result)
            return ((self.__computing_manager.methods[method_id].name + ' (x)', result[0]), 
                    (self.__computing_manager.methods[method_id].name + ' (y)', result[1]))

    def __call__(self, alphabet_id, converter_id1, converter_id2, method_id):
        converter, data = self.read_data(alphabet_id, converter_id1, converter_id2)
        result = self.calc(alphabet_id, converter_id1, converter_id2, method_id, converter, data)
        return result

    @property
    def methods_for_calc_all(self) -> list:
        return [4, 5, 6, 7, 8, 10, 11, 12]

    @property
    def methods_for_calc_all_2d(self) -> list:
        return [4, 5, 6, 7, 8, 9, 10, 11, 12]

    def calc_all(self, alphabet_id, converter_id1, converter_id2):
        converter, data = self.read_data(alphabet_id, converter_id1, converter_id2)
        if converter_id2 == 0:
            methods = self.methods_for_calc_all
        else:
            methods = self.methods_for_calc_all_2d
        results = []
        for method_id in methods:
            results.append(self.calc(alphabet_id, converter_id1, converter_id2, method_id, converter, data))
        return results

