from collections import Counter
# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('a'))# ???

#
# # Вывести количество гласных букв в слове
word = 'Архангельск'
print(sum([1 for el in word.lower() if el in set('ёуеыаоэяию')]))#
#
# # Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(' ')))

#
#
# # Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for el in sentence.split(' '):
    print(el[0])

#
#
# # Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
words = sentence.split(' ')
avg = sum([len(el) for el in words])/len(words)
print(avg)
# # ???