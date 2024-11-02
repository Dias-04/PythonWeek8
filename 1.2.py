char_count_list = [('p', 2), ('u', 1), ('l', 1), (' ', 1), ('f', 1), ('i', 2), ('c', 1), ('t', 1), ('o', 1), ('n', 1)]

list_vow = []
list_cons = []
list_sym = []

vowels = {'a', 'e', 'i', 'o', 'u'}
symbols = {' '}

for char, count in char_count_list:
    if char in vowels:
        list_vow.append((char, count))
    elif char in symbols:
        list_sym.append((char, count))
    else:
        list_cons.append((char, count))

print("list_vow =", list_vow)
print("list_cons =", list_cons)
print("list_sym =", list_sym)
