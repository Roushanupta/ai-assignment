from PIL import Image
import pytesseract

# Specify the path to the Tesseract executable (if it's not in your PATH)
# For Windows, you might need to specify the full path like:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Use pytesseract to extract text
    text = pytesseract.image_to_string(img)

    return text

# Example usage
if __name__ == "__main__":
    image_path = input("Enter the path to the image: ")
    extracted_text = extract_text_from_image(image_path)
    print("\nExtracted Text:")
    print(extracted_text)
