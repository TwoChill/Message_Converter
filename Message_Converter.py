import pyperclip  # $ pip install pyperclip

name = 'Message Converter'


def convertword(convertedMSG):

    convertedMSG = convertedMSG.split(",")

    # These are the letters to concatenate with the ciPher.
    vowelList = (("oei", "aa", "ae", "ee", "ae", "oo",
                  "uu", "au", "ei", "eu", "ie", "ou", "oe", "ui", "ij", "io"),
                 ("a", "e", "o", "u", "i", "y"))

    # Puts the 'ciPher' before the letters in vowelList
    for words in convertedMSG:
        for letters in vowelList[0]:
            if letters in words:
                replace = ciPher + letters.upper()
                words = words.replace(letters, replace)

        for word in words:
            for letter in words:
                if letter in vowelList[1]:
                    replace = ciPher + letter.upper()
                    words = words.replace(letter, replace)
    return words


print('\n')
print('=' * len(name))
print(name)
print('=' * len(name))

ciPher = "ISH"


try:
    convertedMSG = str(input("\nEnter your message:\n\n:> ")).strip('')

    # Replaces comma's and splits sentences to words in a list.
    convertedMSG = convertedMSG.replace(",", "~").lower().split(" ")

    convMSG = [(convertword(convertedMSG[index]))
                         for index in range(0, (len(convertedMSG)))]

    print("\n\n\nYour message in " + ciPher + ": \n")

    # Converts items in new_convertedMSG to a string, replaces comma's and '~' and splits by a dot.
    convMSG = " ".join(convMSG).capitalize().replace(
        "~", ",").split('.')

    # Makes every sentence begin with a capital letter and end with a dot.
    for i in convMSG:
        print(i.strip().capitalize() + ".")
    convMSG = ''.join(convMSG)
    
    # Ask the user if he/she wants to copy the new text to the clipboard.
    answer = str(input('\n\nCopy to clipboard? Y/N: ').upper()).strip()

    if answer == 'Y':
        pyperclip.copy(convMSG)
        print('\n\nMessage has been copied.')
        raise KeyboardInterrupt
    else:
        print('\n\nMessage has NOT been copied.')
        raise KeyboardInterrupt


except KeyboardInterrupt:
    print("\n\n\nGoodbye!\n")
