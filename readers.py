from abc import abstractmethod

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

import docx2txt

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
 
class PDFReader(Reader):
    def __init__(self, path_to_file) -> None:
        super().__init__()
        self._path_to_file = path_to_file
    
    def __call__(self) -> str:
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, laparams=laparams)
        fp = open(self._path_to_file, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos=set()

        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)

        text = retstr.getvalue()

        fp.close()
        device.close()
        retstr.close()
        return text

class DOCXReader(Reader):
    def __init__(self, path_to_file) -> None:
        super().__init__()
        self._path_to_file = path_to_file

    def __call__(self) -> str:
        return docx2txt.process(self._path_to_file)