# выводит на экран всех студентов средний балл которых выше заданного
def print_greater(group_list, target):
    records_present = False # флажок устанавливающий наличие записей отвечающих условию
    for record in group_list:
        avg = sum(record['grades'])/len(record['grades'])
        if avg > target:
            # Если флажок остался False, то выводится шапка таблицы и он ставится True
            if not records_present:
                # Вывод шапки
                print(u'Имя'.ljust(15), u'Фамилия'.ljust(25), u'Экзамены'.ljust(50),
                      u'Оценки'.ljust(10), u'Средний балл'.ljust(3))
                records_present = True
            # Вывод записей
            print(record['firstname'].ljust(15), record['lastname'].ljust(25),
                  str(record['exams']).ljust(50), str(record['grades']).ljust(10),
                  str(avg)[:3])  # обрезание лишних цифр


# все персонажи вымышлены,а любые совпадения с реальными личностями случайны
group_mates = [{'firstname': 'Алексей', 'lastname': 'Сурьянов',
                'exams': ['Инофрматика', 'Английский язык', 'Астрономия'], 'grades': [4, 3, 5]},
               {'firstname': 'Валерия', 'lastname': 'Крылова',
                'exams': ['Инофрматика', 'Химия', 'Физика'], 'grades': [4, 4, 5]},
               {'firstname': 'Георг', 'lastname': 'Стоктон',
                'exams': ['Химия', 'Физика'], 'grades': [3, 4]},
               {'firstname': 'Ян', 'lastname': 'Жижка',
                'exams': ['История', 'Мат анализ', 'Алгебра', 'Физика'], 'grades': [5, 3, 4, 3]},
               {'firstname': 'Зоя', 'lastname': 'Лесинских',
                'exams': ['Мат анализ', 'Инофрматикка', 'Английский язык'], 'grades': [5, 5, 5]},
               {'firstname': 'Али', 'lastname': 'Мугаммедов',
                'exams': ['Физика', 'Химия', 'Мат анализ'], 'grades': [3, 4, 4]}]
# Ввод пользователем среднего балла
grade = float(input('Введите требуемый средний балл:'))
print_greater(group_mates, grade)

