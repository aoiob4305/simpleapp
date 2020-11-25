#-*- coding: utf-8 -*-

from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
    try:
        input = PdfFileReader(open(filename, "rb"))
        pageNum = input.getNumPages()

    except:
        print("file read error")

    try:
        for num in range(0, pageNum): 
            output = PdfFileWriter()

            page = input.getPage(num)
            output.addPage(page)

            outputStream = open(filename + "_" + str(num + 1) + ".pdf", "wb")
            output.write(outputStream)
    except:
        print("file write error")
else:
    print("split pdf file in each page")
    print("usage: "+sys.argv[0]+" filename")