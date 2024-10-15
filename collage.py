from PIL import Image
import os

images_path = "image_dataset"

# Set the desired size for each image in the collage
image_width, image_height = 400, 400  # You can adjust this as needed

# Create a list to hold all images
all_images = []

for group_num in range(1, 11):
    for img_num in range(1, 3):
        image_filename = f'{images_path}/group{group_num}_{img_num}.jpg'  # Adjust extension if not .jpg
        if os.path.exists(image_filename):
            img = Image.open(image_filename)
            # Resize the image to the desired size
            img = img.resize((image_width, image_height), resample=Image.LANCZOS)
            all_images.append(img)
        else:
            print(f"Warning: {image_filename} not found.")

# Calculate the size of the collage
num_columns = 10  # 10 images per row
num_rows = 2      # 2 rows
collage_width = num_columns * image_width
collage_height = num_rows * image_height

# Create a new blank image for the collage
collage_image = Image.new('RGB', (collage_width, collage_height), color='white')

# Paste images into the collage
for idx, img in enumerate(all_images):
    x = (idx % num_columns) * image_width
    y = (idx // num_columns) * image_height
    collage_image.paste(img, (x, y))

# Save the collage image
collage_image.save('collage.jpg')
print("Collage created and saved as collage.jpg")
