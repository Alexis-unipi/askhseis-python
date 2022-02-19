sum = 0

for a in range(100):
    from random import randint

    w = 0
    vhmata = 0
    tetr = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    while True:
        vhmata = vhmata + 1
        while True:
            x = randint(1, 3)
            y = randint(1, 3)
            megethos = randint(1, 3)

            if megethos == 1:
                if tetr[x - 1][y - 1] == 1 or tetr[x - 1][y - 1] == 4 or tetr[x - 1][y - 1] == 6 or tetr[x - 1][
                    y - 1] == 9:
                    print("Εχει ειδη μπει μικρος δακτυλιος σε αυτη τη θεση,δοκιμαστε αλλη θεση")
                else:
                    tetr[x - 1][y - 1] = tetr[x - 1][y - 1] + 1
                    break
            if megethos == 2:
                if tetr[x - 1][y - 1] == 3 or tetr[x - 1][y - 1] == 4 or tetr[x - 1][y - 1] == 8 or tetr[x - 1][
                    y - 1] == 9:
                    print("Εχει ειδη μπει μεσαιος δακτυλιος σε αυτη τη θεση,δοκιμαστε αλλη θεση")
                else:
                    tetr[x - 1][y - 1] = tetr[x - 1][y - 1] + 3
                    break
            if megethos == 3:
                if tetr[x - 1][y - 1] == 5 or tetr[x - 1][y - 1] == 8 or tetr[x - 1][y - 1] == 6 or tetr[x - 1][
                    y - 1] == 9:
                    print("Εχει ειδη μπει μεγαλος δακτυλιος σε αυτη τη θεση,δοκιμαστε αλλη θεση")
                else:
                    tetr[x - 1][y - 1] = tetr[x - 1][y - 1] + 5
                    break

        for row in tetr:
            print(row)

        for i in range(3):
            pl = 0
            for j in range(3):
                if tetr[i][j] == 1 or tetr[i][j] == 4 or tetr[i][j] == 6 or tetr[i][j] == 9:
                    pl = pl + 1
        if pl == 3:
            print("κερδισατε με μικρους δαλτυλιους οριζοντια στην σειρα:", i + 1)
            w = w + 1
            break
        else:
            pl = 0
        for i in range(3):
            pl = 0
            for j in range(3):
                if tetr[i][j] == 3 or tetr[i][j] == 4 or tetr[i][j] == 8 or tetr[i][j] == 9:
                    pl = pl + 1

            if pl == 3:
                print("κερδισατε με μεσαιους δαλτυλιους οριζοντια στην σειρα:", i + 1)
                w = w + 1
                break
            else:
                pl = 0

        for i in range(3):
            pl = 0
            for j in range(3):
                if tetr[i][j] == 5 or tetr[i][j] == 8 or tetr[i][j] == 6 or tetr[i][j] == 9:
                    pl = pl + 1

            if pl == 3:
                print("κερδισατε με μεγαλους δαλτυλιους οριζοντια στην σειρα:", i + 1)
                w = w + 1
                break
            else:
                pl = 0

        for j in range(3):
            pl = 0
            for i in range(3):
                if tetr[i][j] == 1 or tetr[i][j] == 4 or tetr[i][j] == 6 or tetr[i][j] == 9:
                    pl = pl + 1

            if pl == 3:
                print("κερδισατε με μικρους δαλτυλιους καθετα στην στηλη:", j + 1)
                w = w + 1
                break
            else:
                pl = 0

        for j in range(3):
            pl = 0
            for i in range(3):
                if tetr[i][j] == 3 or tetr[i][j] == 4 or tetr[i][j] == 8 or tetr[i][j] == 9:
                    pl = pl + 1

            if pl == 3:
                print("κερδισατε με μεσαιους δαλτυλιους καθετα στην στηλη:", j + 1)
                w = w + 1
                break
            else:
                pl = 0

        for j in range(3):
            pl = 0
            for i in range(3):
                if tetr[i][j] == 5 or tetr[i][j] == 8 or tetr[i][j] == 6 or tetr[i][j] == 9:
                    pl = pl + 1

            if pl == 3:
                print("κερδισατε με μεγαλους δαλτυλιους καθετα στην στηλη:", j + 1)
                w = w + 1
                break
            else:
                pl = 0

        if tetr[0][0] == 1 or tetr[0][0] == 4 or tetr[0][0] == 6 or tetr[0][0] == 9:
            if tetr[1][1] == 1 or tetr[1][1] == 4 or tetr[1][1] == 6 or tetr[1][1] == 9:
                if tetr[2][2] == 1 or tetr[2][2] == 4 or tetr[2][2] == 6 or tetr[2][2] == 9:
                    print("κερδισατε με μικρους δαλτυλιους διαγωνια απο αριστερα")
                    w = w + 1

        if tetr[0][0] == 3 or tetr[0][0] == 4 or tetr[0][0] == 8 or tetr[0][0] == 9:
            if tetr[1][1] == 3 or tetr[1][1] == 4 or tetr[1][1] == 8 or tetr[1][1] == 9:
                if tetr[2][2] == 3 or tetr[2][2] == 4 or tetr[2][2] == 8 or tetr[2][2] == 9:
                    print("κερδισατε με μεσαιους δαλτυλιους διαγωνια απο αριστερα")
                    w = w + 1

        if tetr[0][0] == 5 or tetr[0][0] == 6 or tetr[0][0] == 8 or tetr[0][0] == 9:
            if tetr[1][1] == 5 or tetr[1][1] == 6 or tetr[1][1] == 8 or tetr[1][1] == 9:
                if tetr[2][2] == 5 or tetr[2][2] == 6 or tetr[2][2] == 8 or tetr[2][2] == 9:
                    print("κερδισατε με μεγαλους δαλτυλιους διαγωνια απο αριστερα")
                    w = w + 1

        if tetr[0][2] == 1 or tetr[0][2] == 4 or tetr[0][2] == 6 or tetr[0][2] == 9:
            if tetr[1][1] == 1 or tetr[1][1] == 4 or tetr[1][1] == 6 or tetr[1][1] == 9:
                if tetr[2][0] == 1 or tetr[2][0] == 4 or tetr[2][2] == 6 or tetr[2][0] == 9:
                    print("κερδισατε με μικρους δαλτυλιους διαγωνια απο δεξια")
                    w = w + 1

        if tetr[0][2] == 3 or tetr[0][2] == 4 or tetr[0][2] == 8 or tetr[0][2] == 9:
            if tetr[1][1] == 3 or tetr[1][1] == 4 or tetr[1][1] == 8 or tetr[1][1] == 9:
                if tetr[2][0] == 3 or tetr[2][0] == 4 or tetr[2][0] == 8 or tetr[2][0] == 9:
                    print("κερδισατε με μεσαιους δαλτυλιους διαγωνια απο δεξια")
                    w = w + 1

        if tetr[0][2] == 5 or tetr[0][2] == 6 or tetr[0][2] == 8 or tetr[0][2] == 9:
            if tetr[1][1] == 5 or tetr[1][1] == 6 or tetr[1][1] == 8 or tetr[1][1] == 9:
                if tetr[2][0] == 5 or tetr[2][0] == 6 or tetr[2][0] == 8 or tetr[2][0] == 9:
                    print("κερδισατε με μεγαλους δαλτυλιους διαγωνια απο δεξια")
                    w = w + 1

        for i in range(3):
            if tetr[i][0] == 1 or tetr[i][0] == 4 or tetr[i][0] == 6 or tetr[i][0] == 9:
                if tetr[i][1] == 3 or tetr[i][1] == 4 or tetr[i][1] == 8 or tetr[i][1] == 9:
                    if tetr[i][2] == 5 or tetr[i][2] == 8 or tetr[i][2] == 6 or tetr[i][2] == 9:
                        print("Κερδισατε με σειρα απο μικρο σε μεγαλο δακτυλιο οριζοντια στη σειρα:", i + 1)
                        w = w + 1
                        break

        for i in range(3):
            if tetr[i][2] == 1 or tetr[i][2] == 4 or tetr[i][2] == 6 or tetr[i][2] == 9:
                if tetr[i][1] == 3 or tetr[i][1] == 4 or tetr[i][1] == 8 or tetr[i][1] == 9:
                    if tetr[i][0] == 5 or tetr[i][0] == 8 or tetr[i][0] == 6 or tetr[i][0] == 9:
                        print("Κερδισατε με σειρα απο μικρο σε μεγαλο δακτυλιο οριζοντια στη σειρα:", i + 1)
                        w = w + 1
                        break

        for j in range(3):
            if tetr[0][j] == 1 or tetr[0][j] == 4 or tetr[0][j] == 6 or tetr[0][j] == 9:
                if tetr[1][j] == 3 or tetr[1][j] == 4 or tetr[1][j] == 8 or tetr[1][j] == 9:
                    if tetr[2][j] == 5 or tetr[2][j] == 8 or tetr[2][j] == 6 or tetr[2][j] == 9:
                        print("Κερδισατε με σειρα απο μικρο σε μεγαλο δακτυλιo καθετα στη στηλη:", j + 1)
                        w = w + 1
                        break

        for j in range(3):
            if tetr[2][j] == 1 or tetr[2][j] == 4 or tetr[2][j] == 6 or tetr[2][j] == 9:
                if tetr[1][j] == 3 or tetr[1][j] == 4 or tetr[1][j] == 8 or tetr[1][j] == 9:
                    if tetr[0][j] == 5 or tetr[0][j] == 8 or tetr[0][j] == 6 or tetr[0][j] == 9:
                        print("Κερδισατε με σειρα απο μικρο σε μεγαλο δακτυλιo καθετα στη στηλη:", j + 1)
                        w = w + 1
                        break

        if tetr[2][0] == 1 or tetr[2][0] == 4 or tetr[2][0] == 6 or tetr[2][0] == 9:
            if tetr[1][1] == 3 or tetr[1][1] == 4 or tetr[1][1] == 8 or tetr[1][1] == 9:
                if tetr[0][2] == 5 or tetr[0][2] == 8 or tetr[0][2] == 6 or tetr[0][2] == 9:
                    w = w + 1
                    print("Κερδισατε με σειρα απο μικρο σε μεγαλο δακτυλιo διαγωνια απο δεξια")

        if tetr[2][2] == 1 or tetr[2][2] == 4 or tetr[2][2] == 6 or tetr[2][2] == 9:
            if tetr[1][1] == 3 or tetr[1][1] == 4 or tetr[1][1] == 8 or tetr[1][1] == 9:
                if tetr[0][0] == 5 or tetr[0][0] == 8 or tetr[0][0] == 6 or tetr[0][0] == 9:
                    w = w + 1
                    print("Κερδισατε με σειρα απο μικρο σε μεγαλο δακτυλιo διαγωνια απο δεξια")

        if tetr[0][0] == 1 or tetr[0][1] == 4 or tetr[0][0] == 6 or tetr[0][0] == 9:
            if tetr[1][1] == 3 or tetr[1][1] == 4 or tetr[1][1] == 8 or tetr[1][1] == 9:
                if tetr[2][2] == 5 or tetr[2][2] == 8 or tetr[2][2] == 6 or tetr[2][2] == 9:
                    w = w + 1
                    print("Κερδισατε με σειρα απο μικρο σε μεγαλο δακτυλιo διαγωνια απο δεξια")

        if tetr[0][2] == 1 or tetr[0][2] == 4 or tetr[0][2] == 6 or tetr[0][2] == 9:
            if tetr[1][1] == 3 or tetr[1][1] == 4 or tetr[1][1] == 8 or tetr[1][1] == 9:
                if tetr[0][2] == 5 or tetr[0][2] == 8 or tetr[0][2] == 6 or tetr[0][2] == 9:
                    w = w + 1
                    print("Κερδισατε με σειρα απο μικρο σε μεγαλο δακτυλιo διαγωνια απο δεξια")

        if w > 0:
            sum = sum + vhmata
            break
print(sum)

mo = sum / 100
print("Ο μεσος ορος βηματων μετα απο 100 παιχνιδια ειναι:", mo, "βηματα")



