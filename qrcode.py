import qrcode

img = qrcode.make("https://github.com/AnikGLA/Python-Notes")
img.save("github.png", "PNG")
