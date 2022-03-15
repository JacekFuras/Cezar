from os.path import join


def Decode(shift_parameter):
    rawText = ([letters for letters in input("Wpisz wiadomosc do odszyfrowania: ").lower()])

    rawTextLength = range(len(rawText))
    codedResult = [letters for letters in rawText]
    for i in rawTextLength:

        if ord(rawText[i]) == 32:
            codedLetter = ord(rawText[i])
            codedResult[i] = chr(codedLetter)

        # od d do z
        if ord(rawText[i]) + (26 - shift_parameter) >= 123 and ord(rawText[i]) != 32:
            codedLetter = ord(rawText[i]) - shift_parameter
            codedResult[i] = chr(codedLetter)

        if ord(rawText[i]) + (26 - shift_parameter) < 123 and ord(rawText[i]) != 32:
            codedLetter = ord(rawText[i]) + (26 - shift_parameter)

            codedResult[i] = chr(codedLetter)

    print(*codedResult, sep='')


def Encode(shift_paremeter):
    rawText = ([letters for letters in input("Wpisz wiadomosc do zaszyfrowania: ").lower()])

    rawTextLength = range(len(rawText))
    codedResult = [letters for letters in rawText]
    for i in rawTextLength:

        if ord(rawText[i]) == 32:
            codedLetter = ord(rawText[i])
            codedResult[i] = chr(codedLetter)

        if ord(rawText[i]) + shift_paremeter <= 122 and ord(rawText[i]) != 32:
            print(ord(rawText[i]))
            codedLetter = ord(rawText[i]) + shift_paremeter
            codedResult[i] = chr(codedLetter)

        if ord(rawText[i]) + shift_paremeter > 122 and ord(rawText[i]) != 32:
            codedLetter = ord(rawText[i]) - (26 - shift_paremeter)

            print(ord(rawText[i]))
            codedResult[i] = chr(codedLetter)

    print(*codedResult, sep='')


def Program():
    x = input("Kodowanie wiadomosci (1), Dekodowanie wiadomosci (2): ")
    shift_paremeter = int(input("wpisz paramter przesuniecia: "))
    if 26 > shift_paremeter > 0:
        match x:
            case '1':
                return Encode(shift_paremeter)
            case '2':
                return Decode(shift_paremeter)


Program()
