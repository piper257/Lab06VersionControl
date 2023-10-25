def encoder(password):
    encoded_password = ""
    for item in password:
        encoded_password += str(int(item) + 3)
    return encoded_password


def main():
    choice = -1
    e_password = None
    while choice != 0:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = input("Please enter your password to encode: ")
            e_password = encoder(password)
            print("Your password has been encoded and stored")
        elif choice == 2:
            print(f"The encoded password is {e_password}, and the decoded password is {1}.")

if __name__ == "__main__":
    main()
