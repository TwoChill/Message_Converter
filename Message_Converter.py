import pyperclip  # $ pip install pyperclip

name = 'Message Converter (Dutch)'


def convertword(word):
    # These are the letters to concatenate with the ciPher.
    vowel_list = (("oei", "aa", "ae", "ee", "ae", "oo", "uu", "au", "ei", "eu", "ie", "ou", "oe", "ui", "ij", "io"),
                  ("a", "e", "o", "u", "i", "y"))

    # Puts the 'ciPher' before the letters in vowel_list
    for letters in vowel_list[0]:
        if letters in word:
            word = word.replace(letters, ciPher + letters.upper())

    for letter in vowel_list[1]:
        if letter in word:
            word = word.replace(letter, ciPher + letter.upper())

    return word

print('=' * len(name))
print(name)
print('=' * len(name))

ciPher = "ISH"

try:
    convertedMSG = str(input("\nEnter your message:\n:> ")).strip()

    # Replaces commas and splits sentences to words in a list.
    convertedMSG = convertedMSG.replace(",", "~").lower().split(" ")

    # Convert each word in the message
    convMSG = [convertword(word) for word in convertedMSG]

    print("\nYour message in " + ciPher)

    # Join words into a single string, replace temporary '~' back to ',', and capitalize sentences.
    convMSG = " ".join(convMSG).replace("~", ",").capitalize()

    # Split by sentences to ensure capitalization after periods
    sentences = convMSG.split('.')
    convMSG = '. '.join(sentence.strip().capitalize() for sentence in sentences if sentence)

    print(convMSG)

    # Ask the user if they want to copy the new text to the clipboard.
    answer = str(input('\n\nCopy to clipboard? Y/N: ').upper()).strip()

    if answer == 'Y':
        pyperclip.copy(convMSG)
        print('\nMessage has been copied.')
    else:
        print('\nMessage has NOT been copied.')

except KeyboardInterrupt:
    print("\n\n\nGoodbye!\n")
