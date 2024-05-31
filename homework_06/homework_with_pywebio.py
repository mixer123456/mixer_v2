from pywebio.input import input as input_pw
from pywebio.output import put_text, put_image, put_html

import constans_web

# html
put_html('<h1>Ура, наступний день – це літо!</h1>')
put_html(constans_web.vers)
input_pw(constans_web.plan_for_summer)
put_text(constans_web.count_plan_for_summer)
img = open('summer.avif', 'rb').read()
put_image(img, width='500px')
