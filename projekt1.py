import sys
'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tibor Nešpor
email: tibornespor97@gmail.com
discord: theebone
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# jména a hesla uživatelů + kontrola
print("Registrováni jsou nasledujíci uživatelé")
print("""+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+""")
registrovani = {"bob" : "123","ann" : "pass123","mike" : "password123","liz" : "pass123"}
jmeno = input("Zadejte vaše jméno: ").lower()
heslo = input("Zadejte vaše heslo: ").lower()
if registrovani.get(jmeno) == heslo:
    print(f"Ahoj, {jmeno} vítej v programu na analyzování textů")
else:
    print("Nesprávné jméno nebo heslo, ukončuji program.")
    sys.exit()

# výběr textu + kontrola
print("-" * 64)
volba_textu = input("Vyberte prosím číslo textu který chcete analyzovat v rozmezí 1 až 3: ")
print("-" * 64)
if volba_textu.isdigit():
    vyber_textu = int(volba_textu) - 1
    if 0 <= vyber_textu < len(TEXTS):
        print(f"Vybrali jste text číslo {volba_textu} ")
    else:
        print("Zadané číslo není v rozmezí 1 až 3.Program bude ukončen")
        sys.exit()
else:
    print("Zadali jste neplatný vstup (musí to být číslo) Program bude ukončen")
    sys.exit()
# Statistika slov a cisel
pocet_slov = len(TEXTS[vyber_textu].split())
slova_s_velkym = [velke for velke in TEXTS[vyber_textu].split() 
if velke.startswith(tuple("QWERTZUIOPASDFGHJKLYXCVBNM"))]

slova_cele_velkym = [cele_velke for cele_velke in TEXTS[vyber_textu].split() if
 cele_velke.isupper() and not cele_velke.startswith(tuple("1234567890"))]

slova_s_malym = [male for male in TEXTS[vyber_textu].split()
if male.islower()]


pocet_cisel = [cisla for cisla in TEXTS[vyber_textu].split() if 
cisla.isnumeric()]

pocet_cisel = [int(cislo) for cislo in pocet_cisel]
soucet = sum(pocet_cisel)
#Graf reprezentující četnost textu
slova = TEXTS[vyber_textu].split()
cetnost_delek = {}
for slovo in slova:
    slovo = slovo.strip(".,!?")
    delka_slova = len(slovo)
    if delka_slova in cetnost_delek:
        cetnost_delek[delka_slova] += 1
    else:
        cetnost_delek[delka_slova] = 1




print(f"V textu je {pocet_slov} slov.")
print(f"V textu je {len(slova_s_velkym)} začínajících velkým písmenem.")
print(f"V textu je {len(slova_cele_velkym)} slov napsáno kompletně velkým písmenem.")
print(f"V textu je {len(slova_s_malym)} slov napsáno malými písmeny.")
print(f"V textu jsou {len(pocet_cisel)} čísla.")
print(f"Součet všech čísel v textu je {soucet}.")
print("-" *64 )
print("LEN|  OCCURENCES  |NR.")
print("-" *64)

for delka, pocet in sorted(cetnost_delek.items()):
    hvezdicky = "*" * pocet
    print(f"{delka:>3}|{hvezdicky:<14}|{pocet}")
