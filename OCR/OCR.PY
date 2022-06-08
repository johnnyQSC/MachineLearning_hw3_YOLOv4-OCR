from time import sleep
from types import DynamicClassAttribute
from typing import Counter, Text
import numpy as np
import PIL 
from PIL import Image
import glob
from pyocr.pyocr import TOOLS
from PIL import Image
import pytesseract

#圖片轉換resize與灰階
myfiles=glob.glob('D:/dartnetYolo/darknet/build/darknet/x64/Cut/*.JPG')  #抓取檔案
print(myfiles)
empty_dir=('D:/dartnetYolo/darknet/build/darknet/x64/Cut2/')   #存放位置
print('開始轉換圖片到灰階')
for i,f in enumerate(myfiles):
  img=Image.open(f)
  img_new=img.resize((100,50),PIL.Image.ANTIALIAS)   #更改影像尺寸
  img_new=img_new.convert('L')  #轉換為黑白
  outname=str('newGray')+str('{:0>3d}').format(i+1)+'.jpg'  #改檔名及副檔名
  img_new.save(empty_dir+outname)  #存放位置+檔名
print('完成')

#OCR辨識
out = ''

for i in range(1,21):
    #print(i)
    result=Image.open('D:/dartnetYolo/darknet/build/darknet/x64/cut2/'+str(i)+'.jpg')
    #result.show()
    x = pytesseract.image_to_string(result)
    print(str(i)+"貨櫃號辨識是結果:",pytesseract.image_to_string(result))
    f = open('D:/dartnetYolo/darknet/build/darknet/x64/cut2/OCR.txt','w')
    out += str(i) + "貨櫃號辨識是結果:" + x +'\n'
    f.write(out)