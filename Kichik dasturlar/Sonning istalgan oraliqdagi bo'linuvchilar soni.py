#biron bir oraliqdagi bo'linuvchilar soni
son=int(input('Istalgan butun son kiriting:\n'))
oraliqning_birinchi_soni=int(input('Oraliqning birinchi sonini kiriting\n'))
oraliqning_ikkinchi_soni=int(input('Oraliqning ikkinchi sonini kiriting\n'))
bolinuvchilar_soni=[]
for bolinuvchi in range(oraliqning_birinchi_soni,oraliqning_ikkinchi_soni+1):
      if son%bolinuvchi==0:
           bolinuvchilar_soni.append(bolinuvchi)
           print(f'{son} soni {bolinuvchi}ga bolinadi')
print(son,'soni','(',oraliqning_birinchi_soni,':',oraliqning_ikkinchi_soni,')','oralig\'ida',len(bolinuvchilar_soni),'ta songa qoldiqsiz bo\'linadi')