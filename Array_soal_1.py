import numpy as np

def get_max (an_array):
    big = -1
    for x in an_array:
        if x > big:
            big = x
    return big

def get_min (an_array):
    small = 101
    for x in an_array:
        if x < small:
            small = x
    return small

my_array = np.array([])
print("\nMasukan nilai dari 1-100 jika melebihi dari batas program akan berhenti\n")
a = int (input("masukan angka ke-1 = "))
count = 1
while 0 < a < 101:
    count += 1
    my_array = np.append(my_array, a)
    a = int (input(f"masukan angka ke-{count} = "))

big_number = get_max(my_array)
small_number = get_min(my_array)

print(f"big number in your array is = {big_number}")
print(f"small number in your array is = {small_number}")