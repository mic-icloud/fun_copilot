import os
import string


def clean_word(word):
    """
    word - это строка.
    
    Верни версию слова, в котором все буквы переведены в нижний регистр,
    а знаки препинания удалены с обоих концов.
    
    Внутренняя пунктуация должна быть сохранена.

    >>> clean_word('Hello!')
    'hello'
    >>> clean_word('card-board')
    'card-board'
    """
    word = word.lower()
    word = word.strip(string.punctuation)
    return word

def average_word_length(text):
    """
    text - это строка.
    
    Верни среднюю длину слова в тексте.
    Не засчитывай пустые слова как слова.
    Не учитывай окружающую пунктуацию.
    >>> average_word_length('A pearl! Pearl! Lustrous pearl! Rare. What a nice find.')
    4.1
    """
    words = text.split()
    total = 0
    count = 0
    for word in words:
        word = clean_word(word)
        if word:
            total += len(word)
            count += 1
    return total / count

def different_to_total(text):
    """
    text - это строка.
    
    Верни колличество уникальных слов в тексте, разделенное на общее количество слов в тексте.
    Не засчитывай пустые слова как слова.
    Не учитывай окружающую пунктуацию.
    >>> different_to_total('A pearl! Pearl! Lustrous pearl! Rare. What a nice find.')
    0.7
    """
    words = text.split()
    total = 0
    unique = set()
    for word in words:
        word = clean_word(word)
        if word:
            total += 1
            unique.add(word)
    return len(unique) / total

def exactly_once_to_total(text):
    """
    text - это строка.
    Верни количество слов, которые появляются в тексте ровно один раз, деленное на общее количество слов в тексте.
    Не засчитывай пустые слова как слова. Не учитывай окружающую пунктуацию.
    >>> exactly_once_to_total('A pearl! Pearl! Lustrous pearl! Rare. What a nice find.')
    0.5
    """
    words = text.split()
    total = 0
    unique = set()
    once = set()
    for word in words:
        word = clean_word(word)
        if word:
            total += 1
            if word in unique:
                once.discard(word)
            else:
                unique.add(word)
                once.add(word)
    return len(once) / total
    
def split_string(text, separators):
    """
    text - это строка.
    separators - это строка символов-разделителей.
    Раздели текст на список, используя любой односимвольный разделитель из separators и верни результат.
    Удали пробелы из начала и конца строки перед добавлением в список.
    Не добавляй в список пустые строки.
    
    >>> split_string('one*two[three', '*[')
    ['one', 'two', 'three']
    >>> split_string('A pearl! Pearl! Lustrous pearl! Rare. What a nice find.', '!.?')
    ['A pearl', 'Pearl', 'Lustrous pearl', 'Rare', 'What a nice find']
    """
    words = []
    word = ''
    for char in text:
        if char in separators:
            word = word.strip()
            if word:
                words.append(word)
            word = ''
        else:
            word += char
    word = word.strip()
    if word:
        words.append(word)
    return words
    
def get_sentences(text):
    """
    text - это строка.
    Верни список предложений в тексте.
    Предложения разделяются символами '.', '!', '?'.
    
    >>> get_sentences('A pearl! Pearl! Lustrous pearl! Rare. What a nice find.')
    ['A pearl', 'Pearl', 'Lustrous pearl', 'Rare', 'What a nice find']
    """
    return split_string(text, '.!?')

def average_sentence_length(text):
    """
    text - это строка.
    Верни среднее количество слов в предложении.
    Не засчитывай пустые слова как слова.
    >>> average_sentence_length('A pearl! Pearl! Lustrous pearl! Rare. What a nice find.')
    2.0
    """
    sentences = get_sentences(text)
    total = 0
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            if word:
                total += 1
    return total / len(sentences)

def get_phrases(sentence):
    """
    sentence - это строка предложения.
    Фразы отделяются запятой ',', точкой с запятой (;) или двоеточием (:).
    Верни список фраз в предложении.
    
    >>> get_phrases('Lustrous pearl, Rare, What a nice find')
    ['Lustrous pearl', 'Rare', 'What a nice find']
    """
    return split_string(sentence, ',;:')

