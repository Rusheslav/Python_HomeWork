# Напишите программу, удаляющую из текста все слова,
# в которых присутствуют все буквы "абв".

text = input('Введите текст: ')

tmp = []
for word in text.split():
    w = word.lower()
    if not ('а' in w and 'б' in w and 'в' in w):
        tmp.append(word)

print(' '.join(tmp))