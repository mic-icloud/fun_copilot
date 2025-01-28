def count_words(words):
    count = 0
    for word in words:
        # считай только слова которые точно есть 'Dan' 
        if word == 'Dan':
            count += 1
    return count


words = ['Dan', 'danger', 'Leo']
print(count_words(words))

def most_students(classroom):
    """
    classroom - это список списков.
    Каждый ' ' - свободное место, каждый 'S' - студент.
    Найди наибольшее количество студентов, сидящих в ряду последовательно.
    >>> most_students([['S', ' ', 'S', 'S', 'S', 'S'], ['S', ' ', 'S', 'S', 'S', ' '], [' ', 'S', ' ', 'S', ' ', ' ']])
    4
    """
    max_count = 0
    for row in classroom:
        count = 0
        for seat in row:
            if seat == 'S':
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 0
    return max_count

import doctest
doctest.testmod()