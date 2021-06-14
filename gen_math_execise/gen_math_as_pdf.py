import random
import PyPDF2
import os
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, mm
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import blue

CP  = os.path.dirname(os.path.abspath(__file__))

'''
"Courier"
"Courier-Bold
"Courier-BoldOblique"
"Courier-Oblique"
"Helvetica"
"Helvetica-Bold"
"Helvetica-BoldOblique"
"Helvetica-Oblique"
"Times-Bold"
"Times-BoldItalic
"Times-Italic"
"Times-Roman"
'''
def to_pdf(filename):
    target_file = filename.split('.')[0] + '.pdf'
    target = os.path.join(CP, target_file)
    source_file = os.path.join(CP, filename)
    canvas = Canvas(target, pagesize=A4)
    canvas.translate(0, 0)
    canvas.setFillColor(blue)
    font_size = 16
    canvas.setFont("Courier", font_size)
    
    with open(source_file, 'r') as rh:
        n = 1
        for r in rh:
            r = r.replace('\t', ' '*3)
            if r == '\n':
                canvas.drawString(5, A4[1]-n*20, '')
            else:
                canvas.drawString(5, A4[1]-n*20, r)
            if n % 60 == 0:
                canvas.showPage()
                canvas.setFillColor(blue)
                canvas.setFont("Courier", font_size)
                n =  1 
            n += 1
    canvas.save()
target_file = os.path.join(CP, "ti.txt")
with open(target_file, 'w') as wh:
    n = 600
    hang = 8
    column = 2
    ti = []
    number = 1
    h = 0
    start = 0
    end = 9
    while n:
        a = random.randint(start, end)
        b = random.randint(start, end)
        if a <= b:
            ti.append("{:<28}".format("{:<4} + {:<4} =    ".format(a, b)))
        else:
            ti.append("{:<28}".format("{:<4} - {:<4} =    ".format(a, b)))
        if len(ti) == column:
            wh.write("{:<3}. {}\n".format(number, "    ".join(ti)))
            h += 1
            if h == hang:
                wh.write("\n")
                h = 0
            number += 1
            ti = []
        n -= 1
to_pdf(target_file)