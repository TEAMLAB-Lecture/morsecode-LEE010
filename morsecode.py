# -*- coding: utf8 -*-
import re

# Help Function - 수정하지 말 것


def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code

# Help Function - 수정하지 말 것


def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message


def is_help_command(user_input):
    cmd = user_input.lower()
    return cmd == 'h' or cmd == 'help'


def is_validated_digit(user_input):
    digit_regex = re.compile('[0-9]')
    return not digit_regex.search(user_input)


def is_validated_special(user_input):
    return user_input.isalnum()


def get_sub_mark(sentence):
    mark_regex = re.compile('[.,!?]')
    return mark_regex.sub('', sentence)


def is_validated_english_sentence(user_input):
    sentence = user_input.replace(' ', '')
    sentence = get_sub_mark(sentence)

    return is_validated_digit(sentence) \
        and is_validated_special(sentence) and sentence != ''


def is_validated_morse_code(user_input):
    user_codes = user_input.split(' ')
    morse_codes = set(get_morse_code_dict().values())
    morse_codes.add('')

    for code in user_codes:
        if code not in morse_codes:
            return False

    return True


def get_cleaned_english_sentence(raw_english_sentence):
    return get_sub_mark(raw_english_sentence).strip()


def decoding_character(morse_character):
    morse_code_dict = get_morse_code_dict()
    alphabet_to_morse = {v: k for k, v in morse_code_dict.items()}
    alphabet_to_morse[''] = ' '

    return alphabet_to_morse[morse_character]


def encoding_character(english_character):
    morse_code_dict = get_morse_code_dict()
    morse_code_dict[' '] = ''

    return morse_code_dict[english_character]


def decoding_sentence(morse_sentence):
    return ''.join(map(decoding_character, morse_sentence.split(' ')))


def encoding_sentence(english_sentence):
    space_regex = re.compile(r'\ +')

    cleaned_sentence = get_cleaned_english_sentence(english_sentence).upper()
    cleaned_sentence = space_regex.sub(' ', cleaned_sentence)

    return ' '.join(map(encoding_character, cleaned_sentence))


def main():
    print("Morse Code Program!!")

    while True:
        user_input = input('Input your message(H - Help, 0 - Exit): ')

        if user_input == '0':
            break
        elif is_help_command(input):
            get_help_message()
        elif is_validated_english_sentence(user_input):
            print(encoding_sentence(user_input))
        elif is_validated_morse_code(user_input):
            print(decoding_sentence(user_input))
        else:
            print("Wrong Input")

    print("Good Bye")
    print("Morse Code Program Finished!!")


if __name__ == "__main__":
    main()
