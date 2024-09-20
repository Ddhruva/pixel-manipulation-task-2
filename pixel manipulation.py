from PIL import Image

def encrypt_image(image_path, output_path, key):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()  # Get pixel data
    
    width, height = img.size
    
    # Iterate through each pixel and apply a mathematical operation (encryption)
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            
            # Simple encryption: add the key value to each RGB channel (modulo 256 to stay within valid range)
            encrypted_r = (r + key) % 256
            encrypted_g = (g + key) % 256
            encrypted_b = (b + key) % 256
            
            # Set the encrypted pixel values
            pixels[x, y] = (encrypted_r, encrypted_g, encrypted_b)
    
    # Save the encrypted image
    img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")


def decrypt_image(image_path, output_path, key):
    # Open the encrypted image
    img = Image.open(image_path)
    pixels = img.load()  # Get pixel data
    
    width, height = img.size
    
    # Iterate through each pixel and reverse the mathematical operation (decryption)
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            
            # Reverse encryption: subtract the key value from each RGB channel (modulo 256)
            decrypted_r = (r - key) % 256
            decrypted_g = (g - key) % 256
            decrypted_b = (b - key) % 256
            
            # Set the decrypted pixel values
            pixels[x, y] = (decrypted_r, decrypted_g, decrypted_b)
    
    # Save the decrypted image
    img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")


def main():
    print("Image Encryption/Decryption Tool")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").upper()
    
    image_path = input("Enter the path of the image: ")
    output_path = input("Enter the path to save the output image: ")
    key = int(input("Enter the encryption/decryption key (integer): "))
    
    if choice == 'E':
        encrypt_image(image_path, output_path, key)
    elif choice == 'D':
        decrypt_image(image_path, output_path, key)
    else:
        print("Invalid choice. Please select either E (Encrypt) or D (Decrypt).")


if __name__ == "__main__":
    main()
