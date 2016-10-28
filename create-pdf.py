from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Image, Frame
import csv
from reportlab.lib.units import cm
from reportlab.lib import utils
from reportlab.lib.colors import pink, black, red, blue, green
import sys

ARGUMENTLIST = sys.argv
DATE = ARGUMENTLIST[1]
DATAFILE = ARGUMENTLIST[2]
INVESTIGATOR = ARGUMENTLIST[3]

data = csv.reader(open(DATAFILE,"rb"))
DATALIST = list(data)
mypdf = 'mypdffile.pdf'
c = canvas.Canvas(mypdf, pagesize=A4)
frontimage = 'SAsidelog.png'
genomics = 'genomics_core.png'

def get_image(path, width):
	img = utils.ImageReader(path)
	iw, ih = img.getSize()
	aspect = ih / float(iw)
	height = width * aspect
	return height
newheight_fac = get_image(frontimage, 20)
newheight_gen = get_image(genomics, 8)

# LOGOS 
c.drawImage(frontimage, 8, 7, width=20*cm, height=newheight_fac*cm, mask='auto')
c.drawImage(genomics, 150, 640, width=8*cm, height=newheight_gen*cm, mask='auto')
c.setFont('Helvetica', 18, leading=None)
c.drawString(160, 600, 'Bioinformatics')
c.setFont('Helvetica', 15, leading=None)
c.drawString(160, 580, 'Core Facility')
c.setFont('Helvetica-Bold', 28, leading=None)

# HEADER
c.setFillGray(0.25)
c.drawString(160, 480, 'Sequencing Report')
c.setFillColorRGB(0.2,0.1,0.5)
c.setFont('Helvetica-Bold', 22, leading=None)
c.drawString(160, 455, 'Raw data delivery and Bioinformatics')

# DATE, INVESTIGATOR AND PROJECT NAME
c.setFillColorRGB(0,0,0)
c.setFont('Helvetica', 15, leading=None)
ANALYSISDATE = 'Analysis date:  ' + DATE
c.drawString(160, 380, ANALYSISDATE)
INVEST = 'Investigator:     ' + INVESTIGATOR
c.setFont('Helvetica', 15, leading=None)
c.drawString(160, 360, INVEST)
c.setFont('Helvetica', 15, leading=None)
PROJ = DATALIST[3][1]
PROJECT = 'Project:            ' + PROJ
c.drawString(160, 340, 'Project:            G16-032')


c.showPage()

#for row in data:
#	print row
#        c.setFont('Helvetica', 8, leading=None)
#        ypos=ypos+10
#        c.drawCentredString(215, ypos, row)
#

c.save()


