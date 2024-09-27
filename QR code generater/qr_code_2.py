import qrcode as qr
from PIL import Image

qr = qr.QRCode(version=1, error_correction=qr.constants.ERROR_CORRECT_H, box_size=10, border=4)

qr.add_data('www.google.com')

qr.make(fit=True)

qr.make_image(fill_color="yellow", back_color="blue").save('qr_code_2.png')
