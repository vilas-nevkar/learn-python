from PyPDF2 import PdfFileWriter, PdfFileReader

import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

font = '/media/capricorn/Home/Master/Code/Python/Core/learn_python/resource/Aparajita.ttf'
pdfmetrics.registerFont(TTFont('Marathi', font))

buffer = io.BytesIO()
# create a new PDF with Reportlab
can = canvas.Canvas(buffer, pagesize=A4)
can.setFont('Marathi', 14)
can.drawString(137, 604, "अनुराग")
can.save()
# move to the beginning of the StringIO buffer
buffer.seek(0)
new_pdf = PdfFileReader(buffer)
# read your existing PDF
existing_pdf = PdfFileReader(open("/media/capricorn/Home/Master/Code/Python/Core/learn_python/resource/tc_format.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open("destination.pdf", "wb")
output.write(outputStream)
outputStream.close()