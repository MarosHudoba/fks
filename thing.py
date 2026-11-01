
import json

with open("PeriodicTableJSON.json", "r", encoding='utf-8') as f:
    pte = json.load(f)

#print(pte['elements'])

sumMx21 = 0
sumMy21 = 0

sumMx1 = 0
sumMy1 = 0

sumMx22 = 0
sumMy22 = 0

sumMx2 = 0
sumMy2 = 0

sumMx23 = 0
sumMy23 = 0

sumMx3 = 0
sumMy3 = 0

sumMx24 = 0
sumMy24 = 0

sumMx4 = 0
sumMy4 = 0

for el in pte['elements']:

    #         Pre lavny dolny roh          

    sumMx21 += ((el['wxpos'] - 0.5) ** 2 )* el['number']
    sumMy21 += ((7.5 - el['wypos']) ** 2 )* el['number']

    sumMx1 += (el['wxpos'] - 0.5) * el['number']
    sumMy1 += (7.5 - el['wypos']) * el['number']

    #         Pre lavny horny roh          

    sumMx22 += ((el['wxpos'] - 0.5) ** 2 )* el['number']
    sumMy22 += ((el['wypos'] - 0.5) ** 2 )* el['number']

    sumMx2 += (el['wxpos'] - 0.5) * el['number']
    sumMy2 += (el['wypos'] - 0.5) * el['number']

    #        Pre pravy horny roh

    sumMx23 += ((32.5 - el['wxpos']) ** 2 )* el['number']
    sumMy23 += ((el['wypos'] - 0.5) ** 2 )* el['number']

    sumMx3 += (32.5 - el['wxpos']) * el['number']
    sumMy3 += (el['wypos'] - 0.5) * el['number']   

    #         Pre pravy dolny roh          

    sumMx24 += ((32.5 - el['wxpos']) ** 2 )* el['number']
    sumMy24 += ((7.5 - el['wypos']) ** 2 )* el['number']

    sumMx4 += (32.5 - el['wxpos']) * el['number']
    sumMy4 += (7.5 - el['wypos']) * el['number']

print("Pre lavny dolny roh: ", sumMx21 + sumMy21)
print("Pre lavny horny roh: ", sumMx22 + sumMy22)
print("Pre pravy horny roh: ", sumMx23 + sumMy23)
print("Pre pravy dolny roh: ", sumMx24 + sumMy24)

print()

print("Pre lavny dolny roh: ", sumMx1,sumMy1)