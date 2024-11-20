# Jackie Hall
# UWYO COSC 1010
# Submission Date 11/20/2024
# Lab 10
# Lab Section: 15
# Sources, people worked with, help given to: 
# your
# comments
# here

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()



# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

from pathlib import Path

def files():
    rock = Path('rockyou.txt')
    has = Path('hash')




# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.

try:
    with open(has, 'r') as hashf:
        rhas = hashf.read().strip()

except FileNotFoundError:
        print("Error: 'hash' file not found.")
        return

try:
    with open(rock,'r', encoding='utf-8', errors='ignore') as rockf:
        pwords = rock.readlines()

except FileNotFoundError:
    print("File not found.")
    return

else:
    for pword in pwords:
        pword =  pword.strip()
        hashedp = get_hash(pword) 

    if hashedp == rhas:
        print(f"Password cracked: {pword}")
        break
    
    else:
        print("Error finding password")

# - Read in the value stored within `hash`.
#   - You must use a try and except block.

# ``  <---- coded by my cat and shes very proud


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.
