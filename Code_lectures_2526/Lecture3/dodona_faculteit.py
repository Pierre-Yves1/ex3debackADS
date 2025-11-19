def faculteit_rec(n):
    if n == 0:
        return 1
    else:
        return n * faculteit_rec(n - 1)  # voert dus fac opnieuw uit, tot n=0, dan stopconditie


def faculteit(n):  # dit op niet-recursieve manier, op manier ve student tijdens les, prof zou volgende blokje doen
    i = 1
    result = 1
    while i <= n:
        result = result * i
        i = i + 1
    return result


def faculteit2(n):  # manier hoe prof op niet-recursieve manier zou doen
    result = 1
    for i in range(1,
                   n + 1):  # n+1 want n'de getal moet er nog bij, hier kan 0 tot n niet want 0 gaat niet, moet beginnen vf 1
        result = result * i
    return result


aantal_testen = int(input("aantal testen"))
for i in range(0, aantal_testen):  # is zelfde als 1 tot aantal_testen+1 denk ik
    getal = int(input("Getal?"))
    if getal > 13:
        print("invoer te groot")
    else:
        print(faculteit2(getal))
