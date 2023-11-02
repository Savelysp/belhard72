user_text = input("введите текст ")
end_of_first_word = user_text.index(" ")
start_of_last_word = user_text.rindex(" ") + 1
first_word = user_text[:end_of_first_word]
last_word = user_text[start_of_last_word:]
center_of_text = user_text[end_of_first_word:start_of_last_word]
print(last_word + center_of_text + first_word)
