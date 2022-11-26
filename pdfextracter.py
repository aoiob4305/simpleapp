from PyPDF2 import PdfMerger
import sys

if len(sys.argv) < 2:
    print("usage: {} filename".format(sys.argv[0]))
else:
    print("filename is {}".format(sys.argv[1]))
    filename = sys.argv[1]

    try:
        pagenum_start = int(input("start page num: "))
        pagenum_end = int(input("end page num: "))

        if pagenum_start > pagenum_end:
            print("page number is wrong")
        else:
            print("extract page from {} to {}".format(pagenum_start, pagenum_end))    

    except ValueError as e:
        print(e)
        exit()

    try:
        merger = PdfMerger()
        with open(filename, "rb") as ifp:
            merger.append(fileobj=ifp, pages=(pagenum_start-1, pagenum_end))


        with open("{}_{}-{}.pdf".format(filename, pagenum_start, pagenum_end), "wb") as ofp:
            merger.write(ofp)
    
    except Exception as e:
        print(e)
        exit()