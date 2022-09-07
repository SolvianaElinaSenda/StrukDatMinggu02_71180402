import time

# Fungsi Iteratif


def fungsi_iteratif(n):
    n = i
    for i in range(6, 101):
        print(i)


start = time.time()
hasil = fungsi_iteratif(100)
end = time.time()
hasilTime = end-start

# print(n)


# Fungsi Rekursif
def fungsi_rekursif(n):
    if n < 5:
        return 0
    else:
        return fungsi_rekursif(n+1)


hasil1 = fungsi_iteratif(100)
print("Fungsi Iteratifnya adalah: ", hasil1)
print(hasilTime)

hasil2 = fungsi_rekursif(100)
print("Fungsi Rekursifnya adalah: ", hasil2)
print(hasilTime)
