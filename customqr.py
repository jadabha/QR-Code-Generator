import qrcode

data = input("Please enter the link that you want to create a QR code for: \n")

while True:
    if "https" in data or "www." in data or ".com" in data:
        img = qrcode.make(data)
        img.save('MyQRCode1.png')
        print("QR Code saved as MyQRCode1.png")
        break
    else:
        data = input("Please enter a valid link. ('Q' or 'q' to quit.): \n")
        if data.lower() == 'q':
            print("Goodbye!")
            break