"""
print("Darvozani qirrasini (🅿) yuzasini (🕳) ni hisoblash dastur tuzing. ")

print(f"Darvozani eni 4 metr bo'yi 3 metrga teng ")
a=4
b=3
print(f"Darvozani yuzasi  S={a*b} ga teng ")
print(f"Darvozani premetri P={a+b} ga teng")
"""


"""
print("Darvozani qirrasini (🅿) yuzasini (🕳) ni hisoblash dastur tuzing. Qiymatlar foydalanuvchi tomonidan kritilsin ")

a=(float(input("Darvozani bo'yini ⬆ kriting.\n")))
b=(float(input("Darvozani enini ⬅➡ kriting.\n")))
print(f"Darvozani yuzasi  S={a*b} ga teng ")
print(f"Darvozani premetri P={a+b} ga teng")
"""
"""

print("Quydagi o'zgaruchilarni turini aniqlang)
alfa = 8764
beta = "lola"
print(alfa,type(alfa))
print(beta,type(beta))
  """

"""

alfa = 8764345
beta = "aqlbek"
d=True
s=0
resp="d"
b=100
max=False
fs="true34"
t=102,5
res="2500"
a='-50'
b=45,67
g=4j
print(alfa,type(alfa))
print(beta,type(beta))

print(d,type(d))
print(s,type(s))
print(resp,type(resp))
print(b,type(b))
print(max,type(max))
print(fs,type(fs))
print(t,type(t))
print(a,type(a))
print(b,type(b))
print(g,type(g))
"""
"""

a=(int(input("1-qayq tezligini kriting. =>>> ")))
b=(int(input("2-qayq tezligini kriting. =>>> ")))
print(f"Ikkita qayiq turg'un suvda bir biriga tomon {a} km/soat va {b} km/soat tezlik bilan suzmoqda Ular orasidagi masofa 24 km bo'lsa,
1-savol: Ular qancha vaqtdan keyin uchrashadi? 
2-savol: Qancha vaqtdan keyin ular orasidagi masofa 12 km ni tashkil qiladi?")
#t=(a+b)/24
#t2=(a+b)/12
print(f"1-savolga javob: Ular {(a+b)/24} vaqtda uchrashadi")
print(f"2-savolga javob: Ular orasidagi masofa 12 km ni tashkil etsa ular  {(a+b)/12} va+qtda uchrashad")
"""
"""

a=float(input("Darvozani bo'yini kriting.\n"))
b=float(input("Darvozani enini kriting.\n"))
print(f"Darvozani yuzasi S={a*b} kvga teng ")
print(f"Darvozani peremetri P={a+b} metrga teng ")
"""

"""

print("Uchburchak asosining uzunligi 'c' va balandligini 'h' foydalanuvchi tomonidan kritiladi. Uchburchakni yuzasi 'S'ni hisiblash dastur tuzing ")
c=float(input("Uchburchak asosining uzunligini kriting.>>>"))
h=float(input("Uchburchaknin bo'yini kritin"))
print(f"Uchburchakni yuzasi S={c*h/2} ga teng. ")
"""

"""

print("Avtomobilni o'rtacha tezligi 'v' km/saot va bosib o'tgan yo'li s 'km'\
 foydalanuvchi tomonidan kritiladi. Avtomobilni yurgan vaqtini 't' aniqlovchi dastur tuzing.\n")
v=float(input("Avtomobilni o'rtacha tezligini kriting.\n"))
s=float(input("Avtomobilni bosib o'tgan yo'lni kriting.\n"))
print(f"Avtomobilni yurgan vaqti t={s/v} saot yurgan")
"""
"""
print("Doirani radiusi 'r'ga teng. Doirani yuzasi 's' va aylanani uzunligi 'l' ni topish dasturini tuzing.")

r=float(input("Doirani radiusini kriting. R="))
s=float(input("Doirani yuzasini kriting. S="))
pi=3.14
print(f"Doirani uzunligi L={2*pi*r} ga teng")
"""

"""
x=float(input(" 'x' qiymat kiriting."))     
y=float(input(" 'y' qiymat kiriting."))
a=x+2*y+5**2*4-58
print(f"x={x}\
       y={y}\
          x+2*y+5**2*4-58=\
  {x}+2*{y}+5**2*4-58={a}")     
"""

"""
a=256+(2589-1549)*458+456**14-4565/5
print(a)
"""


#print(" Berilgan ikki honali son honalarining yig'indisi va ko'paytmasini hisoblash dastur tuzing")
def son(hona):
    s=0
    for x in hona:
        if x.isdigit()==True:
           z=int(x)
           s=s+z
    return s
print(son("133"))

"""
x=float(input("x="))
print(f"y= 7/(x*2+x+1)+x*2={7/(x*2+x+1)+x*2}")
"""
