import os

# !PER CODERUNNER EXTENSION NEVEIKIA DEL ENCODING ERRORS(win11?)! #
# !VEIKIA TIK SU PYTHON 3.6+ DEL 26 LINE! #

vardai = []
path = os.listdir(os.getcwd())
print(path)

for file in(path):
    if file.endswith(".txt") and len(file) == 7:
        #print(".txt found")
        with open(file, "r", encoding="utf-8") as r:
            vardai_open = r.readlines()
            vardai += vardai_open



vardai = [x[:-1] for x in vardai]
dupes = {i:vardai.count(i) for i in vardai}
#print(dupes)

total_zenkliukai = len(vardai)

total_akcijos_kaina = 0
mokiniu_vardai_kainos = {}
kainu_map = {
    1: 5,
    2: 10,
    3: 15,
    4: 19,
    5: 22,
    6: 24,
    7: 25
}

for name, i in dupes.items():
    vardo_kaina = 0

    if i == 1:
        total_akcijos_kaina += kainu_map[i]
        vardo_kaina += kainu_map[i]

    elif i == 2:
        total_akcijos_kaina += kainu_map[i]
        vardo_kaina += kainu_map[i]

    elif i == 3:
        total_akcijos_kaina += kainu_map[i]
        vardo_kaina += kainu_map[i]

    elif i == 4:
        total_akcijos_kaina += kainu_map[i]
        vardo_kaina += kainu_map[i]

    elif i == 5:
        total_akcijos_kaina += kainu_map[i]
        vardo_kaina += kainu_map[i]

    elif i == 6:
        total_akcijos_kaina += kainu_map[i]
        vardo_kaina += kainu_map[i]

    elif i == 7:
        total_akcijos_kaina += kainu_map[i]
        vardo_kaina += kainu_map[i]

    elif i >= 8:
        total_akcijos_kaina += kainu_map[i]
        vardo_kaina += kainu_map[i]
        i -= 7
        for a in range(i):
            total_akcijos_kaina += 1
            vardo_kaina += 1

    mokiniu_vardai_kainos[name]=i
    
print(f"\nvisu zenkliuku kiekis: {total_zenkliukai}")
print(f"visu zenkliuku kaina be akciju: {total_zenkliukai * 5} Eur")
print(f"\nvisu zenkliuku kaina su akcijomis: {total_akcijos_kaina} Eur")

with open("saskaita.txt", "w", encoding="utf-8") as w:
    print(f"visu zenkliuku kiekis: {total_zenkliukai}", file=w)
    print(f"visu zenkliuku kaina be akciju: {total_zenkliukai * 5} Eur", file=w)
    print(f"visu zenkliuku kaina su akcijomis: {total_akcijos_kaina} Eur", file=w)
    for name, i in mokiniu_vardai_kainos.items():
        print(f"\n{name} zenkliuku kaina: {i} Eur", file=w)

with open("sarasas.txt", "w", encoding='utf-8') as w:
    print(dupes, file=w)
