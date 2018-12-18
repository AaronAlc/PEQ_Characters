import re

string = "Slot: ARMS HEAD BACK LEGS</br>"
s2 = "STR: 15 STA: 20 \nHP: +300 MANA: +270"

#regex = "Slot:(.+)<"
regex = "STR: \+?([0-9]+)"

match = re.search(regex, s2)

if match is not None:
    print (match.group(1))

