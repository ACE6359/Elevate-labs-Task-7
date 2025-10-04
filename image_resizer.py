import os
from PIL import Image

def resize_images(input_folder="images_input", output_folder="images_resized", size=(800, 600), output_format="JPEG"):
    os.makedirs(output_folder, exist_ok=True)
    processed, failed = 0, 0

    for file in os.listdir(input_folder):
        if not file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
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
    resize_images()
