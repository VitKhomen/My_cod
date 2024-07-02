
direction = input('Что нужно, шифрование или дешифрование?(Ш или Д) ')
leng = input('На каком языке, русский или английский?(Р или А) ')
chip_step = int(input('Какой шаг сдвига: '))
text = input('Введите текст: ')
cesar_text = ''
if direction == 'Д' and leng == 'А':
    chip_step = 26 - chip_step
if direction == 'Д' and leng == 'Р':
    chip_step = 32 - chip_step


for i in range(len(text)):
    if text[i].isalpha():
        if ord(text[i].lower()) in range(97, 123):
            if text[i].islower():
                cesar_text += chr((ord(text[i]) % 97 + chip_step) % 26 + 97)
            else:
                cesar_text += chr((ord(text[i].lower()) % 97 + chip_step) %
                                  26 + 97).upper()
        if ord(text[i].lower()) in range(1072, 1104):
            if text[i].islower():
                cesar_text += chr((ord(text[i]) %
                                  1072 + chip_step) % 32 + 1072)
            else:
                cesar_text += chr((ord(text[i].lower()) %
                                   1072 + chip_step) % 32 + 1072).upper()
    else:
        cesar_text += text[i]

print(cesar_text)
