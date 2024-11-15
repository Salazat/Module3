def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    def valid_email(email):
        simvol = False
        for i in email:
            if i == '@':
                simvol = True
                break

        domain = False
        if len(email) >= 4:
            if email[-4:] == '.com' or email[-4:] == '.net':
                domain = True
        if len(email) >=3:
            if email[-3:] == '.ru':
                domain = True

        if simvol == True:
            if domain == True:
                result = True
            else:
                result = False
        else:
            result = False
        return result

    recipient_valid = valid_email(recipient)
    send_valid = valid_email(sender)
    if recipient_valid == False or send_valid == False:
        print("Невозможно отправить письмо с адреса", sender, "На адрес", recipient)
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender,"на адрес", recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
