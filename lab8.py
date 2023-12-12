from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def aes_encrypt_ecb(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext

def aes_decrypt_ecb(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_text

# Приклад використання
if __name__ == "__main__":
    # Генеруємо випадковий ключ
    key = get_random_bytes(16)

    # Ваш текст для шифрування
    plaintext = b"Hello, AES ECB!"

    # Шифруємо
    ciphertext = aes_encrypt_ecb(plaintext, key)
    print("Encrypted:", ciphertext)

    # Дешифруємо
    decrypted_text = aes_decrypt_ecb(ciphertext, key)
    print("Decrypted:", decrypted_text.decode('utf-8'))
