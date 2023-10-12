def main():
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    TEXT = input("Enter a text: ")
    TEXT = TEXT.upper()

    

    print(TEXT)

    for alphabetLetter in alphabet:
        # print(alphabetLetter)
        count = 0
        # print(letter)
        for letter in TEXT:
            if alphabetLetter == letter:
                count += 1
        print(f"{alphabetLetter}: {count}")

        



main()