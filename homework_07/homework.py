def welcome_user_message(username):
    normalized_username = username.strip()
    return f'<h1>Вітаємо тебе, шановний {normalized_username}</h1>'


def calculating_area_rectangle(width, height):
    # if width < 0 or height < 0:
    #     return False
    return width * height
