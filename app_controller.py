from readers import *
from converters import *
from computing import *
from alphabets import *

class AppController:
    def __init__(self):
        pass

    def create_reader(self, file: str):
        if file.endswith("pdf"):
            return PDFReader(file)
        elif file.endswith(".docx"):
            return DOCXReader(file)
        return TXTReader(file)

    def calculate(self, file: str, selected_method_id: int):
        reader = self.create_reader(file)
        converter = BoostedConverter2(ENGLISH_ALPHABET)
        method = CumulativeFrequencies()
        print(method(converter(reader())))