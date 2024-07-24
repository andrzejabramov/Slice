import re


regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.com|\.ru|\.net)')

def isValid(email):
    return True if re.fullmatch(regex, email) else False

def send_email(message, recipient, sender='university.help@gmail.com'):
    if isValid(recipient) is False or isValid(sender) is False:
        note = f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}"
    elif recipient == sender:
        note = 'Нельзя отправить письмо самому себе!'
    elif sender == 'university.help@gmail.com':
        note = f"Письмо с текстом: {message} успешно отправлено с адреса {sender} на адрес {recipient}"
    else:
        note = f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо с текстом: {message} отправлено с адреса {sender} на адрес {recipient}."
    return note

message = '"Это сообщение для проверки связи"'
recipient = 'vasyok1337@gmail.com'
print(send_email(message, recipient))