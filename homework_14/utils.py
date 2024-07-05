from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import jinja2

import configs, constants


def send_email(
        recipients: list[str],
        *,
        mail_body: str,
        mail_subject: str,
):
    TOKEN = configs.TOKEN_UKR_NET
    USERS_EMAIL = configs.USERS_EMAIL
    USERNAME = configs.USERNAME
    SMTP_SERVER = configs.STMP_SERVER

    msg = MIMEMultipart('alternative')
    msg['Subject'] = mail_subject
    msg['From'] = constants.MSG_FROM.format(users_email=USERS_EMAIL)
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = f'{USERNAME} ({USERS_EMAIL})'
    msg['Return-Path'] = f'{USERNAME} ({USERS_EMAIL})'
    msg['X-Mailer'] = 'decorator'

    text_to_send = MIMEText(mail_body, 'html')
    msg.attach(text_to_send)

    mail = smtplib.SMTP_SSL(SMTP_SERVER)
    mail.login(USERS_EMAIL, TOKEN)
    mail.sendmail(USERS_EMAIL, recipients, msg.as_string())
    mail.quit()


def create_letter(params: dict) -> str:
    template_loader = jinja2.FileSystemLoader(searchpath='.')
    template_env = jinja2.Environment(loader=template_loader)
    template_file = 'template_letter.html'
    template = template_env.get_template(template_file)
    result = template.render(params)
    print(result)
    return result
