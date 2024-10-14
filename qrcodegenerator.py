import qrcode  # Ensure this is correct
from PIL import Image  # Make sure Pillow is installed

# Configure the QR code
qr = qrcode.QRCode(
    version=15,      # Version of the QR code, increases data capacity
    box_size=10,     # Size of each box in the QR code grid
    border=5         # Size of the white border around the QR code
)

# Set the data you want to encode
data = "https://www.youtube.com/"
qr.add_data(data)
qr.make(fit=True)

# Create and save the QR code image
img = qr.make_image(fill="black", back_color="white")
img.save("test.png")
