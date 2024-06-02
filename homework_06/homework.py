# homework 6 "working with pywebio"

from pywebio.input import textarea
from pywebio.output import put_text, put_image, put_html
import messages

# configuration
page_main_image_path = 'summer.avif'
page_main_image_width_px = 500

# html
put_html(f'<h1>{messages.PAGE_HEADER}</h1>')
put_text(messages.PAGE_CONTENT)

users_plan = textarea(
    label=messages.SUMMER_PLAN_REQUEST,
    placeholder=messages.SUMMER_PLAN_REQUEST)

put_text(messages.SUMMER_PLAN_INFO.format(
    info=len(users_plan)
))

img = open(page_main_image_path, 'rb').read()
put_image(img, width=f'{page_main_image_width_px}px')
put_text('end')
