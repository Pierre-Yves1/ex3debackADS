try:
    number = float(input("Enter a number: "))
    print("The number entered is", number)
except ValueError as ex: #valueError: als je iets wilt inlezen en omzetten vb nr een float en dat lukt niet => ValueError
    #ValueError naam gegeven 'ex' om foutboodschap in volgende tekst mee te geven
    print("Exception:", ex)


