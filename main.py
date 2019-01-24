#Author:Selvamanikannan
#Dated:24-01-1999

from PIL import Image, ImageOps, ImageDraw
import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(input("Enter the data\n"))
qr.make(fit=True)
img = qr.make_image(fill_color='#F9B957', back_color='#000000')
img.save('OrginalQR.png') 


im = Image.open('OrginalQR.png')
im = im.convert("RGBA")
logo = Image.open('design.jpg')

width, height = im.size
width-=40
height-=40
print(width,height)
val=width-70

#lt
box = (40,40,110,110)
im.crop(box)
region = logo
region = region.resize((box[2] - box[0], box[3] - box[1]))
im.paste(region,box)
#lb
box = (val,40,width,110)
im.crop(box)
region = logo
region = region.resize((box[2] - box[0], box[3] - box[1]))
im.paste(region,box)
#rt
box = (38,val,110,width)
im.crop(box)
region = logo
region = region.resize((box[2] - box[0], box[3] - box[1]))
im.paste(region,box)
im.save('boxQR.png')

size = (300,300)
mask = Image.new('L', size, 0)
draw = ImageDraw.Draw(mask) 
draw.ellipse((0, 0) + size, fill=255)
output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
output.putalpha(mask)
output.save('circleQR.png')
