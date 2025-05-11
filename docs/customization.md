<!-- Copyright (c) 2025 Swaraj Puppalwar (UltronTheAI) -->
<!-- Licensed under the MIT License. See LICENSE file in the project root for full license information. -->
<!-- Project: https://github.com/UltronTheAI/eBook-Generator-AI-Agent -->

# Customization Guide

This guide explains how to customize various aspects of the eBook Generator AI Agent to suit your specific needs.

## Customizing eBook Prompts

The easiest way to customize the eBook Generator is to modify the prompts used for generation.

### Modifying Existing Prompts

Edit the `prompts` list in `app.py` or `main.py`:

```python
prompts = [
    "Write a book about 'Your Custom Topic 1' under 25 pages",
    "Write a book about 'Your Custom Topic 2'",
    # Add more custom prompts here
]
```

### Prompt Format Guidelines

For best results, follow these guidelines when creating prompts:

1. **Basic Format**: `Write a book about 'Topic'`
2. **Length Control**: Add `under X pages` to control the length
3. **Specificity**: More specific prompts yield better results
4. **Genre Guidance**: Include genre information for appropriate styling

Examples:
- `Write a book about 'Digital Marketing for Small Businesses' under 30 pages`
- `Write a book about 'Mediterranean Cooking for Beginners' with 15 recipes`
- `Write a book about 'Fantasy World Building' in the style of a creative guide`

## Customizing Cover Templates

### Adding New Cover Templates

1. Create a new SVG file with your design
2. Save it in the `Templates` directory with a numeric name (e.g., `11.svg`)
3. Ensure your SVG contains the text "Your Title Here" and "Author Name" as placeholders

### Modifying Existing Templates

Edit the SVG files in the `Templates` directory:

1. Open the desired SVG file (e.g., `1.svg`) in a text editor or SVG editor
2. Modify the design while keeping the placeholder text
3. Save the file with the same name

### Cover Generation Parameters

You can customize the cover generation by modifying the `generate_cover_svg` function call:

```python
# Custom cover generation
cover_svg = generate_cover_svg(
    title="Your Custom Title",
    author="Your Name",
    Custom_Prompt="Use bright colors and a minimalist design"
)
```

## Customizing PDF Output

### Font Size

Modify the font size parameter in the `generate_pdf` function:

```python
# Larger font for better readability
generate_pdf(content, output_path, font_size=24)

# Smaller font to fit more content
generate_pdf(content, output_path, font_size=18)
```

### PDF Styling

To customize the PDF styling, modify the HTML template in the `generate_pdf` function in `pdf_generator.py`:

```python
styled_html = f"""
<html>
<head>
    <style>
        body {{
            font-size: {font_size};
            margin: 0;
            padding: 20mm;
            text-align: justify;
            font-family: 'Your Preferred Font', serif; /* Custom font */
            color: #333; /* Custom text color */
        }}
        h1 {{
            text-align: center;
            font-size: {font_size+4};
            color: #0066cc; /* Custom heading color */
        }}
        p {{
            line-height: 1.6;
        }}
        /* Add more custom CSS here */
    </style>
</head>
<body>
    {html_content}
</body>
</html>
"""
```

### Page Size

To change the page size, modify the options in the `generate_pdf` function:

```python
options = {
    "page-size": "Letter",  # Change from A4 to Letter
    # Other options...
}
```

Common page sizes:
- A4: 210 x 297 mm (default)
- Letter: 8.5 x 11 inches
- A5: 148 x 210 mm
- B5: 176 x 250 mm

## Customizing AI Behavior

### Model Selection

To use different AI models, modify the model names in the `content_generator.py` file:

```python
# Change from gemini-1.5-flash to a different model
head = client.chats.create(model="gemini-1.5-pro")  # Example of using a different model
```

### AI Instructions

To customize the AI's behavior, modify the instructions sent to the models:

```python
# Customize the Head's instructions
head.send_message("Your Name is Head or Mr. Jake Thompson. You are the head of an editorial team creating a technical manual. Focus on clear explanations and include code examples where appropriate...")
```

### Response Formatting

To customize how the AI structures its responses, modify the Pydantic models in `models.py`:

```python
# Add a new field to capture additional information
class ChapterWithExamples(BaseModel):
    title: str
    content: str
    pages: int
    examples: List[str]  # New field for examples
```

## Customizing Output Directory Structure

### Output Base Directory

To change where eBooks are saved, modify the `base_dir` parameter in `create_valid_folder`:

```python
# Change from "book" to a custom directory
path_folder = create_valid_folder(data['title'], base_dir="my_ebooks")
```

### File Naming

To customize how files are named, modify the relevant sections in `main.py` or `app.py`:

```python
# Custom file naming pattern
output_path = os.path.join(path_folder, f"chapter_{c}_{data['title']}.pdf")
```

## Advanced Customizations

### Adding New Features

To add new features, create new functions in the appropriate modules:

```python
# Add to pdf_generator.py
def generate_pdf_with_toc(content, output_path, toc_title="Table of Contents"):
    """Generate a PDF with an automatic table of contents."""
    # Implementation...
```

### Customizing the Workflow

To customize the overall workflow, modify the `create_ebook` function in `main.py`:

```python
def create_ebook(prompt, include_cover=True, include_toc=True):
    """
    Create an eBook with customizable components.
    
    Args:
        prompt (str): The prompt for the eBook
        include_cover (bool): Whether to include a cover
        include_toc (bool): Whether to include a table of contents
    """
    # Modified implementation...
```

### Creating Custom Templates

For more extensive customization, create template files for different types of eBooks:

1. Create a `templates` directory
2. Add template files (e.g., `novel_template.md`, `technical_guide_template.md`)
3. Modify the content generation to use these templates

## Example: Creating a Custom eBook Type

Here's an example of creating a custom recipe book generator:

```python
def create_recipe_book(cuisine, num_recipes=10):
    """
    Create a recipe book for a specific cuisine.
    
    Args:
        cuisine (str): Type of cuisine (e.g., "Italian", "Thai")
        num_recipes (int): Number of recipes to include
    """
    prompt = f"Write a recipe book about '{cuisine} Cooking' with {num_recipes} recipes"
    data = generate_ebook_idea(prompt)
    
    # Custom processing for recipes
    # ...
    
    return create_ebook(prompt)
``` 