from fpdf import FPDF
import unicodedata

def create_pdf(cover_letter_text: str, output_path: str):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    
    # Clean the text to remove/replace unsupported Unicode characters
    def clean_text(text):
        # Replace common Unicode characters with ASCII equivalents
        replacements = {
            '\u2011': '-',  # Non-breaking hyphen
            '\u2013': '-',  # En dash
            '\u2014': '--', # Em dash
            '\u2018': "'",  # Left single quote
            '\u2019': "'",  # Right single quote
            '\u201c': '"',  # Left double quote
            '\u201d': '"',  # Right double quote
            '\u2022': '-',  # Bullet point
            '\u2026': '...', # Ellipsis
        }
        
        for unicode_char, ascii_char in replacements.items():
            text = text.replace(unicode_char, ascii_char)
        
        # Remove any remaining non-latin-1 characters
        text = text.encode('latin-1', errors='ignore').decode('latin-1')
        
        return text
    
    cleaned_text = clean_text(cover_letter_text)
    
    for line in cleaned_text.split("\n"):
        pdf.multi_cell(0, 10, line)
    
    pdf.output(output_path)
    return output_path
