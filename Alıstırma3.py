######################################
#      UYGULAMA MÜLAKAT SORUSU       #
######################################


# Amaç : Çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir.
# key'ler orijinal değerler, value'lar ise değiştirilmiş değerler olacak.

numbers = range(10)
new_dict = {}

for number in numbers:
    if number % 2 == 0:
        new_dict[number] = number ** 2
   print(new_dict)  
  
# Ekran Çıktısı : {0: 0, 2: 4, 4: 16, 6: 36, 8: 64, 9: 81}


# 2.YOL:
{number: number ** 2 for number in numbers if number % 2 == 0}

# Ekran Çıktısı : {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
