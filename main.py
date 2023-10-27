def mainMenu():
    print("Menu")
    print("-"*13)
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encoder(password):
    pass_str = str(password)
    pass_list = list(pass_str)
    value = []
    for c in pass_list:
        value.append(int(c) + 3)
        final = ''.join(map(str, value))
    return final

#Decoder code -  Connor Trzcinski
def decoder(password):
    pass_str = str(password)
    pass_list = list(pass_str)
    value= []
    for c in pass_list:
        value.append(int(c) // 3)
        final = ''.join(map(str, value))
    return final



def main():
    mainMenu()
    run = True
    while run == True:
        choice = int(input("Please enter an option:" + " "))
        if choice == 1:
            global password
            password = int(input("Please enter a password to encode"))
            encoder(password)
            print("Your password has been encoded and stored")
        elif choice == 2:
            print(f"The encoded password is {encoder(password)}, and the original password is {password}.")
        elif choice == 3:
            run = False


if __name__ == "__main__":
    main()




