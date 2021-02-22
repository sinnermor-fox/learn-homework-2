"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""
import urllib
from urllib import request


def main():
    url = "https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0"
    urllib.request.urlretrieve(url, 'referat.txt')
    with open('referat.txt', 'r') as f:
        file_data = f.readlines()
    print(f'Длина строки: {len(file_data)}')
    words = ''.join(file_data).split(' ')
    print(f'Кол-во слов: {len(words)}')
    new_words_str = ' '.join(words).replace('.', '!')
    with open('referat2.txt', 'w') as f:
        f.writelines(new_words_str)

    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    pass

if __name__ == "__main__":
    main()
