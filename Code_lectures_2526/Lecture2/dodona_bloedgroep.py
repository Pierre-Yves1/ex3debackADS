# Helper: bloedgroep splitsen in ABO-deel en rhesus (+ of -)
def split_bloedgroep(bg):
    rh = bg[-1]          # laatste teken is altijd + of - # laatste teken (dus -1) is altijd + of -, de rhesus
    if bg.startswith("AB"):
        abo = "AB"
    else:
        abo = bg[0]      #kan A, B of O zijn
    return abo, rh


# Mogelijke ABO-genotypes (allelen) voor een fenotype
def abo_genotypes(abo):
    if abo == "A":
        return [("A", "A"), ("A", "O")]
    elif abo == "B":
        return [("B", "B"), ("B", "O")]
    elif abo == "AB":
        return [("A", "B")]
    else:   # "O"
        return [("O", "O")]


# Mogelijke rhesus-genotypes voor een fenotype
def rh_genotypes(rh):
    if rh == "+":
        return [("+", "+"), ("+", "-")]
    else:   # "-"
        return [("-", "-")]


# Bepaal ABO-bloedgroep uit 2 allelen
def abo_from_alleles(a1, a2):
    s = {a1, a2}
    if s == {"A", "B"}:
        return "AB"
    elif s == {"A"} or s == {"A", "O"}:
        return "A"
    elif s == {"B"} or s == {"B", "O"}:
        return "B"
    else:
        return "O"


# Bepaal rhesus uit 2 allelen
def rh_from_alleles(r1, r2):
    if r1 == "-" and r2 == "-":
        return "-"
    else:
        return "+"


def bloedgroep_kind(ouder1, ouder2):
    abo1, rh1 = split_bloedgroep(ouder1)
    abo2, rh2 = split_bloedgroep(ouder2)

    abo_g1 = abo_genotypes(abo1)
    abo_g2 = abo_genotypes(abo2)
    rh_g1 = rh_genotypes(rh1)
    rh_g2 = rh_genotypes(rh2)

    mogelijke_abo = set()
    mogelijke_rh = set()

    # Alle mogelijke ABO-bloedgroepen van het kind
    for g1 in abo_g1:
        for g2 in abo_g2:
            for a1 in g1:
                for a2 in g2:
                    mogelijke_abo.add(abo_from_alleles(a1, a2))

    # Alle mogelijke rhesusfactoren van het kind
    for rg1 in rh_g1:
        for rg2 in rh_g2:
            for r1 in rg1:
                for r2 in rg2:
                    mogelijke_rh.add(rh_from_alleles(r1, r2))

    # Combineer ABO en rhesus
    result = set()
    for abo in mogelijke_abo:
        for rh in mogelijke_rh:
            result.add(abo + rh)

    return result


def bloedgroep_ouder(ouder, kind):
    mogelijke_ouders = set()

    # alle mogelijke bloedgroepen
    abo_groups = ["O", "A", "B", "AB"]
    rh_groups = ["-", "+"]

    for abo in abo_groups:
        for rh in rh_groups:
            bg = abo + rh
            # als deze bloedgroep samen met 'ouder' het kind kan geven, is hij mogelijk
            if kind in bloedgroep_kind(ouder, bg):
                mogelijke_ouders.add(bg)

    return mogelijke_ouders