def isISBN(code: str):
    if len(code) != 13 or not code.isdigit():
        return False

    if code[:3] not in ('978', '979'): #:3 betekent van start tot 3 -1, dus 0,1,2
        return False

    o = int(code[0]) + int(code[2]) + int(code[4]) + int(code[6]) + int(code[8]) + int(code[10]) #int doen want als je niet doet neemt hij bvb '2' en dan heb je letter ipv getal
    e = int(code[1]) + int(code[3]) + int(code[5]) + int(code[7]) + int(code[9]) + int(code[11])
    check = (10-(o+3*e) % 10) % 10 #mod = %

    if check == int(code[12]):
        return True
    else:
        return False

def group_name(code: str):
    g = code[3]
    if g == "0" or g == "1":
        return "Engelstalige landen"
    elif g == "2":
        return "Franstalige landen"
    elif g == "3":
        return "Duitstalige landen"
    elif g == "4":
        return "Japan"
    elif g == "5":
        return "Russischtalige landen"
    elif g == "7":
        return "China"
    else:  # 6, 8 of 9
        return "Overige landen"

def overzicht(codes: list):
    counts = {
        "Engelstalige landen": 0,
        "Franstalige landen": 0,
        "Duitstalige landen": 0,
        "Japan": 0,
        "Russischtalige landen": 0,
        "China": 0,
        "Overige landen": 0,
        "Fouten": 0,
    }
    for code in codes:
        if isISBN(code):
            groep = group_name(code)
            counts[groep] += 1
        else:
            counts["Fouten"] +=1


    # in exact de juiste volgorde printen
    print("Engelstalige landen:", counts["Engelstalige landen"])
    print("Franstalige landen:", counts["Franstalige landen"])
    print("Duitstalige landen:", counts["Duitstalige landen"])
    print("Japan:", counts["Japan"])
    print("Russischtalige landen:", counts["Russischtalige landen"])
    print("China:", counts["China"])
    print("Overige landen:", counts["Overige landen"])
    print("Fouten:", counts["Fouten"])




