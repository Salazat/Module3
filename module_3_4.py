def single_root_words(root_word, *other_words):
    same_words = []
    root_word_lower = root_word.lower()

    for i in other_words:
        line_str = str(i)
        words = []
        space_word = ''
        index = 0
        x = len(line_str)

        while index < x:
            chart = line_str[index]
            if chart != ' ':
                space_word += chart
            else:
                if space_word != '':
                    words.append(space_word)
                    space_word = ''
            index += 1

        if space_word != '':
            words.append(space_word)
        for word in words:
            word_lower = word.lower()
            if word_lower.count(root_word_lower) > 0 or root_word_lower.count(word_lower) > 0:
                same_words.append(word)

    return same_words

root_word = 'день'
other_words = 'Дневной завтрак порой лучше съесть в будни или преддень'
result = single_root_words(root_word, other_words)
print('Однокоренные слова:', *result)
print(' ' + '-' * len(other_words))

root_word = 'Гол'
other_words = 'Оголенный провод под напряжением стал Оголяться'
result = single_root_words(root_word, other_words)
print('Однокоренные слова:', *result)
print(' ' + '-' * len(other_words))

print('Для самостоятельной проверки')
root_word = input('Введите искомый корень: ')
other_words = input('Введите строку с остальными словами: ')
result = single_root_words(root_word, other_words)
print('Однокоренные слова:', *result)

