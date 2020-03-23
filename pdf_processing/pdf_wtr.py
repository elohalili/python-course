import PyPDF2

source = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('pdf/wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for page in source.pages:
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

with open('super_wtr.pdf', 'wb') as super_wtr:
    output.write(super_wtr)
