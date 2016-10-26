from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Image, Frame
import csv
from reportlab.lib.units import cm
from reportlab.lib import utils

data_file = 'csv.csv'
mypdf = 'mypdffile.pdf'
c = canvas.Canvas(mypdf, pagesize=A4)
frontimage = 'SAsidelog.png'
genomics = 'genomics_core.png'
bioinf = 'bioinformatics_core.png'

def get_image(path, width):
	img = utils.ImageReader(path)
	iw, ih = img.getSize()
	aspect = ih / float(iw)
	height = width * aspect
	return height
newheight_fac = get_image(frontimage, 20)
newheight_gen = get_image(genomics, 8)
#newheight_bio = get_image(bioinf, 6)

#ypos=400
#attendee_data = csv.reader(open(data_file,"rb"))
#for row in attendee_data:
#	datastring = row[5]
#	c.setFont('Helvetica', 8, leading=None)
#	ypos=ypos+40
#	c.drawCentredString(215, ypos, datastring)

c.drawImage(frontimage, 8, 7, width=20*cm, height=newheight_fac*cm)
c.drawImage(genomics, 150, 640, width=8*cm, height=newheight_gen*cm)
#c.drawImage(bioinf, 70, 120, width=6*cm, height=newheight_bio*cm)

#story = []
#story.append(get_image(frontimage, width=21*cm))
#frame.addFromList(story, c)

c.showPage()

c.save()


