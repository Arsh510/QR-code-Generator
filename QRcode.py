import qrcode  # pip install qrcode  #pip install pillow
#img = qrcode.make("https://www.youtube.com/")
img = qrcode.make("I AM ARSH PATEL. I LEARN PYTHON AND THIS PROJECT TO GENRATE A QRCODE")
img.save("TEXT.png")
