cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
  if car == 'gm':
    print(car.upper())
  else:
    print(car.title())


cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
  if car != 'gm':
    print(car.title())
  else:
    print(car.upper())


name = input("Ismingizni kiritish>>>")
if name.lower() == 'admin':
  print(f"Xush kelibsiz, {name.title()}. Foydalanuvchilar ro'yxatini ko'rasizmi")
else:
  print(f"Xush kelibsiz, {name.title()}")
