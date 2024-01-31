#tarmoqlanuchi opertor if, elif, else.
# and VA or YOKI
"""
kun = input("Haftaning qaysi kuni? ")
harorat = float(input("Havo haroratini qanday?  "))
if kun.lower()=="yakshanba" and harorat>=32:
    print("Cho'milgani ketdik")
elif kun.lower()=="shanba" or harorat>=18:
    print("Choyhonaga boramiz")
else:
    print("Uyda dam olamiz.")
"""

#bool malumot turlari
"""

meva=["nok",'olma','uzum','gilos']
b = 'olma' in meva #bool bu bor yoki yuqligini aytadi
print(b)
"""

"""
narx=15000
choy=True
salat=False
if choy and salat:
    narx+=10000
elif choy or salat:
    narx+=5000
else:
    pass 
print(f"Jami {narx} so'm bo'ldi")
"""
"""
#shartlarni ketma ket tekshirish
narx=15000
choy=True
salat=bool(input("salat olasizmi\n"))
non=True
kampot=True
assart=False
if choy:
    print("Mijoz choy oldi ")
    narx+=3000
    if salat:
        print("Mijoz salat oldi")
        narx+=4000
    if non:
        print("Mjoz non oldi")
        narx+=2500
    if kampot:
        print("Mijoz kamport oldi")
        narx+=6500
    if assart:
        print("Mijoz kampot oldi")
        narx+=15000
print(f"Jami {narx} so'm")
"""

"""
menu = ['osh','shashlik','bosma','manti','jizz','norin']
ovqat = input("Nima ovqat yeysiz?\n") 
if ovqat.lower() not in menu:
    print("Afsuski bizda tugab qolgan")
else:
    print("Buyurtmangiz tez orada yetkazizb beriladi")
"""
"""
u = ['osh','shashlik','bosma','manti','jizz','norin']
byurtmalar = ['osh','chuchvara','goshkuyda','shashlik','bosma','manti','jizz','norin']
if byurtmalar:
    for taom in byurtmalar:
        if taom in menu:
            print(f"Bizda {taom} bor.")
        else:
            print(f"Bizda  {taom} tugab qoldi.")
"""



