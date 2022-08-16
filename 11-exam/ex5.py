d = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}
input = input()
points = 0
for letter in input:
    for k, v in d.items():
        if letter in v:
            points += k
            break
print(points)