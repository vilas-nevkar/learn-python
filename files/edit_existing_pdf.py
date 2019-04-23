from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

buffer = io.BytesIO()
# create a new PDF with Reportlab
can = canvas.Canvas(buffer, pagesize=A4)
can.drawString(137, 604, "Anurag")
can.save()
# move to the beginning of the StringIO buffer
buffer.seek(0)
new_pdf = PdfFileReader(buffer)
# read your existing PDF
existing_pdf = PdfFileReader(open("destination.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open("destination.pdf", "wb")
output.write(outputStream)
outputStream.close()