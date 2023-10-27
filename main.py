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

print(encoder(12345555))


