# Пользователь вводит предложение, заменить все пробелы на "-" двумя способами
user_sentence = input("Введите предложение: ")
sentence_split = user_sentence.split(' ')
print('-'.join(sentence_split))
