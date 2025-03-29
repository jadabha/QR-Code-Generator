import qrcode

data = "https://youtu.be/dQw4w9WgXcQ?si=WZK2KydNhkKSmV5n"

img = qrcode.make(data)

img.save('MyQRCode1.png')