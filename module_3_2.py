def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    if len(recipient) < 4 or len(sender) < 4:
        return
    if (('@' not in recipient or
            '.com' not in recipient[-4:] and
            '.ru' not in recipient[-3:] and
            '.net' not in recipient[-4:]) or
        ('@' not in sender or
         '.com' not in sender[-4:] and
         '.ru' not in sender[-3:] and
         '.net' not in sender[-4:])):
        print( "Невозможно отправить письмо с адреса <", sender, "> на адрес <", recipient, ">.")
        return
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender != "university.help@gmail.com":
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <", sender, "> на адрес <", recipient, ">.")
        return
    else:
        print("Письмо успешно отправлено с адреса <", sender, "> на адрес <", recipient, ">.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')