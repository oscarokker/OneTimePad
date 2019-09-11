from secrets import token_bytes
from typing import Tuple

if __name__ == "__main__":
    key1, key2 = encrypt("One Time Pad!")
    print(key1)
    print(key2)
    result: str = decrypt(key1, key2)
    print(result)

def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    # "big" betyder, at mest betydende bit er i starten (venstre) er den der repræsenterer den højeste numeriske værdi
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy  # XOR
    return dummy, encrypted

def random_key(length: int) -> int:
    # Generate length random bytes
    tb: bytes = token_bytes(length)
    # Convert those bytes into a bit string and return it
    return int.from_bytes(tb, "big")

def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2 # XOR operator
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()
