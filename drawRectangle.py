'''
在图片上上标注矩形框
'''
import requests
import base64
import json
import random
#图片处理：
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import time

def drawRectangle(image,box, size, color,border):
    #https://blog.csdn.net/wuguangbin1230/article/details/80348504
    # 画个边框为1的红色矩形框
    draw = ImageDraw.Draw(image)
    if len(box)==2:
        print("no 2 p")
        box.append(box[0]+size)
        box.append(box[1]+size)
    draw.rectangle(xy=(box[0], box[1], box[2], box[3]), fill=None, outline=color)
    return image
    
imgBadFace = "1631587643.jpeg"
#{Left:735.17 Top:1131.12 Width:1121 Height:1132}
L = 735.17
T = 1131.12
W = 1121
H = 1132
image = Image.open(imgBadFace) 
image = drawRectangle(image,[L,T,L+W,T+H],1,'red',3)
# draw = ImageDraw.Draw(image)

#{Left:806.09 Top:2943.62 Width:732 Height:768}
L = 806.09
T = 2943.62
W = 732
H = 768
image = drawRectangle(image,[L,T,L+W,T+H],1,'red',3)
draw = ImageDraw.Draw(image)
display(image)