def average_sentence_complexity(text):
    """
    text - это строка текста.
    Верни среднее количество фраз в предложении текста.
    
    >>> average_sentence_complexity('A pearl! Pearl! Lustrous pearl! Rare. What a nice find.')
    1.0
    >>> average_sentence_complexity('A pearl! Pearl! Lustrous pearl! Rare, what a nice find.')
    1.25
    """
    sentences = get_sentences(text)
    total = 0
    for sentence in sentences:
        phrases = get_phrases(sentence)
        total += len(phrases)
    return total / len(sentences)
    
def make_signature(text) -> list :
    """
    Сигнатура текста - это список из 5 элементов: 
    средняя длина слова;
    разные слова деленные на общее количество слов;
    слова, использованные ровно один раз, деленные на общее количество слов;
    средняя длина предложения;
    средняя сложность предложения.
    Верни сигнатуру текста.
    >>> make_signature('A pearl! Pearl! Lustrous pearl! Rare, what a nice find.')
    [4.1, 0.7, 0.5, 2.5, 1.25]
    """
    return [average_word_length(text), 
            different_to_total(text), 
            exactly_once_to_total(text), 
            average_sentence_length(text), 
            average_sentence_complexity(text)]
    

def get_all_signatures(known_dir) -> dict:
    """
    known_dir - это имя каталога книг.
    Определи сигнатуру каждого файла в каталоге known_dir.
    Верни словарь, где ключ - это имя файла, а значение - это сигнатура файла.
    """
    signatures = {}
    # Исправь UnicodeDecodeError
    for file in os.listdir(known_dir):
        with open(os.path.join(known_dir, file), 'r', encoding='utf-8') as f:
            text = f.read()
            signatures[file] = make_signature(text)
    return signatures

def get_score(signature1, signature2, weights) -> float:
    """
    signature1 - это сигнатура текста 1.
    signature2 - это сигнатура текста 2.
    weights - это список пяти весов.
    Верни балл для signature1 и signature2.
    
    >>> get_score([4.6, 0.1, 0.05, 10, 2], [4.3, 0.1, 0.04, 16, 4], [11, 33, 50, 0.4, 4])
    14.2
    """
    score = 0
    for i in range(5):
        score += abs(signature1[i] - signature2[i]) * weights[i]
    return score

def lowest_score(signatures_dict, unknown_signature, weights):
    """
    signatures_dict - это словарь сопоставления сигнатур
    unknown_signature - это сигнатура неизвестного текста.
    weights - это список пяти весов.
    Верни ключ, значение сигнатуры которого имеет наименьший балл с unknown_signature.

    >>> d = {'Dan': [1,1,1,1,1], 'Leo': [3,3,3,3,3]}
    >>> unknown = [1, 0.8, 0.9, 1.3, 1.4]
    >>> weights = [11, 33, 50, 0.4, 4]
    >>> lowest_score(d, unknown, weights)
    'Dan'
    """
    lowest = None
    for key in signatures_dict:
        score = get_score(signatures_dict[key], unknown_signature, weights)
        if lowest is None or score < lowest[1]:
            lowest = (key, score)
    return lowest[0]

def process_data(mystery_filename, known_dir):
    """
    mystery_filename - это имя файла неизвестной книги, автора которой нужно определить.
    known_dir - это имя каталога книг.
    Верни имя сигнатуры, наиболее блзкое к сигнатуре текста mystery_filename.
    """
    signatures = get_all_signatures(known_dir)
    with open(mystery_filename, 'r', encoding='utf-8') as f:
        text = f.read()
        unknown_signature = make_signature(text)
    return lowest_score(signatures, unknown_signature, [11, 33, 50, 0.4, 4])

def make_guess(known_dir):
    """
    Запроси у пользователя имя файла неизвестной книги.
    Получи все сигнатуры книг в known_dir и выведи имя той из них,
    которая имеет наименьший балл с именем файла пользователя.
    """
    filename = input('Enter the filename: ')
    print(process_data(filename, known_dir))

import doctest
doctest.testmod()

make_guess('ch7/known_authors')
