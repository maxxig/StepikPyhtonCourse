string = input().upper()
d = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}
result = ''
for s in string:
    for key, value in d.items():
        if s in value:
            cnt = value.index(s) + 1
            result = result + (key * cnt)
            break
print(result)