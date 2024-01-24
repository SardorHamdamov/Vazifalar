"""
dostlar=["Ali","Vali","Hasan","Husan","Olim"]
print("Kamida 5 ta do'stingizni ro'yhatini kriting")
for x in dostlar:
    print(f"salom {x}" )
print(f"Kod  {len(dostlar)} martda takrorlandi")

print("10 dan 100gacha bo'lgan toq sonlar va ularni yegindisi")
toq_sonlar=list(range(11,101,2))
print(toq_sonlar)

for x in range(11,101,2):
    print(f"{x} ning kubi {x**3}")

print("Foydalanuvchidan 5ta rng sevimli kinosi kritishni so'raydi va kinolar degan ro'yhatni konsulga chiqaradigon dastur.")
kinolar=[]
for n in range(1,6):
     kinolar.append(input(f"{n}-kino"))
print(kinolar)
"""


suhbat=int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
print(suhbat,"ta shubatchini ismlarini kiriting.")
ism=[]
for x in range(suhbat):
    ism.append(input(f"{x+1}-suhbatchini ismini kriting:>>>"))
print(f"Siz suhbat qilgan insonlarni ismlar {ism}")


