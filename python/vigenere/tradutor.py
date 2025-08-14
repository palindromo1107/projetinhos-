def vigenere_encrypt(text, key):
    encrypted_text = []
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text.append(encrypted_char)
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)


def vigenere_decrypt(text, key):
    decrypted_text = []
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted_text.append(decrypted_char)
            key_index = (key_index + 1) % len(key)
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)


# Exemplo de uso

#           !ADAPITAE DEPOIS!
mensagem = "Segredo@123"
chave = "CHAVE"
criptografada = vigenere_encrypt(mensagem, chave)
print("Mensagem Criptografada:", criptografada)

descriptografada = vigenere_decrypt(criptografada, chave)
print("Mensagem Descriptografada:", descriptografada)
