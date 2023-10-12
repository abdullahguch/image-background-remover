import rembg
from PIL import Image
import io
import os

def remove_background(input_path):
    try:
        # Explicitly provide the file extension
        _, file_extension = os.path.splitext(input_path)
        file_extension = file_extension.lower()

        # Supported file extensions by rembg
        supported_extensions = ['.png', '.jpg', '.jpeg']

        if file_extension not in supported_extensions:
            raise ValueError(f"Unsupported file extension: {file_extension}")

        with open(input_path, "rb") as input_file:
            input_data = input_file.read()

        # Use rembg to remove the background
        output_data = rembg.remove(input_data)

        # Convert the binary data to a PIL Image
        output_image = Image.open(io.BytesIO(output_data))

        # Convert the image to RGBA mode (add alpha channel)
        output_image = output_image.convert('RGBA')

        # Save the resulting image as PNG using the same path with a ".png" extension
        output_path = os.path.splitext(input_path)[0] + ".png"
        output_image.save(output_path, format='PNG')

        print("Background removed successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_path = input("Enter the path of the input image: ")

    remove_background(input_path)
