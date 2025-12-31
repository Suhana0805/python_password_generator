import random
import string

def generate_password(length=12):
    # Define what characters to use
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters from the list
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

if __name__ == "__main__":
    print("--- Secure Password Generator ---")
    try:
        user_length = int(input("Enter password length (e.g., 8, 12, 16): "))
        if user_length < 6:
            print("Warning: Password creates is too short to be secure!")
        
        pwd = generate_password(user_length)
        print(f"\nYour Secure Password: {pwd}")
        
    except ValueError:
        print("Please enter a valid number.")