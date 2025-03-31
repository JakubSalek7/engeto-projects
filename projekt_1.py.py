"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jakub Salek
email: jakub.n.salek@gmail.com
discord: zob3772
"""

import sys

# Předpřipravené texty
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

# Registrovaní uživatelé
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# Přihlášení uživatele
username = input("username:")
password = input("password:")

if users.get(username) != password:
    print("unregistered user, terminating the program..")
    sys.exit()

print(f"Welcome to the app, {username}")
print("We have 3 texts to be analyzed.")
print("-" * 40)

# Výběr textu
try:
    choice = int(input("Enter a number btw. 1 and 3 to select: "))
    if choice not in [1, 2, 3]:
        raise ValueError
except ValueError:
    print("Invalid input, terminating the program..")
    sys.exit()

selected_text = TEXTS[choice - 1]

# Analýza textu
words = selected_text.split()
titlecase_words = [word for word in words if word.istitle()]
uppercase_words = [word for word in words if word.isupper() and word.isalpha()]
lowercase_words = [word for word in words if word.islower()]
numeric_strings = [int(word) for word in words if word.isdigit()]

print("-" * 40)
print(f"There are {len(words)} words in the selected text.")
print(f"There are {len(titlecase_words)} titlecase words.")
print(f"There are {len(uppercase_words)} uppercase words.")
print(f"There are {len(lowercase_words)} lowercase words.")
print(f"There are {len(numeric_strings)} numeric strings.")
print(f"The sum of all the numbers {sum(numeric_strings)}")
print("-" * 40)

# Sloupcový graf četnosti délek slov
word_lengths = {}
for word in words:
    length = len(word.strip(".,!?"))
    word_lengths[length] = word_lengths.get(length, 0) + 1

print("LEN|  OCCURENCES  |NR.")
print("-" * 40)
for length, count in sorted(word_lengths.items()):
    print(f"{length:2}| {'*' * count:<12} |{count}")
