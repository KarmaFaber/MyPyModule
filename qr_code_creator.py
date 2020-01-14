#command prompt -> pip install qrcode
#command prompt -> pip install pillow (image)

#ERROR_CORRECT_L-About 7% or less errors can be corrected.
#ERROR_CORRECT_M-(default)-About 15% or less errors can be corrected.
#ERROR_CORRECT_Q-About 25% or less errors can be corrected.
#ERROR_CORRECT_H-About 30% or less errors can be corrected.
#----------------------------------------------------------------------------------------------------------------

#to use this def -->
#from MyPyModule.qr_code_creator import *
#create_QR_code(data) -->  data="https://github.com/KarmaFaber"

import qrcode
from random_string_creator import id_generator
from pillow import Image, ImageDraw, ImageFont
import random
import datetime

def create_QR_code(data):
    qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

    data=""
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill="black", black_color="black")

    name=id_generator(5)
    img_name=""+name+"{}".format(".png")

    img.save(img_name) 
    return img






def id_creator(name, lastname, passport, company):
    #image:
    image = Image.new('RGB', (1000,900), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', size=45)

    #date and time:
    d_date = datetime.datetime.now()
    reg_format_date = d_date.strftime("  %d-%m-%Y\t\t ID CARD Generator\t\t\t\t\t  %I:%M:%S %p")

    #date, name, lastname, passport, company:---
    (x, y) = (50, 250)
    message = ""
    date=message
    color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype('arial.ttf', size=45)
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (50, 350)
    message = ""
    name=message
    color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype('arial.ttf', size=45)
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (600, 75)
    idno=random.randint(10000000,90000000)
    message = str('ID '+str(idno))
    color = 'rgb(89, 62, 100)' # black color
    font = ImageFont.truetype('arial.ttf', size=60)
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (50, 450)
    message = ""
    lastname=message
    color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype('arial.ttf', size=45)
    draw.text((x, y), message, fill=color, font=font)
    
    (x, y) = (50, 250)
    message = ""
    passport=message
    color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype('arial.ttf', size=45)
    draw.text((x, y), message, fill=color, font=font)

    # save the edited image
    image.save(str(name)+'.png')

    img = qrcode.make(str(company)+str(idno))   
    img.save(str(idno)+'.bmp')

    til = Image.open(name+'.png')
    im = Image.open(str(idno)+'.bmp') 
    til.paste(im,(600,350))
    til.save(name+'.png')

    
print(id_creator("maria", "karma", "jajdbkj", "sinfatinogas"))
