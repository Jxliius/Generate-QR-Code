import qrcode

data = 'https://open.kattis.com/'

img = qrcode.make(data)

img.save('kattis.png')