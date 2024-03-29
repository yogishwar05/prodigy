from PIL import Image

def encrypt_image(image_path, key):
    try:
        img = Image.open(image_path)
        width, height = img.size
        pixels = img.load()

        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

        encrypted_image_path = image_path.split('.')[0] + "_encrypted.png"
        img.save(encrypted_image_path)
        print("Image encrypted successfully!")
        return encrypted_image_path
    except Exception as e:
        print("Error:", e)

def decrypt_image(image_path, key):
    try:
        img = Image.open(image_path)
        width, height = img.size
        pixels = img.load()

        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

        decrypted_image_path = image_path.split('_encrypted')[0] + "_decrypted.png"
        img.save(decrypted_image_path)
        print("Image decrypted successfully!")
        return decrypted_image_path
    except Exception as e:
        print("Error:", e)

def main():
    while True:
        print("\n1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            image_path = input("Enter the path of the image to encrypt: ")
            key = int(input("Enter the encryption key (integer): "))
            encrypted_image_path = encrypt_image(image_path, key)
            print("Encrypted image saved as:", encrypted_image_path)
        elif choice == '2':
            image_path = input("Enter the path of the image to decrypt: ")
            key = int(input("Enter the encryption key (integer): "))
            decrypted_image_path = decrypt_image(image_path, key)
            print("Decrypted image saved as:", decrypted_image_path)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()