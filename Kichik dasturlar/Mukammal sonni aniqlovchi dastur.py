#mukammal sonni aniqlovchi dastur
son=int(input("istalgan butun sonni kiriting"))
bolinuvchilar=[]
for bolinuvchi in range(1,son):
    if not son%bolinuvchi:
        bolinuvchilar.append(bolinuvchi)
if sum(bolinuvchilar)==son:
    print(f'{son} mukammal son')
else:
    print(f'{son} mukammal son emas')