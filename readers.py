from abc import abstractmethod


class Reader:
    @abstractmethod
    def __call__(self) -> str:
        pass

class PDFReader(Reader):
    def __call__(self) -> str:
        return "huy"

class SimpleReader(Reader):
    def __init__(self) -> None:
        super().__init__()
    
    def __call__(self) -> str:
        return "abababbchskjsqqlkqkqkqszzz"

class TXTReader(Reader):
    def __init__(self, path_to_file) -> None:
        super().__init__()
        self._path_to_file = path_to_file
    
    def __call__(self) -> str:
        with open(self._path_to_file, "r") as f:
            return f.read()
 