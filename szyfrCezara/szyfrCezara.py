text = input("Podaj tekst: ") 
key = int(input("Podaj klucz: ")) 
encryptedText = "" 

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] 

for letter in text: 
    # print(letter) 
    if letter in alphabet: 
        index = alphabet.index(letter) +1
        # print(index) 
        encryptedIndex = index + key
        while encryptedIndex > len(alphabet):
            encryptedIndex = encryptedIndex - len(alphabet)
        # print(encryptedIndex)
        encryptedLetter = alphabet[encryptedIndex] 
        encryptedText = encryptedText + encryptedLetter 
    else:  
        encryptedText = encryptedText + letter 


print("Szyfr: " + encryptedText) 
