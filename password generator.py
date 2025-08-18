import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters =''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected."
    
    password =''.join(random.choice(characters)for _ in range(length))
    return password
    
def main():
    print("Password Generator")

    try:
        length =int(input("Enter the desired password length:"))
    except valueError:
        print("Invalid input. please enter a number.")
        return
    if length <= 0:
        print("password length must be greater than 0.")
        return


    use_upper = input("Include uppercase letters?(y/n): ").lower() =='y'
    use_lower = input("Include lowercase letters?(y/n): ").lower() =='y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() =='y'

    password = generate_password(length,use_upper,use_lower,use_digits,use_symbols)

    print("\ngenerated password",password)

if __name__=="__main()__":
    main()
    
    
