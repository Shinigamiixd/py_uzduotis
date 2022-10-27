import os

# !PER CODERUNNER EXTENSION NEVEIKIA DEL ENCODING ERRORS(win11?)! #
# !VEIKIA TIK SU PYTHON 3.6+ DEL 26 LINE! #

vardai = []
path = os.listdir(os.getcwd())
print(path)

for file in(path):
    if file.endswith(".txt") and len(file) == 7:
        print(".txt found")
        with open(file, "r", encoding="utf-8") as r:
            vardai_open = r.readlines()
            vardai += vardai_open



vardai = [x[:-1] for x in vardai]
dupes = {i:vardai.count(i) for i in vardai}
print(dupes)

total_zenkliukai = len(vardai)

total_akcijos_kaina = 0
vals = list(dupes.values())

for i in vals:
    if i == 1:
        total_akcijos_kaina += 5
    elif i == 2:
        total_akcijos_kaina += 5+5
    elif i == 3:
        total_akcijos_kaina += 5+5+5
    elif i == 4:
        total_akcijos_kaina += 5+5+5+4
    elif i == 5:
        total_akcijos_kaina += 5+5+5+4+3
    elif i == 6:
        total_akcijos_kaina += 5+5+5+4+3+2
    elif i == 7:
        total_akcijos_kaina += 5+5+5+4+3+2+1
    
print(f"\nvisu zenkliuku kiekis: {total_zenkliukai}")
print(f"visu zenkliuku kaina be akciju: {total_zenkliukai * 5} Eur")
print(f"\nvisu zenkliuku kaina su akcijomis: {total_akcijos_kaina} Eur")



with open("sarasas.txt", "w", encoding='utf-8') as w:
    print(dupes, file=w)

with open("saskaita.txt", "w") as w:
    print(f"visu zenkliuku kiekis: {total_zenkliukai}", file=w)
    print(f"visu zenkliuku kaina be akciju: {total_zenkliukai * 5} Eur", file=w)
    print(f"visu zenkliuku kaina su akcijomis: {total_akcijos_kaina} Eur", file=w)

