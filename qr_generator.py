import qrcode
import os

data = "Start 100 mini Projects Day 1"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

os.makedirs("output", exist_ok=True)
filename = os.path.join("output", "qrcode.png")
img.save(filename)

print(f"✅ QR Code saved to: {filename}")
