def dubbel(list):
    for x in list:
        if list.count(x) == 2:
            return x
    return None

def dubbels(list):
    eenmaal = set() #set ipv list aanmaken want geen dubbels erin!
    meermaals = set()
    for x in list:
        if list.count(x) == 1:
            eenmaal.add(x)
        elif list.count(x) >= 2:
            meermaals.add(x)
    return eenmaal, meermaals



# append() hoort bij een list
# Een list is een geordende verzameling waarin elementen dubbel mogen voorkomen.
# ✔️ append() voegt iets achteraan toe
# ✔️ volgorde blijft behouden
# ✔️ dubbele waarden zijn toegestaan

# 🟦 add() hoort bij een set
# Een set is een ongeordende verzameling waarin alleen unieke elementen mogen zitten.

# append() → lijst → voegt element toe (met volgorde, duplicates ok)
# add() → set → voegt element toe (geen volgorde, geen duplicates)