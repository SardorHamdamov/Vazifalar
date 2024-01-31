"""
print("Foydalanuchidan juf son kritishni so'rang agar foydalanuvchi juft son krtisa Rahmat! deb chiqarsin agar toq son chiqarsa bu son juf son emas desin")
juft_son=int(input("Juft son kriting\n>>>"))
print(juft_son)
if juft_son%2==0:
    print("Rahmat!")
else:
    print("Bu juft son emas")
"""

"""
print("Foydalanucvchidan yoshini so'rang va muzeyga kirish un chiptaa narxi quydagicha chiqaring")
yow = int(input("Yoshingizni kriting.\n->"))
if 4>=yow or yow>=60:
    print("Sizga krish bepul.")
elif 18>=yow:
    print("Sizga krish 10000 so'm.")
elif 18<=yow:
    print("Sizga krish 20000 so'm.")
else:
    pass
"""

"""
print("Foydalanuvchidan ikkita sn kritishni so'rang so'ng sonlarni solishtring teng yoki kata kichikligini taqqoslang ")
a=float(input("Birinchi sondi kriting. "))
b=float(input("ikkinchi sondi kriting. "))
if a>b:
    print(f"{a} soni {b} sonidan kotta. Natija: {a} > {b}")
elif a==b:
    print(f"{a} soni {b} soniga teng. Natija: {a} = {b}")
else:
    print(f"{a} soni {b} sonidan kichik. Natija: {a} < {b}"
"""




mahsulotlar=['alicha','uzum',"olma","qovun","o'rik","gilos",'nok','behi','qulpinay']
print(f"Sizga qanday mahsulotlar kerak {mahsulotlar}")
savat = []
for x in range(1,6):
    savat.append(input(f"Savatga {x}-mahsulotni qo'shing: "))
print(savat)

if savat:
    for meva in savat:
        if meva in mahsulotlar:
            print(f"Bizda {meva} bor. ")
        else:
            print(f"Bizda  {meva} tugab qoldi. ")

"""
print("5 ta mahsulot kriting.")
mahsulot = []
for son in range(1,5):
    mahsulot.appen(input(f"{son}-mahsulotni kriting: "))
"""