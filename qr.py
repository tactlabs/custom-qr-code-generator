
import qrcode
from PIL import Image, ImageDraw

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size= 9,
    border = 1,
)

# The data that you want to store
print("Give the Data that need to be stored in QR code Image")
data=input()



qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="#996000", back_color="black")


img.save("qr.png")


def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

im = Image.open('qr.png')
im = add_corners(im,100)
im.save('qr.png')


