from collections import Counter

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
counted_names = Counter([el['first_name'] for el in students])
for name, value in counted_names.items():
    print(f"{name}: {value}")

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
most_common = Counter([el['first_name'] for el in students]).most_common(1)[0][0]
print(f"Самое частое имя среди учеников: {most_common}")

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ]
]
i = 1
for students in school_students:
    names = [student['first_name'] for student in students]
    most_common = Counter(names).most_common(1)[0][0]
    print(f"Самое частое имя в классе {i}: {most_common}")
    i += 1

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
for school_class in school:
    students = [student['first_name'] for student in school_class['students']]
    male_count = sum([1 for person in students if is_male[person]])
    female_count = sum([1 for person in students if not is_male[person]])
    print(f" В классе {school_class['class']} {female_count} девочки и {male_count} мальчика.")


# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
for school_class in school:
    students = [student['first_name'] for student in school_class['students']]
    male_count = sum([1 for person in students if is_male[person]])
    female_count = sum([1 for person in students if not is_male[person]])
    school_class['female_count'] = female_count
    school_class['male_count'] = male_count
male_sorted = sorted(school, key= lambda i: i['male_count'], reverse=True)
female_sorted = sorted(school, key= lambda i: i['female_count'], reverse=True)
print(f"Больше всего мальчиков в классе {male_sorted[0]['class']}")
print(f"Больше всего мальчиков в классе {female_sorted[0]['class']}")
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
