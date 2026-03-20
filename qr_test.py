import qrcode 

url = input("Enter a valid URL: ").strip()

# Enter your own file path
file_path = "C:\\Users\\OCEAN TECH\\OneDrive\\Desktop\\Self Python Projects\\python email\\images py\\qrcode.png"


qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR Code is generated")