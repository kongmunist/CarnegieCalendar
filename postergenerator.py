import qrcode
from PIL import Image, ImageDraw



def getQR(link):
    qr = qrcode.QRCode(
        box_size=16,
        border=1,
    )
    qr.add_data(link)
    qr.make(fit=True)
    return qr.make_image()

def makePoster(pathToBG, link):
    img = getQR(link)
    w, h = img.size

    bg = Image.open(pathToBG, 'r')
    bgw, bgh = bg.size

    bg.paste(img, ((bgw-w)//2, (bgh-h)//2-10))
    return bg

link = "https://www.carnegiecalendar.com/"
path = "CCTemplate2.png"
color = (240,)*3

imageList = []

for i in range(1,64):
    yea = link + str(i)
    img = makePoster(path, yea)
    ImageDraw.Draw(img).text((163,273), str(i), color)
    imageList.append(img)

orig = imageList.pop(0)
orig.save('posterList2.pdf','PDF', quality=95, save_all=True, append_images=imageList)
# resolution=1200.0,


