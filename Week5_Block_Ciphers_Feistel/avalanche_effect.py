def encrypt(data):
    keys = [3,5,7,9]

    for k in keys:
        data ^= k

    return data

p1 = 100
p2 = 101

c1 = encrypt(p1)
c2 = encrypt(p2)

print("Ciphertext 1:", c1)
print("Ciphertext 2:", c2)