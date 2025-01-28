import pyperclip

def clean_email():
    """
    Буфер обмена содержит строки текста.
    Очисти текст, удали любой символ > или пробел в начале каждой строки.
    Замени текст в буфере обмена на очищенный текст.
    """
    text = pyperclip.paste()
    lines = text.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].lstrip('>').lstrip()
    text = '\n'.join(lines)
    pyperclip.copy(text)
    
if __name__ == '__main__':
    clean_email()
