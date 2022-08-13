import qrcode
data_qr = input("write your text here")
img = qrcode.make(data_qr)
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")