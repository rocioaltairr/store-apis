# from Crypto.Cipher import AES
# import hashlib

# def encryptpassword(password):
#     password = password.encode()
#     key = hashlib.sha256(password).digest()
#     IV = 'This is an IV456'
#     cipher = AES.new(key, AES.MODE_CBC, IV)
#     padded_message = pad_message(password)
#     encrypted_message = cipher.encrypt(padded_message)
#     return encrypted_message

# def decrypt_password(encrypted_password):
#     password = b'mypassword'  # Replace with the password used for encryption
#     key = hashlib.sha256(password).digest()
#     IV = 'This is an IV456'
#     cipher = AES.new(key, AES.MODE_CBC, IV)
#     decrypted_text = cipher.decrypt(encrypted_password).strip().decode()
#     return decrypted_text

# def pad_message(message):
#     while len(message) % 16 != 0:
#         message = message + b" "
#     return message

# # print(encryptpassword("12345"))


