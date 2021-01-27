def person_print(name, last_name, age, *others):
    formatted_data = 'Imię: {}, nazwisko: {}, wiek: {}' \
                     .format(name, last_name, age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)
person_print('Arkadiusz', 'Majczyna', 21, "te;. 123123123")
