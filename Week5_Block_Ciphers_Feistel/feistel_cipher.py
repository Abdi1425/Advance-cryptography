def feistel_round(left, right, key):
    return right, left ^ (right ^ key)

left = 15
right = 7

keys = [3,5,7,9]

for key in keys:
    left, right = feistel_round(left, right, key)

print("Ciphertext:", left, right)