
import numpy as np

def mean (data):
    total = 0
    jmlh = 0
    for x in data :
        total += x
        jmlh += 1
    return total/jmlh

counting = 0
n = int(input("Masukan Banyak Bebek = "))
scores = np.array([])

while counting != n:
    counting +=1
    score = int(input(f"Masukan nilai bebek ke {counting}  = "))
    scores = np.append (scores, score)
    
mean_bebek = mean(scores)
bebek = 0
lulus = 0
gagal = 0
print("\npengumuman nilai kelulusan bebek!\n")
for x in scores:
    bebek += 1
    if x > mean_bebek:
        print(f"selamat bebek {bebek} lulus!")
        lulus += 1
    else:
        print(f"maaf ya bebek {bebek} kamu kurang beruntung :(")
        gagal += 1
print(f"\ntotal bebek yang lulus adalah = {lulus}\nyang gagal sebanyak = {gagal}")
print("MANTAPP")
