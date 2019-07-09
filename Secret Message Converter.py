import pyperclip # $ pip install pyperclip

name = 'Secret Message Converter'

def convertword(convertedMSG):

    convertedMSG = convertedMSG.split(",")

    # These are the letters to concatenate with the SecretWord.
    ISHvowelList = (("oei", "aa","ae","ee","ae","oo",
     "uu", "au", "ei","eu", "ie", "ou", "oe", "ui", "ij","io"),
     ("a", "e", "o", "u", "i", "y"))

    for words in convertedMSG:
        for letters in ISHvowelList[0]:
            if letters in words:
                replace = secretWord + letters.upper()
                words = words.replace(letters, replace)


        for word in words:
            for letter in words:
                if letter in ISHvowelList[1]:
                    replace = secretWord + letter.upper()
                    words = words.replace(letter, replace)
    return words

print('\n')
print('=' * len(name))
print(name)
print('=' * len(name))

secretWord = "ISH"

try:
    convertedMSG = str(input("\nPlease enter your message:\n\n"))

    # Replaces comma's and splits sentences to words in a list.
    convertedMSG = convertedMSG.replace(",","~").lower().split(" ")

    # The manipulated words are appended to 'new_converterdMSG'.
    new_converterdMSG = []
    for index in range(0,(len(convertedMSG))):
        new_converterdMSG.append(convertword(convertedMSG[index]))

    print("\n\n\nYour message in " + secretWord + ": \n")

    # Converts items in new_convertedMSG to a string.
    convMSG = " ".join(new_converterdMSG).capitalize()

    # Puts back the comma's.
    convMSG = convMSG.replace("~",",")

    # Makes every sentence begin with a capital letter and end with a dot.
    sentence = convMSG.split('.')
    for i in sentence:
        print (i.strip().capitalize() + ". ", end='')


    answer = str(input('\n\n\n\nCopy to clipboard? Y/N: ').upper())
    if answer == 'Y':
        pyperclip.copy(convMSG)
        print('\n\nMessage has been copied.')
        raise KeyboardInterrupt
    else:
        print('\n\nMessage has NOT been copied.')
        raise KeyboardInterrupt



except KeyboardInterrupt:
    print("\n\n\nGoodbye!\n")
