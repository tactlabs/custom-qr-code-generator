
import qrcode


qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 15,
    border = 8,
)

# The data that you want to store
print("Give the Data that need to be stored in QR code Image")
data=input()



qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="#996000", back_color="black")


img.save("qrcode.png")



