python
import os
import binascii
import bitcoin
from decimal import Decimal

def generate_random_key():
    # Generate a random private key
    private_key = os.urandom(32)
    private_key_hex = binascii.hexlify(private_key).decode()

    # Get the corresponding public key
    public_key = bitcoin.privtopub(private_key_hex)

    # Get the Bitcoin address
    address = bitcoin.pubtoaddr(public_key)

    return private_key_hex, address

def find_position(hex_str):
    return int(hex_str, 16) + 1

def find_private_key(position):
    return hex(int(position) - 1)[2:].zfill(64)

def calculate_position(string):
    characters = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    base = len(characters)
    length = len(string)
    position = 0
    power = 1

    for i in range(length - 1, -1, -1):
        char = string[i]
        digit = characters.index(char)
        position += digit * power
        power *= base

    return position

def calculate_address_position(address):
    characters = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    base = len(characters)
    position = 0
    power = 1

    for i in range(len(address) - 1, -1, -1):
        char = address[i]
        digit = characters.index(char)
        position += digit * power
        power *= base

    return position

user = input("1: Generate and Find Priv Position\n2: Position to Priv\n3: Generate and Find Address Position\n4: Address to Position\n[Ans]: ")

if user == '1':
    private_key_hex, address = generate_random_key()
    print("Private Key (Hex):", private_key_hex)
    print("Address:", address)
    position = find_position(private_key_hex)
    print("Private Key Position:", position)
    address_position = calculate_address_position(address) + 1
    print("Address Position:", address_position)

elif user == '2':
    position = Decimal(input("\nPosition: "))
    private_key = find_private_key(position)
    print("Private Key:", private_key)

elif user == '3':
    private_key_hex, address = generate_random_key()
    print("Private Key (Hex):", private_key_hex)
    print("Address:", address)
    position = find_position(address)
    print("Address Position:", position)
    private_key_position = find_position(private_key_hex)
    print("Private Key Position:", private_key_position)

elif user == '4':
    address = input("\nAddress: ")
    position = calculate_address_position(address)
    print("Address Position:", position)

else:
    print('\nWrong input')
