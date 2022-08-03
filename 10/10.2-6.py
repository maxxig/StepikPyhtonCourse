letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
slovar =[]
for i in range(len(letters)):
    slovar.append((letters[i], morse[i]))

dict_morze = dict(slovar)

string = input().upper()
result = ''

for s in string:
    if s in dict_morze:
        result = result + dict_morze[s] + ' '
print(result.strip())