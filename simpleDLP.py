import re
import ctypes
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

def messageBox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(None,title,text,style)

def read_pdf_PDFMINER(pdf_file_path):
    output_string = StringIO()
    with open(pdf_file_path, 'rb') as f:
        parser = PDFParser(f)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    return str(output_string.getvalue())

print("================ PDF 문서내 주민번호 검출기 프로그램 ================")
print("Sample >>> C:\실습\homework\dlp_test.pdf")
path = input("파일경로 >>> ")
print("\n================ 원본 PDF 데이터 ================")
text = read_pdf_PDFMINER(path)
print(text)

humannum = re.compile(r'\b(?:[0-9]{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[1,2][0-9]|3[0,1]))-[1-4][0-9]{6}\b')
result = humannum.search(text)
print(result)

if result != None:
    messageBox("PDF 문서에서 개인정보가 탐지됨", "경고", 0)


