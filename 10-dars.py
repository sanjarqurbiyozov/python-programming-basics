# IF operatori
avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
for avto in avtolar:              # avtolar ichidagi har bir avto uchun ...
  if avto == 'bmw':               # ... agar avto bmw ga teng bolsa ...
    print(avto.upper())           # avto nomi hamma harflari katta bilan yoz.
  else:   # aks holda ...
    print(avto.title())   # avto nomini birinchi harfini katta harfda yoz.



# Qiymatlarning teng emasligini tekshrish. Checking for inequality of values.
name = input('Ismingiz nima? \n>>>') # Foydalanuvchidan ismini soraymiz.
if name.lower() != 'ali':            # Agar ism ali ga teng bolmasa ...
  print(f"Uzr, {name.title()} biz Alini kutyabmiz.") # quyidagi habar chiqadi
else:
  print("Salom, Ali!")
