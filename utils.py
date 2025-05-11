# Copyright (c) 2025 Swaraj Puppalwar (UltronTheAI)
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
# Project: https://github.com/UltronTheAI/eBook-Generator-AI-Agent
import os
import re
import shutil
from cairosvg import svg2png
from PIL import Image

def convert_svg_to_png(svg_path, output_path=None):
    """
    Convert an SVG file to PNG format.
    
    Args:
        svg_path (str): Path to the SVG file.
        output_path (str, optional): Path for the output PNG file. If None, will be derived from svg_path.
        
    Returns:
        None
    """
    try:
        # If output_path is not provided, generate it from svg_path
        if output_path is None:
            output_path = os.path.splitext(svg_path)[0] + '.png'
        
        # Check if SVG file exists
        if not os.path.exists(svg_path):
            print(f"Error: SVG file {svg_path} does not exist")
            return
        
        # Convert SVG to PNG
        svg2png(url=svg_path, write_to=output_path)
        print(f"Successfully converted {svg_path} to {output_path}")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")

def convert_png_to_jpg(png_path, output_path=None, size=(500, 700)):
    """
    Convert a PNG file to JPG format and resize it.
    
    Args:
        png_path (str): Path to the PNG file.
        output_path (str, optional): Path for the output JPG file. If None, will be derived from png_path.
        size (tuple, optional): Size to resize the image to. Default is (500, 700).
        
    Returns:
        None
    """
    try:
        # If output_path is not provided, generate it from png_path
        if output_path is None:
            output_path = os.path.splitext(png_path)[0] + '.jpg'
        
        # Check if PNG file exists
        if not os.path.exists(png_path):
            print(f"Error: PNG file {png_path} does not exist")
            return
        
        # Open the PNG image
        with Image.open(png_path) as img:
            # Convert to RGB (JPG doesn't support transparency)
            if img.mode in ('RGBA', 'LA'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[-1])
                img = background
            else:
                img = img.convert('RGB')
            
            # Resize to specified size
            img = img.resize(size, Image.LANCZOS)
            
            # Save as JPG
            img.save(output_path, 'JPEG', quality=95)
            print(f"Successfully converted {png_path} to {output_path} with size {size[0]}x{size[1]}")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")

def create_valid_folder(title, base_dir="book"):
    """
    Creates a folder with a sanitized title, ensuring compatibility with Windows.

    Args:
        title (str): The original folder name.
        base_dir (str, optional): The base directory where the folder will be created. Default is "book".
        
    Returns:
        str: The path of the created folder.
    """
    # Remove invalid characters for Windows folder names
    valid_title = re.sub(r'[<>:"/\\|?*]', "", title)

    # Construct the folder path
    folder_path = os.path.join(base_dir, valid_title)

    # Create the folder, ensuring it exists
    os.makedirs(folder_path, exist_ok=True)

    print(f"Folder created: {folder_path}")
    return folder_path

def copy_copyright_file(path_folder):
    """
    Copy the copyright.pdf file to the specified folder.
    
    Args:
        path_folder (str): Path to the destination folder.
        
    Returns:
        None
    """
    source_file = "./copyright.pdf"
    destination_file = os.path.join(path_folder, "copyright.pdf")
    
    try:
        # Check if source file exists
        if not os.path.exists(source_file):
            print(f"Error: Source file {source_file} does not exist")
            return
        
        # Create destination folder if it doesn't exist
        os.makedirs(path_folder, exist_ok=True)
        
        # Copy the file
        shutil.copy2(source_file, destination_file)
        print(f"File copied successfully to {destination_file}")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")

def delete_file(file_path):
    """
    Delete a file at the specified path.
    
    Args:
        file_path (str): Path to the file to be deleted.
        
    Returns:
        None
    """
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"Error: File {file_path} does not exist")
            return
        
        # Delete the file
        os.remove(file_path)
        print(f"Successfully deleted {file_path}")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}") 