from email.mime import image
import qrcode
import image
qr = qrcode.QRCode(
    version=8,
    box_size=10,
)
data = '''https://techstorm-23.vercel.app/rules_codebee.html'''
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_colour="white")
img.save("test.png")
