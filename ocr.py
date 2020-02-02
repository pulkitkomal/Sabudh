from PIL import Image as image
import os
import tesserocr
from tesserocr import PyTessBaseAPI

with PyTessBaseAPI(lang='gur+eng') as api:
    ent = os.listdir(r'D:/sabudh')
    Textdata = []
    for i in ent:
        img = image.open(r'D:/sabudh' + '/' + 'i.jpg')
        gray = img.convert('L')
        blackwhite = gray.point(lambda x: 0 if x < 200 else 255, '1')
        blackwhite.save(r"outputS.jpg")
        api.SetImageFile(r"outputS.jpg")
        Text = api.GetUTF8Text()
        Textdata.append(Text)

print(Textdata[0])
