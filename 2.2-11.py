alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
word = input() + ' запретил букву'

for i in alphabet:
    if word.find(i) >=0:
        print(word + ' ' + i)
        word = word.replace(i, '').strip()
        word = word.replace('  ', ' ')
    if len(word) == 0:
        break