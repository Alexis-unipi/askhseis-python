import json
fl = open('text.txt', 'r')
x = fl.readline()
y = json.loads(x)
kleidia = y.keys()
lista1 = list(kleidia)
print(lista1)
kleidi = input("Δωστε ενα κλειδι τα παραπανω :")
d = []
with open('text.txt', 'r') as z:
    for i in z:
        d.append(eval(i))

times = [onoma[kleidi]for onoma in d]
lista2 = times
megisto = max(lista2)
elaxisto = min(lista2)
print(megisto)
print(elaxisto)


def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num



print(most_frequent('text.txt'))