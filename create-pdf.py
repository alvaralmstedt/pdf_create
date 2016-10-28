from  reportlab.lib.styles import ParagraphStyle as PS
from  reportlab.platypus import PageBreak
from  reportlab.platypus.paragraph import Paragraph
from  reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from  reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import getSampleStyleSheet
from  reportlab.platypus.frames import Frame
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Image, Frame
import csv
from reportlab.lib.units import cm, inch
from reportlab.lib import utils
from reportlab.lib.colors import pink, black, red, blue, green
import sys

ARGUMENTLIST = sys.argv
DATE = ARGUMENTLIST[1]
DATAFILE = ARGUMENTLIST[2]
INVESTIGATOR = ARGUMENTLIST[3]
INSTRUMENT = ARGUMENTLIST[4]
RUNID = ARGUMENTLIST[5]
#PASSWORD = ARGUMENSTLIST[6]


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
c.drawString(160, 340, PROJECT)


c.showPage()


c.setFillGray(0.25)
c.setFont('Helvetica-Bold', 22, leading=None)
c.drawString(60, 740, 'Sequencing Report')
c.setStrokeColorRGB(0.2,0.1,0.5)
c.line(1.5*cm,720,19.5*cm,720)
c.line(1.5*cm,435,19.5*cm,435)
c.setFont('Helvetica-Bold', 18, leading=None)
c.drawString(60, 690, 'Contents')

ROW1 = 'Contents ................................................................................................................................. 2'
ROW2 = 'Sequencing run information ................................................................................................... 2'
ROW3 = 'General run information ......................................................................................................... 2'
ROW4 = 'QC plot and statistics ............................................................................................................ 3'
ROW5 = 'Sample information ................................................................................................................ 4'
ROW6 = 'Data information ..................................................................................................................... 5'
ROW7 = 'Data delivery ........................................................................................................................ 5'
ROW8 = 'Data structure ....................................................................................................................... 5'
c.setFont('Helvetica', 12, leading=None)
c.drawString(65, 670, ROW1)
c.drawString(65, 650, ROW2)
c.drawString(70, 630, ROW3)
c.drawString(70, 610, ROW4)
c.drawString(65, 590, ROW5)
c.drawString(65, 570, ROW6)
c.drawString(70, 550, ROW7)
c.drawString(70, 530, ROW8)


RUNINFOLISTc = []
RUNINFOLISTc.append(RUNID)
RUNINFOLISTc.append(RUNID.split("_")[0])
RUNINFOLISTc.append(INSTRUMENT)
READLENGTH = '2x' + DATALIST[12][0]
RUNINFOLISTc.append(READLENGTH)
RUNINFOLISTc.append('placeholder1')
RUNINFOLISTc.append('placeholder2')
RUNINFOLISTc.append('placeholder3')
RUNINFOLISTc.append('placeholder4')

RUNINFOYpos = 380
RUNINFOLIST = ['Run ID', 'Date', 'Instrument', 'Read length', 'Reagent kit version', 'Application', 'Library preperation kit', 'Protocol']
c.setFont('Helvetica-Bold', 12, leading=None)
for i in RUNINFOLIST:
	c.drawString(65, RUNINFOYpos, i)
	RUNINFOYpos= RUNINFOYpos - 20
	if i == RUNINFOLIST[4] or i == RUNINFOLIST[6]:
		RUNINFOYpos = RUNINFOYpos - 30

RUNINFOYpos = 380
c.setFont('Helvetica', 12, leading=None)
for i in RUNINFOLISTc:
        c.drawString(330, RUNINFOYpos, i)
        RUNINFOYpos= RUNINFOYpos - 20
        if i == RUNINFOLISTc[4] or i == RUNINFOLISTc[6]:
                RUNINFOYpos = RUNINFOYpos - 30


c.showPage()


c.showPage()


c.showPage()





c.setStrokeColorRGB(0.2,0.1,0.5)
c.line(1*cm,180,20*cm,180)

textobject = c.beginText()
textobject.setTextOrigin(2*cm,160)
textobject.setFont("Helvetica", 10)
textobject.textLines('''Publications are important to us, as are our users. Publications are signs that our work generates interesting
 results. This enables us to apply for more funds to keep the centre running. We would appreciate if our
 facility is mentioned in the Acknowledgements section when data have been obtained in our lab, for example 
by using the sentence: "We would like to thank the Genomics and Bioinformatics Core Facility platforms,
 at the Sahlgrenska Academy, University of Gothenburg".''')
c.drawText(textobject)

c.showPage()


c.save()


