# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
# Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. 
# Örnek olarak:
#input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# output: [1,'a','cat',2,3,'dog',4,5]

#ÇÖZÜM :

liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
new_liste = []
def flatten(n):
    for i in n:
        if isinstance(i, liste):
            flatten(i)
        else:
            new_liste.append(i)

flatten(liste)
print(new_liste)




# 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
# Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. 
# Örnek olarak:
# input: [[1, 2], [3, 4], [5, 6, 7]]
# output: [[[7, 6, 5], [4, 3], [2, 1]]

# ÇÖZÜM :

list =[[1, 2], [3, 4], [5, 6, 7]]
list=list[::-1]

for i in range(len(list)):
    (list[i])=(list[i])[::-1]
print(list)
