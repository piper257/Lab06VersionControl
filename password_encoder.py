def encoder(password):
    encoded_password = ""
    for item in password:
        # Added a fix for instances where (item + 3) >= 10
        new_item = int(item) + 3
        if new_item >= 10:
            new_item -= 10
        encoded_password += str(new_item)

    return encoded_password


# Logan B
def decoder(e_password):
    d_password = ""
    for digit in e_password:
        new_digit = int(digit) - 3
        if new_digit < 0:
            new_digit += 10
        d_password += str(new_digit)

    return d_password


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
            d_password = decoder(e_password)
            print(f"The encoded password is {e_password}, and the decoded password is {d_password}.")


if __name__ == "__main__":
    main()
