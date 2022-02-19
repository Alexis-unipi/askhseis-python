arxeio = open('file.txt')
d = (arxeio.read())
d = str(d)
listab1 = []
bytear1 = bytearray(d, "utf8")
for byte in bytear1:
    duadiko = bin(byte)
    listab1.append(duadiko[2:])
Lista1 = []
Lista2 = []
for item in listab1:
    l1 = list(item)
    if len(l1) < 7:
        l1.insert(0, '0')
    meg1 = 0
    meg2 = 0
    s1 = 0
    s2 = 0
    for bit in l1:
        if bit == '0':
            s2 = s2+1
            s1 = 0
            if meg2 < s2:
                meg2 = s2
        else:
            s1 = s1 + 1
            s2 = 0
            if meg1 < s1:
                meg1 = s1
        Lista1.append(meg1)
        Lista2.append(meg2)
M1 = max(Lista1)
M2 = max(Lista2)
print(M1)
print(M2)
