# Copyright (c) 2025 Swaraj Puppalwar (UltronTheAI)
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
# Project: https://github.com/UltronTheAI/eBook-Generator-AI-Agent
import os
import re
import markdown
import pdfkit
from PyPDF2 import PdfMerger

def generate_pdf(content, output_path, font_size=20):
    """
    Converts Markdown content into a formatted PDF with full-page text fit.
    
    Args:
        content (str): Markdown content to convert to PDF.
        output_path (str): Path for the output PDF file.
        font_size (int, optional): Font size for the PDF. Default is 20.
        
    Returns:
        None
    """
    # Convert Markdown to HTML with additional styling
    html_content = markdown.markdown(content)
    styled_html = f"""
    <html>
    <head>
        <style>
            body {{
                font-size: {font_size};
                margin: 0;
                padding: 20mm;
                text-align: justify;
            }}
            h1 {{
                text-align: center;
                font-size: {font_size+4};
            }}
            p {{
                line-height: 1.6;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # PDF generation options for full-page fit
    options = {
        "page-size": "A4",
        "margin-top": "0mm",
        "margin-bottom": "0mm",
        "margin-left": "0mm",
        "margin-right": "0mm",
        "encoding": "UTF-8",
        "no-outline": None
    }

    # Generate the PDF
    pdfkit.from_string(styled_html, output_path, options=options)

def create_book_pdf(path_folder):
    """
    Merges individual chapter PDFs into a single book PDF.
    
    Args:
        path_folder (str): Path to the folder containing the PDFs to merge.
        
    Returns:
        tuple: (success (bool), list of source PDF files)
    """
    merger = None
    try:
        # Read data.json
        with open(os.path.join(path_folder, 'data.json'), 'r') as f:
            import json
            data = json.load(f)
        
        # Get title and create valid filename
        title = data['title']
        valid_title = re.sub(r'[<>:"/\\|?*]', "", title)
        output_dir = path_folder
        output_path = os.path.join(output_dir, f'{valid_title}.pdf')
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Initialize PDF merger
        merger = PdfMerger()
        
        # List of PDF files in order: copyright, contents, chapters (1.pdf, 2.pdf, ...)
        pdf_files = ['copyright.pdf', 'contents.pdf']
        
        # Add chapter PDFs (1.pdf, 2.pdf, ...)
        chapter_files = sorted(
            [f for f in os.listdir(path_folder) if f.endswith('.pdf') and f not in pdf_files and f.split('.')[0].isdigit()],
            key=lambda x: int(x.split('.')[0])
        )
        pdf_files.extend(chapter_files)
        
        # Check if all required files exist
        for pdf_file in pdf_files:
            pdf_path = os.path.join(path_folder, pdf_file)
            if not os.path.exists(pdf_path):
                print(f"Error: {pdf_file} not found in {path_folder}")
                return False, []
            
            # Append PDF to merger
            merger.append(pdf_path)
        
        # Write merged PDF to output file
        with open(output_path, 'wb') as fout:
            merger.write(fout)
        
        print(f"Book created successfully: {output_path}")
        return True, pdf_files  # Return success status and list of source PDFs
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return False, []
    finally:
        if merger:
            merger.close()

def delete_source_pdfs(path_folder, pdf_files):
    """
    Delete source PDF files after they have been merged into a single book.
    
    Args:
        path_folder (str): Path to the folder containing the PDFs.
        pdf_files (list): List of PDF files to delete.
        
    Returns:
        None
    """
    try:
        for pdf_file in pdf_files:
            pdf_path = os.path.join(path_folder, pdf_file)
            if os.path.exists(pdf_path):
                try:
                    os.remove(pdf_path)
                    print(f"Successfully deleted {pdf_path}")
                except Exception as e:
                    print(f"Error deleting {pdf_path}: {str(e)}")
            else:
                print(f"File {pdf_path} does not exist")
    except Exception as e:
        print(f"Error occurred during deletion: {str(e)}") 