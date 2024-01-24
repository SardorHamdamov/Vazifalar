
davlatlar=["Uzbekistan","Yevropa","Russiya","Amerika","Koreya"]
print(davlatlar)

print(f"Man bilgan davlatlar soni {len(davlatlar)} ta va ular {davlatlar} shular tashkil etadi")

#davlatlar sorted() orqali tartib bilan yozish
print(f"Tartib bilan yozganimizda {sorted(davlatlar)} shunday ko'rinishda bo'ladi")

davlatlar.sort(reverse=True)
print(f"Tartib bilan teskari yani orqasidan yozganimizda {davlatlar} shunday ko'rinishda bo'ladi")

davlatlar=["Uzbekistan","Yevropa","Russiya","Amerika","Koreya"]
print(davlatlar[::-1])


juft_sonlar=list(range(0,1201,2))
print(juft_sonlar)

print(f"Juft sonlar yrg'indisi {sum(juft_sonlar)}")

juft_sonlar_m=max(juft_sonlar)
juft_sonlar_k=min(juft_sonlar)
ayirmasi=(juft_sonlar_m)-(juft_sonlar_k)
print(f"Eng  kotta va eng kichik sonlar o'rtasida ayirmasi {ayirmasi} ga teng")

print(f"Elementlar soni {len(juft_sonlar)}")


juft_sonlar=list(range(120,1201,2))
print(f" Juft sonlar boshidan {juft_sonlar[:20]}  ta tashkil qiladi")
print(f" Juft sonlar o'rtasidan  {juft_sonlar[-20:]}  ta tashkil qiladi")
print(f" Juft sonlar oxiridan {juft_sonlar[530:550]}  ta tashkil qiladi")

Taomlar=["Osh","Somsa","Shashlik","Tuhum","Manti"]
nonushta=Taomlar
print(nonushta)
nonushta=[Taomlar[3]]
nonushta.append("Qaymoq")
nonushta.append("Issiq non")
print(nonushta)

print(Taomlar)
ozgarmas=tuple(nonushta)
print(ozgarmas)


