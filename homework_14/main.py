import utils,configs



def main():
    list_of_recipients = [
        'mixer1234@ukr.net',
        'mixer1234@ukr.net',
        # 'blender495@ukr.net',
    ]
    utils.send_email(
        list_of_recipients,
        mail_subject='head',
        mail_body='<h1>body</h1>'
    )



if __name__ == '__main__':
    main()
