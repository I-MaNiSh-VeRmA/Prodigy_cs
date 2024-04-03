from PIL import Image

def encrypt_image(input_image_path, output_image_path, key):
    img = Image.open(input_image_path)
    width, height = img.size

    # Convert the image to RGB mode if it's not already in RGB
    img = img.convert("RGB")

    # Encrypt the image by swapping pixel values
    pixels = img.load()
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    img.save(output_image_path)
    print("Image encrypted successfully!")

def decrypt_image(input_image_path, output_image_path, key):
    img = Image.open(input_image_path)
    width, height = img.size

    # Convert the image to RGB mode if it's not already in RGB
    img = img.convert("RGB")

    # Decrypt the image by swapping pixel values
    pixels = img.load()
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    img.save(output_image_path)
    print("Image decrypted successfully!")

input_image = "D:\Prodigy Infotech\Image encryption\img1.jpg"
encrypted_image = "encrypted_image.jpg"
decrypted_image = "decrypted_image.jpg"
encryption_key = 123  

encrypt_image(input_image, encrypted_image, encryption_key)

decrypt_image(encrypted_image, decrypted_image, encryption_key)
