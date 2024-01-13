import qrcode
import image
qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)

data = "https://nextjobfinder.com/subscribemsa.php?msclkid=442760eb804413c4e2260549faf37c5b"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fit = "black",back_color = "white")
img.save("test.png")