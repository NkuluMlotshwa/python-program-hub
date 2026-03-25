#Sample IBAN examples you can use to test:
#GB72 HBZU 7006 7212 1253 00
#FR14 2004 1010 0505 0001 3M02 606
#GB72 HBZU 7006 7212 1253 01
#ES91 2100 0418 4502 0005 1332
#FR14 2004 1010 0505 0001 3M02 60@
#GB72HBZU7006
#NL91 ABNA 0417 1643 00
#NL91 ABNA 0417 1643 01

def caesar_encrypt():
    return "Caesar Cipher (Encrypt) not yet implemented."


def caesar_decrypt():
    return "Caesar Cipher (Decrypt) not yet implemented."


def numbers_processor():
    return "Numbers Processor not yet implemented."


def iban_validator():
    return "IBAN Validator not yet implemented."


def show_menu():
    print("\n==============================")
    print(" Welcome to the Python Program Hub")
    print("==============================")
    print("1. Caesar Cipher (Encrypt)")
    print("2. Caesar Cipher (Decrypt)")
    print("3. Numbers Processor")
    print("4. IBAN Validator")
    print("5. Exit")
    print("==============================")


def play_again():
    while True:
        choice = input("\nWould you like to choose another program? (yes/no): ").lower()

        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("Invalid input. Please enter yes or no.")


def main():
    print("Hello! Welcome to the program.")

    while True:
        show_menu()
        choice = input("Please enter your choice (1-5): ")

        if choice == "1":
            print(caesar_encrypt())
            if not play_again():
                print("Goodbye!")
                break

        elif choice == "2":
            print(caesar_decrypt())
            if not play_again():
                print("Goodbye!")
                break

        elif choice == "3":
            print(numbers_processor())
            if not play_again():
                print("Goodbye!")
                break

        elif choice == "4":
            print(iban_validator())
            if not play_again():
                print("Goodbye!")
                break

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 5.")


main()
