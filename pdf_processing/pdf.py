import sys

import PyPDF2

with open('pdf/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilted.pdf', 'wb') as new_file:
        writer.write(new_file)


##############################################
# PDF merger

# retrieves all arguments given in the command line
inputs = sys.argv[1:]


def pdf_merger(pdf_list):
    # creates merger
    merger = PyPDF2.PdfFileMerger()
    # open watermark file
    with open('./pdf/wtr.pdf') as watermark_file:
        for file_name in pdf_list:
            # append each filename
            merger.append(file_name)
        # write the whole file
    merger.write('super.pdf')


pdf_merger(inputs)
