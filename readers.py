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
        return "-3 0 2 3 2 3 4 4 1 1 1 1 7 10 12"