import random

def random_string(length):
    """"
    length - это целое число.
    Верни строку заданной длины, где каждый символ - это цифра от 0 до 9, без повторений.
    """
    s = ''
    while len(s) < length:
        digit = str(random.randint(0, 9))
        if digit not in s:
            s += digit
    return s


def get_guess(length):
    """"
    length - это длина строки.
    Продолжфй просить игрока ввести строку, в которой каждый символ является цифрой от 0 до 9,
    пока игрок не введет правильную догатку,
    Правильная догадка имеет заданную длину и не содержит повторяющихся цифр.
    """
    guess = input('Enter a guess: ')
    while len(guess) != length or not guess.isdigit() or len(set(guess)) != length:
        guess = input('Enter a guess: ')
    return guess

def guess_result(guess, secret_code):
    """
    guess и secret_code - это строки одинаковой длины.
    Верни список из двух значений: первое значение - колличество индексов в guess,
    где символ в этом индексе совпадает с символом в secret_code;
    второе значение - колличество индексов в guess, где символ в этом индексе
    существует в другом индексе в secret_code.
    >>> guess_result('3821', '1862')
    [1, 2]
    >>> guess_result('1234', '4321')
    [0, 4]    
    """
    bulls = cows = 0
    for i in range(len(guess)):
        if guess[i] == secret_code[i]:
            bulls += 1
        elif guess[i] in secret_code:
            cows += 1
    return [bulls, cows]

def play(num_digits, num_guesses):
    """"
    Создай случайную строку с цифрами num_digits.
    У игрока есть догадки num_guesses, чтобы угадать эту строку.
    После каждой догадки игроку сообщается, сколько цифр находится на правильных местах (bulls)
    и сколько цифр находится на неправильных местах (cows).
    """
    answer = random_string(num_digits)
    print('I generated a random {}-digit number for you to guess.'.format(num_digits))
    print('You have {} guesses to get it.'.format(num_guesses))
    for i in range(num_guesses):
        guess = get_guess(num_digits)
        result = guess_result(guess, answer)
        print('Correct: {}, Missed: {}'.format(result[0], result[1]))
        if guess == answer:
            print('You win!')
            return
    print('You lose. The correct answer was {}.'.format(answer))
    
play(4, 10)