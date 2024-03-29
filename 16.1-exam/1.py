def generate_letter (mail, name, date, time, place, teacher = 'Тимур Гуев', number = 17):
    str = ''
    str += f'To: {mail} \nПриветствую, {name}!\nВам назначен экзамен, который пройдет {date}, в {time}.\nПо адресу: {place}.\nЭкзамен будет проводить {teacher} в кабинете {number}.\nЖелаем удачи на экзамене!'
    return str

print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
print()
print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00',
                      'Часова 23, корпус 2', 'Василь Ярошевич', 23))