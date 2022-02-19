paixths1 = 0
paixths2 = 0
for i in range(100):
    from random import randint

    print("Δωστε αρχικες θεσεις για τα πιονια σας ")
    grammhA = randint(1, 8)
    tempA1 = grammhA  # τα temp χρησιμευουν στο να αποθηκευονται οι συντεταγμενες της προηγουμενης κινησης ωστε να
    sthlhA = randint(1, 8)  # συγκριθουν με αυτες της επομενης κινησης και να μπορεσουμε να δουμε αν ειναι επιτρεπτη
    tempA2 = sthlhA
    while True:
        grammhB = randint(1, 8)
        sthlhB = randint(1, 8)
        if grammhA != grammhB and sthlhA != sthlhB:
            break
        else:
            print("Η θεση εχει ειδη χρησιμοποιηθει ως αρχικη απο τον προηγουμενο παιχτη")
    tempB1 = grammhB
    tempB2 = sthlhB

    while True:
        while True:
            grammhA = randint(1, 8)
            sthlhA = randint(1, 8)
            if grammhA != tempA1:  # ο πυργος μπορει να αλλαξει ειτε γραμμη ειτε στηλη αλλα οχι και τα δυο μαζι
                if sthlhA == tempA2:
                    tempA1 = grammhA
                    tempA2 = sthlhA
                    break

            else:
                if sthlhA != tempA2:
                    if sthlhA == tempA2:
                        tempA1 = grammhA
                        tempA2 = sthlhA
                        break

        if grammhA == grammhB and sthlhA == sthlhB:
            paixths1 = paixths1 + 1
            print("Κερδισε ο παιχτης 1")
            break
        while True:
            grammhB = randint(1, 8)
            sthlhB = randint(1, 8)
            if grammhB != tempB1 and sthlhB != tempB2:  # ο αξιοματικος αλλαζει γραμμη και στηλη καθε φορα διοτι κηνηται μονο
                tempB1 = grammhB  # διαγωνια
                tempB2 = sthlhB
                break

        if grammhA == grammhB and sthlhA == sthlhB:
            paixths2 = paixths2 + 1
            print("Κερδισε ο παιχτης 2")
            break
print("Στην σκακιερα 8*8:")
print("Ο παιχτης 1 μετα απο 100 παιχνιδια μαζεψαι:",paixths1,"βαθμους")
print("Ο παιχτης 2 μετα απο 100 παιχνιδια μαζεψαι:",paixths2,"βαθμους")



paixths1 = 0
paixths2 = 0
for i in range(100):
    from random import randint

    print("Δωστε αρχικες θεσεις για τα πιονια σας ")
    grammhA = randint(1, 7)
    tempA1 = grammhA  # τα temp χρησιμευουν στο να αποθηκευονται οι συντεταγμενες της προηγουμενης κινησης ωστε να
    sthlhA = randint(1, 7)  # συγκριθουν με αυτες της επομενης κινησης και να μπορεσουμε να δουμε αν ειναι επιτρεπτη
    tempA2 = sthlhA
    while True:
        grammhB = randint(1, 7)
        sthlhB = randint(1, 7)
        if grammhA != grammhB and sthlhA != sthlhB:
            break
        else:
            print("Η θεση εχει ειδη χρησιμοποιηθει ως αρχικη απο τον προηγουμενο παιχτη")
    tempB1 = grammhB
    tempB2 = sthlhB

    while True:
        while True:
            grammhA = randint(1, 7)
            sthlhA = randint(1, 7)
            if grammhA != tempA1:  # ο πυργος μπορει να αλλαξει ειτε γραμμη ειτε στηλη αλλα οχι και τα δυο μαζι
                if sthlhA == tempA2:
                    tempA1 = grammhA
                    tempA2 = sthlhA
                    break

            else:
                if sthlhA != tempA2:
                    if sthlhA == tempA2:
                        tempA1 = grammhA
                        tempA2 = sthlhA
                        break

        if grammhA == grammhB and sthlhA == sthlhB:
            paixths1 = paixths1 + 1
            print("Κερδισε ο παιχτης 1")
            break
        while True:
            grammhB = randint(1, 7)
            sthlhB = randint(1, 7)
            if grammhB != tempB1 and sthlhB != tempB2:  # ο αξιοματικος αλλαζει γραμμη και στηλη καθε φορα διοτι κηνηται μονο
                tempB1 = grammhB  # διαγωνια
                tempB2 = sthlhB
                break

        if grammhA == grammhB and sthlhA == sthlhB:
            paixths2 = paixths2 + 1
            print("Κερδισε ο παιχτης 2")
            break
print("Στην σκακιερα 7*7:")
print("Ο παιχτης 1 μετα απο 100 παιχνιδια μαζεψαι:",paixths1,"βαθμους")
print("Ο παιχτης 2 μετα απο 100 παιχνιδια μαζεψαι:",paixths2,"βαθμους")



paixths1 = 0
paixths2 = 0
for i in range(100):
    from random import randint

    print("Δωστε αρχικες θεσεις για τα πιονια σας ")
    grammhA = randint(1, 7)
    tempA1 = grammhA  # τα temp χρησιμευουν στο να αποθηκευονται οι συντεταγμενες της προηγουμενης κινησης ωστε να
    sthlhA = randint(1, 8)  # συγκριθουν με αυτες της επομενης κινησης και να μπορεσουμε να δουμε αν ειναι επιτρεπτη
    tempA2 = sthlhA
    while True:
        grammhB = randint(1, 7)
        sthlhB = randint(1, 8)
        if grammhA != grammhB and sthlhA != sthlhB:
            break
        else:
            print("Η θεση εχει ειδη χρησιμοποιηθει ως αρχικη απο τον προηγουμενο παιχτη")
    tempB1 = grammhB
    tempB2 = sthlhB

    while True:
        while True:
            grammhA = randint(1, 7)
            sthlhA = randint(1, 8)
            if grammhA != tempA1:  # ο πυργος μπορει να αλλαξει ειτε γραμμη ειτε στηλη αλλα οχι και τα δυο μαζι
                if sthlhA == tempA2:
                    tempA1 = grammhA
                    tempA2 = sthlhA
                    break

            else:
                if sthlhA != tempA2:
                    if sthlhA == tempA2:
                        tempA1 = grammhA
                        tempA2 = sthlhA
                        break

        if grammhA == grammhB and sthlhA == sthlhB:
            paixths1 = paixths1 + 1
            print("Κερδισε ο παιχτης 1")
            break
        while True:
            grammhB = randint(1, 7)
            sthlhB = randint(1, 8)
            if grammhB != tempB1 and sthlhB != tempB2:  # ο αξιοματικος αλλαζει γραμμη και στηλη καθε φορα διοτι κηνηται μονο
                tempB1 = grammhB  # διαγωνια
                tempB2 = sthlhB
                break

        if grammhA == grammhB and sthlhA == sthlhB:
            paixths2 = paixths2 + 1
            print("Κερδισε ο παιχτης 2")
            break
print("Στην σκακιερα 7*8:")
print("Ο παιχτης 1 μετα απο 100 παιχνιδια μαζεψαι:",paixths1,"βαθμους")
print("Ο παιχτης 2 μετα απο 100 παιχνιδια μαζεψαι:",paixths2,"βαθμους")