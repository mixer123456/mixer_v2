import utils, constants, configs


def main():
    list_of_recipients = [
        'mixer1234@ukr.net',
        'blender495@ukr.net',
    ]

    for res in list_of_recipients:
        params = {
            'subject': constants.MSG_SUBJECT,
            'recipient_name': f'{configs.USERNAME} <{configs.USERS_EMAIL}>',
            'body': constants.MSG_BODY,
            'sender_name': res,
        }
        body = utils.create_letter(params)
        utils.send_email(
            list_of_recipients,
            mail_subject=constants.MSG_SUBJECT,
            mail_body=body
        )


if __name__ == '__main__':
    main()
