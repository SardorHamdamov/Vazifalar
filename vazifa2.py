ismlar=["Abror","Murod","Sodiqjon"]
print(f"""Salom {ismlar[0]}, bugun choyxona bormi?
{ismlar[1]}, choyxonaga boramizmi?
{ismlar[2]} o'qishga borasizmi?""")

print("royhatlarga son qoshish")
sonlar=["2","-23","34.5","10"]
print(sonlar)
sonlar.append(98)
sonlar.insert(3,"22")
sonlar.pop(2)
print(sonlar)

print("royhat ichidan sug'rib olish")
t_shaxslar=["Bobur","Temur","Alisher Navoiy","Imom Buxoriy"]
z_shaxslar=["Bill Gates","Jaloliddin Ahmadaliyev","Doston Ergashev","Shohruhhon"]
print(f"Men tarixiy shaxslardan {t_shaxslar[3]} bilan, zamonaviy shaxslardan esa {z_shaxslar[0]} bilan suhbat qilishni istar edim")

print("bosh royhatga yangi ro'yhat qoshish")
friends=[]
friends.append("Sodiqjon") #qo'shadi
friends.append("Qodir")
friends.append("Botir")
friends.append("Muhammadjon")
friends.append("Fazliddin")
friends.append("Marif")
print(friends)

print("orasidan o'chiradi")
friends.remove("Sodiqjon") #o'chiradi
friends.remove("Botir")
print(friends)

print("orasiga qoshish dasturi")
friends.insert(0,"Shukur")
friends.insert(10,"Doston")
friends.insert(2,"Halim")
print(friends)

print('yangi_mehmonlar')
yangi_mehmonlar=[friends[0],friends[1],friends[2],friends[3],friends[4],friends[5],friends[6]]
print(yangi_mehmonlar)




