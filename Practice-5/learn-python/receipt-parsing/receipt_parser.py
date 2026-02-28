import re
import json
f = open("raw.txt", "rt", encoding="utf-8")
text = f.read()

patternNamePrice = r"\d+\.\n(?P<Name>.*)\n.*\n.*\n.*Стоимость\n(?P<Price>\d+.*)"
p1 = re.findall(patternNamePrice, text)

sum = 0
for i in range(len(p1)):
    sum += float(p1[i][1].replace(",", ".").replace(" ", ""))

patternDateTime = r"(?<=Время: )\d+.*"
p2 = re.findall(patternDateTime, text)

patternPaymentMethod = r"Банковская карта"
p3 = re.findall(patternPaymentMethod, text)

paymentMethod = ""
if bool(p3[0].lower().find("банк")+1) and bool(p3[0].lower().find("карта")+1):
    paymentMethod = "Payed by bank card"
else:
    paymentMethod = "Payed by cash"

x = {
    "namePrice": p1,
    "sum": round(sum),
    "time": p2[0],
    "paymentMethod": paymentMethod 
}

print(json.dumps(x, indent=4))

f.close()