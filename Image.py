#import required libraries
from rembg import remove
from PIL import Image

#Creating a function for image background removal purpose
def background_removal(image_path, new_image_path):
    # Open the original imager
    image = Image.open(image_path)

    # Use rembg to remove the background
    new_image = remove(image)

    # Create a new image with white background of the same size as the original image
    white_background = Image.new("RGB", image.size, (255, 255, 255))

    # Paste the foreground (image with removed background) onto the white background
    white_background.paste(new_image, (0, 0), new_image)

    # Save the new image with white background
    white_background.save(new_image_path)

if __name__ == "__main__":
    image_path = "Image.jpg"    #original image path
    new_image_path = "whitebackground_image.png"    #new image path

    background_removal(image_path, new_image_path)
