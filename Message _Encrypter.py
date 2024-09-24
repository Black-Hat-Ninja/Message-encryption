from pyfiglet import Figlet
from cryptography.fernet import Fernet
from termcolor import colored
f = Figlet(font='slant')
print(f.renderText('Personal message encrypter via Fernet'))
print("\n \t\t\t\t\ Written by: ")
print(colored('\t\t\t\t\t Blak Hat India', 'red'))

# Function to generate a key and encrypt a message
def encrypt_message(message):
    # Generate a key
    key = Fernet.generate_key()
    fernet = Fernet(key)
    
    # Encrypt the message
    encrypted_message = fernet.encrypt(message.encode())
    
    return key, encrypted_message

# Main function to get user input and perform encryption
def main():
    user_input = input("Enter the string you want to encrypt: ")
    key, encrypted_message = encrypt_message(user_input)
    
    print(f"Key: {key.decode()}")
    print(f"Encrypted message: {encrypted_message.decode()}")

if __name__ == "__main__":
    main()
