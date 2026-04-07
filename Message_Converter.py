import re
import pyperclip  # pip install pyperclip

name = 'Message Converter (Dutch)'
CIPHER = "ISH"

# Single-pass regex: digraphs are listed before single vowels so they match
# first, preventing a vowel inside a digraph from being replaced twice.
_PATTERN = re.compile(r'oei|aa|ae|ee|oo|uu|au|ei|eu|ie|ou|oe|ui|ij|io|[aeoiuy]')


def convertword(word, cipher=CIPHER):
    return _PATTERN.sub(lambda m: cipher + m.group().upper(), word)


def convert_message(message, cipher=CIPHER):
    words = message.replace(",", "~").lower().split(" ")
    converted = [convertword(w, cipher) for w in words]
    result = " ".join(converted).replace("~", ",")

    # Capitalize the first letter of each sentence without lowercasing the rest.
    sentences = [s.strip() for s in result.split('.') if s.strip()]
    result = '. '.join(s[0].upper() + s[1:] for s in sentences)
    return result


print('=' * len(name))
print(name)
print('=' * len(name))

while True:
    try:
        message = input("\nEnter your message:\n:> ").strip()
        if not message:
            continue

        result = convert_message(message)

        print(f"\nYour message in {CIPHER}:")
        print(result)

        answer = input('\nCopy to clipboard? Y/N: ').strip().upper()
        if answer == 'Y':
            try:
                pyperclip.copy(result)
                print('\nMessage has been copied.')
            except Exception:
                print('\nCould not access clipboard.')
        else:
            print('\nMessage has NOT been copied.')

        again = input('\nConvert another? Y/N: ').strip().upper()
        if again != 'Y':
            print('\nGoodbye!\n')
            break

    except KeyboardInterrupt:
        print('\n\nGoodbye!\n')
        break
