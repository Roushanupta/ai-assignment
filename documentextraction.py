import fitz  # PyMuPDF for text extraction
import camelot
import json

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from the PDF using PyMuPDF
    """
    doc = fitz.open(pdf_path)
    text = ""
    
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text("text")
        
    return text

def extract_tables_from_pdf(pdf_path):
    """
    Extracts tables from PDF using Camelot
    """
    tables = camelot.read_pdf(pdf_path, pages='all', flavor='stream')  # 'stream' is often better for tables with text
    table_data = []
    
    for table in tables:
        table_data.append(table.df.values.tolist())  # convert to list format
    
    return table_data

def create_json(pdf_path):
    """
    Creates a structured JSON output from a PDF, including text and tables
    """
    # Extract text from PDF
    text_content = extract_text_from_pdf(pdf_path)
    
    # Extract tables from PDF
    table_data = extract_tables_from_pdf(pdf_path)
    
    # Create a structured dictionary to store the extracted data
    pdf_data = {
        "document_text": text_content,
        "list_items": table_data
    }
    
    # Convert the data to a JSON format
    json_data = json.dumps(pdf_data, indent=4)
    
    return json_data

# Example usage
if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF: ")
    extracted_json = create_json(pdf_path)
    
    # Display the JSON output
    print("\nExtracted JSON data:")
    print(extracted_json)
