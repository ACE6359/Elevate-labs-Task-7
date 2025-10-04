import os
import argparse
from PIL import Image

def resize_images(input_folder, output_folder, size, output_format):
    os.makedirs(output_folder, exist_ok=True)
    processed, failed = 0, 0

    for file in os.listdir(input_folder):
        if not file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp')):
            continue

        src = os.path.join(input_folder, file)
        dest = os.path.join(output_folder, os.path.splitext(file)[0] + f".{output_format.lower()}")

        try:
            with Image.open(src) as img:
                img.convert("RGB").resize(size, Image.Resampling.LANCZOS).save(dest, output_format)
                print(f"✔ {file} → {dest}")
                processed += 1
        except Exception as e:
            print(f"✖ Failed to process {file}: {e}")
            failed += 1

    print(f"\n✅ Completed: {processed} images resized | ⚠️ Failed: {failed}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="🖼️ Image Resizer Tool - Resize and convert images in batch using Python and Pillow"
    )
    parser.add_argument("--input", type=str, default="images_input", help="Input folder path")
    parser.add_argument("--output", type=str, default="images_resized", help="Output folder path")
    parser.add_argument("--width", type=int, default=800, help="New image width")
    parser.add_argument("--height", type=int, default=600, help="New image height")
    parser.add_argument("--format", type=str, default="JPEG", help="Output image format (JPEG, PNG, etc.)")

    args = parser.parse_args()
    new_size = (args.width, args.height)

    resize_images(args.input, args.output, new_size, args.format)
