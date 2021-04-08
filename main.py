from libraries.encription import Encrypt

if __name__=='__main__':
    encrypt = Encrypt()

    keys = encrypt.generate_keys()

    file_out = open("public.pem", "wb")
    file_out.write(keys['public_key'])
    file_out.close()

    file_out = open("private.pem", "wb")
    file_out.write(keys['private_key'])
    file_out.close()

    encrypt.read_public_key('public.pem')
    encrypt.set_private_key_path('private.pem')

    text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"""

    print(f'Original text\n\n{text}')

    encrypt_data = encrypt.encrypt_string(text)

    print(f'\n\nEncrypted data\n\n{encrypt_data}')

    decrypted_text = encrypt.decrypt_data(encrypt_data)

    print(f'\n\nDecrypted Text\n\n{decrypted_text}')
