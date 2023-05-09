import os
import argparse
from PIL import Image

def add_watermark(input_folder, logo_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if not os.path.exists(logo_path):
        print(f"Error: Logo file '{logo_path}' does not exist.")
        return

    for file in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file)
        file_ext = os.path.splitext(file)[1].lower()

        if file_ext in ['.png', '.jpg', '.jpeg']:
            image = Image.open(file_path).convert("RGBA")
            image_width, image_height = image.size

            logo = Image.open(logo_path).convert("RGBA")

            # Resize the logo to be 5% of the target image size
            target_logo_width = int(image_width * 0.13)
            logo_ratio = target_logo_width / logo.width
            target_logo_height = int(logo.height * logo_ratio)
            logo = logo.resize((target_logo_width, target_logo_height), Image.LANCZOS)

            logo_width, logo_height = logo.size

            # Adding Padding to the logo
            logo_padding = int(image_width * 0.02)
            
            # Position the logo in the bottom right corner
            position = (image_width - logo_width - logo_padding, image_height - logo_height - logo_padding)

            # Overlay the logo on the image
            overlay = Image.new("RGBA", image.size, (255, 255, 255, 0))
            overlay.paste(logo, position, mask=logo)
            watermarked_image = Image.alpha_composite(image, overlay)
            watermarked_image = watermarked_image.convert("RGB")

            output_file_path = os.path.join(output_folder, file)
            watermarked_image.save(output_file_path)

            print(f"Watermarked image saved: {output_file_path}")


def main():
    parser = argparse.ArgumentParser(description='Add watermark to images in a folder')
    parser.add_argument('-i', '--input', type=str, required=True, help='Input folder containing images')
    parser.add_argument('-l', '--logo', type=str, required=True, help='Logo file (PNG format recommended)')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output folder for watermarked images')

    args = parser.parse_args()

    add_watermark(args.input, args.logo, args.output)

if __name__ == "__main__":
    main()
