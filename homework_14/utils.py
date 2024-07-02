from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

import configs, constants


def send_email(
        recipients: list[str],
        *,
        mail_body: str,
        mail_subject: str,
):
    TOKEN = configs.TOKEN_UKR_NET
    USER = configs.MAIL_USER
    SMTP_SERVER = configs.STMP_SERVER

    msg = MIMEMultipart('alternative')
    msg['Subject'] = mail_subject
    msg['From'] = constants.MSG_FROM.format(user=USER)
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = USER
    msg['Return-Path'] = USER
    msg['X-Mailer'] = 'decorator'


    text_to_send = MIMEText(mail_body, 'html')
    msg.attach(text_to_send)

    mail = smtplib.SMTP_SSL(SMTP_SERVER)
    mail.login(USER, TOKEN)
    mail.sendmail(USER, recipients, msg.as_string())
    mail.quit()

