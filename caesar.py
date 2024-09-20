from colorama import Fore, Style, init
init(autoreset=True)
def caesar_cipher(text, shift, mode='encrypt', case_sensitive=False):
    result = ""
    shift = shift if mode == 'encrypt' else -shift
    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            new_char = chr((ord(char) + shift - 65) % 26 + 65)
            result += new_char if case_sensitive else new_char.lower()

        elif char.islower():
            new_char = chr((ord(char) + shift - 97) % 26 + 97)
            result += new_char if case_sensitive else new_char.upper()
        else:
            result += char  
    return result
def terminal_caesar_cipher():
    print(f"\n{Fore.CYAN}{'='*10} Welcome to the {Fore.YELLOW}Caesar Cipher Program {'='*10}")
    print(f"{Fore.MAGENTA}> Encrypt and Decrypt Texts Securely\n")
    while True:
        print(f"\n{Fore.CYAN}{'-'*5} Options {'-'*5}")
        print(f"{Fore.GREEN}[1] Encrypt")
        print(f"{Fore.GREEN}[2] Decrypt")
        print(f"{Fore.RED}[3] Exit")
        choice = input(f"\n{Fore.YELLOW}> Choose an option (1, 2, or 3): ")
        if choice == '1' or choice == '2':
            message = input(f"\n{Fore.CYAN}Enter your message: {Fore.WHITE}")
            try:
                shift = int(input(f"{Fore.CYAN}Enter the shift value (e.g., 4): {Fore.WHITE}"))
            except ValueError:
                print(f"{Fore.RED}Invalid shift value. Please enter a valid number.")
                continue
            case_sensitive = input(f"{Fore.CYAN}Case sensitive (yes/no)? ").lower() == "yes"
            mode = 'encrypt' if choice == '1' else 'decrypt'
            result = caesar_cipher(message, shift, mode=mode, case_sensitive=case_sensitive)
            if choice == '1':
                print(f"\n{Fore.GREEN}✔ Encrypted message: {Fore.WHITE}{result}")
            else:
                print(f"\n{Fore.GREEN}✔ Decrypted message: {Fore.WHITE}{result}")
        elif choice == '3':
            print(f"\n{Fore.RED}Exiting... Goodbye!")
            break
        else:
            print(f"{Fore.RED}Invalid option. Please choose 1, 2, or 3.")
if __name__ == "__main__":
    terminal_caesar_cipher()
