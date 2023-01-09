import os
os.system('cls')

def mergesort(ar): 
    if len(ar) <= 1:
        return ar

    mid = len(ar) // 2 
    left = ar[:mid]
    right = ar[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge (left,right)

def merge(left, right):
    result = [] 

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    elif right:
        result += right
    return result

listacak =  [12, 1, [22, 3, [8, 14]], 2, 6, [11], 90]
lista =  listacak[0:2] 
lista1 = listacak[3:5]
listb1 = listacak[6:7]
listb = listacak[2][0:2]
listc = listacak[2][2][0:2]
listd = listacak[5]

listterurut = lista+lista1+listb1+listb+listc+listd
hasil = mergesort(listterurut)

print("sebelum terurut :",listacak)
print("sesudah terurut :",hasil)