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
from MyPyModule.random_string import id_generator

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