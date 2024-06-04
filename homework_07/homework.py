def welcome_user_message(username):
    normalized_username = username.title().strip()
    return f'<h1>Вітаємо тебе, шановний {normalized_username}</h1>'


def area_of_the_rectangle(a, b):
    if a < 0 or b < 0:
        return False
    return a * b
