<!-- Copyright (c) 2025 Swaraj Puppalwar (UltronTheAI) -->
<!-- Licensed under the MIT License. See LICENSE file in the project root for full license information. -->
<!-- Project: https://github.com/UltronTheAI/eBook-Generator-AI-Agent -->

# Module Reference

This document provides detailed information about each module in the eBook Generator AI Agent.

## Table of Contents

- [models.py](#modelspy)
- [utils.py](#utilspy)
- [pdf_generator.py](#pdf_generatorpy)
- [content_generator.py](#content_generatorpy)
- [main.py](#mainpy)
- [app.py](#apppy)
- [run.py](#runpy)
- [__init__.py](#__init__py)

## models.py

The `models.py` module defines the data structures used throughout the application using Pydantic models.

### Classes

#### Chapter

Represents a book chapter.

```python
class Chapter(BaseModel):
    title: str       # Chapter title
    content: str     # Brief description of chapter content
    pages: int       # Number of pages allocated to the chapter
```

#### FinalRecipe

Represents the complete eBook structure.

```python
class FinalRecipe(BaseModel):
    title: str               # eBook title
    contents: List[Chapter]  # List of chapters
    Totalpages: int          # Total page count
```

#### HeadRecipe

Response model for the Head AI agent.

```python
class HeadRecipe(BaseModel):
    response: str                     # Text response from the Head
    isBookIdeaConformed: bool = False # Whether the book idea is finalized
```

#### ThinkerRecipe

Response model for the Thinker AI agents.

```python
class ThinkerRecipe(BaseModel):
    response: str  # Text response from the Thinker
```

#### CoverHeadRecipe

Response model for the cover design Head AI agent.

```python
class CoverHeadRecipe(BaseModel):
    response: str           # Text response from the Head
    selected_template: str  # Selected cover template ID
```

#### ConfigRecipe

Model for title and author configuration.

```python
class ConfigRecipe(BaseModel):
    title: str   # Shortened title for the cover
    author: str  # Author name for the cover
```

#### eBookRecipe, eBookRecipPages, eBookRecipPage

Models for eBook content generation responses.

```python
class eBookRecipe(BaseModel):
    response: str  # Text response from the AI

class eBookRecipPages(BaseModel):
    page_markdown: str  # Markdown content for a page

class eBookRecipPage(BaseModel):
    chapter_markdown: List[eBookRecipPages]  # List of pages in a chapter
    response: str                           # Text response from the AI
```

#### ContentPageSchema

Model for the table of contents page.

```python
class ContentPageSchema(BaseModel):
    markdown: str  # Markdown content for the table of contents
```

## utils.py

The `utils.py` module provides utility functions for file operations and image conversions.

### Functions

#### convert_svg_to_png

```python
def convert_svg_to_png(svg_path, output_path=None)
```

Converts an SVG file to PNG format.

**Parameters:**
- `svg_path` (str): Path to the SVG file
- `output_path` (str, optional): Path for the output PNG file

#### convert_png_to_jpg

```python
def convert_png_to_jpg(png_path, output_path=None, size=(500, 700))
```

Converts a PNG file to JPG format and resizes it.

**Parameters:**
- `png_path` (str): Path to the PNG file
- `output_path` (str, optional): Path for the output JPG file
- `size` (tuple, optional): Size to resize the image to (default: (500, 700))

#### create_valid_folder

```python
def create_valid_folder(title, base_dir="book")
```

Creates a folder with a sanitized title.

**Parameters:**
- `title` (str): The original folder name
- `base_dir` (str, optional): The base directory (default: "book")

**Returns:**
- `str`: Path to the created folder

#### copy_copyright_file

```python
def copy_copyright_file(path_folder)
```

Copies the copyright.pdf file to the specified folder.

**Parameters:**
- `path_folder` (str): Path to the destination folder

#### delete_file

```python
def delete_file(file_path)
```

Deletes a file at the specified path.

**Parameters:**
- `file_path` (str): Path to the file to be deleted

## pdf_generator.py

The `pdf_generator.py` module handles PDF generation and manipulation.

### Functions

#### generate_pdf

```python
def generate_pdf(content, output_path, font_size=20)
```

Converts Markdown content into a formatted PDF.

**Parameters:**
- `content` (str): Markdown content to convert to PDF
- `output_path` (str): Path for the output PDF file
- `font_size` (int, optional): Font size for the PDF (default: 20)

#### create_book_pdf

```python
def create_book_pdf(path_folder)
```

Merges individual chapter PDFs into a single book PDF.

**Parameters:**
- `path_folder` (str): Path to the folder containing the PDFs to merge

**Returns:**
- `tuple`: (success (bool), list of source PDF files)

#### delete_source_pdfs

```python
def delete_source_pdfs(path_folder, pdf_files)
```

Deletes source PDF files after they have been merged into a single book.

**Parameters:**
- `path_folder` (str): Path to the folder containing the PDFs
- `pdf_files` (list): List of PDF files to delete

## content_generator.py

The `content_generator.py` module handles AI content generation.

### Functions

#### generate_ebook_idea

```python
def generate_ebook_idea(Custom_Prompt="")
```

Generates an eBook idea with title, content, and page distribution.

**Parameters:**
- `Custom_Prompt` (str, optional): Custom prompt for the eBook idea

**Returns:**
- `dict`: The final eBook idea with title, contents, and total pages

#### generate_cover_svg

```python
def generate_cover_svg(title, author, Custom_Prompt="")
```

Generates an SVG cover for the eBook.

**Parameters:**
- `title` (str): Title of the eBook
- `author` (str): Author of the eBook
- `Custom_Prompt` (str, optional): Custom prompt for cover generation

**Returns:**
- `str`: SVG content for the cover

#### generate_ebook_content

```python
def generate_ebook_content(author, data, Custom_Prompt="")
```

Generates the content for each chapter of the eBook.

**Parameters:**
- `author` (str): Author of the eBook
- `data` (dict): Data structure containing eBook details
- `Custom_Prompt` (str, optional): Custom prompt for content generation

**Returns:**
- `list`: List of chapter markdown content

#### generate_content_page

```python
def generate_content_page(prompt, font_size=20)
```

Generates the table of contents page in markdown format.

**Parameters:**
- `prompt` (str): Prompt for content page generation
- `font_size` (int, optional): Font size for the content page (default: 20)

**Returns:**
- `str`: Markdown content for the table of contents

## main.py

The `main.py` module implements the core workflow of the eBook Generator.

### Functions

#### create_ebook

```python
def create_ebook(prompt)
```

Creates an eBook based on the given prompt.

**Parameters:**
- `prompt` (str): Prompt for the eBook idea

**Returns:**
- `str`: Path to the created eBook folder

#### main

```python
def main()
```

Main function to run the eBook creation process for all prompts.

## app.py

The `app.py` module serves as the main entry point for the application.

### Components

- **Imports**: Imports necessary modules and functions
- **Prompts List**: Contains predefined prompts for eBook generation
- **Main Function**: Orchestrates the eBook generation process

## run.py

The `run.py` module provides an alternative entry point for the application.

### Components

- **Imports**: Imports the main function from the main module
- **Entry Point**: Calls the main function when the script is run directly

## __init__.py

The `__init__.py` module makes the directory a proper Python package and exports necessary components.

### Components

- **Imports**: Imports all functions and classes from the various modules
- **Exports**: Exports these components via the `__all__` list 