def main():
    try:
        number1 = int(input("Enter an integer: "))      
        number2 = int(input("Enter an integer: "))      
        result = number1 / number2
        print("Result is " + str(result))
    except ZeroDivisionError: # Catch zero divisor error
        print("Division by zero!")
    except: #een andere onbenoemde fout, vb als je 5 deelt door tekst
        print("Something wrong in the input")
    else: #else w enkel uitgevoerd als geen van die except's wordt uitgevoerd
        print("No exceptions")
    finally: # finally w altijd uitgevoerd
        print("The finally clause is executed")

main()