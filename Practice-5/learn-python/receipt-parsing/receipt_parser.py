import re
f = open("raw.txt", "rt", encoding="utf-8")
text = f.read()

patternNamePrice = r"\d+\.\n(?P<Name>.*)\n.*\n.*\n.*Стоимость\n(?P<Price>\d+.*)"
print(re.findall(patternNamePrice, text))

f.close()