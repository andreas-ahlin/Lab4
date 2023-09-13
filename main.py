from bintreeFile import Bintree


def makechildren(startordet):
    svenska = Bintree()
    gamla = Bintree()
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()                # Ett trebokstavsord per rad
            if ordet in svenska:
                None
            else:
                svenska.put(ordet)

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                   'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
        for i in range(0, 3):
            barn = [*startordet]
            for searchletter in letters:
                barn[i] = searchletter
                newword = barn[0]+barn[1]+barn[2]
                if newword in svenska and not newword in gamla and newword != startordet:
                    print(newword)
                    gamla.put(newword)


def main():
    startord = input('Skriv in startord:')
    makechildren(startord)


main()
