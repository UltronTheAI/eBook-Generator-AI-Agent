<!-- Copyright (c) 2025 Swaraj Puppalwar (UltronTheAI) -->
<!-- Licensed under the MIT License. See LICENSE file in the project root for full license information. -->
<!-- Project: https://github.com/UltronTheAI/eBook-Generator-AI-Agent -->

# Usage Guide

This guide explains how to use the eBook Generator AI Agent to create eBooks from simple prompts.

## Basic Usage

To run the eBook Generator:

```bash
python app.py
```

This will start the eBook generation process using the predefined prompts in the system. **Note: The process is interactive and will prompt you to press Enter between generating each eBook.**

## Creating a Custom eBook

To create a custom eBook with your own prompt:

1. Import the necessary components in your Python script:

```python
from PDF import create_ebook

# Generate an eBook with a custom prompt
path = create_ebook("Write a book about 'Your Custom Topic' under 25 pages")
print(f"eBook created successfully at: {path}")
```

## Understanding the Process

When you run the eBook Generator, it follows these steps:

1. **Idea Generation**: The AI generates a book concept based on your prompt
2. **Content Planning**: The AI creates a detailed outline with chapters and page allocations
3. **Content Generation**: Each chapter is written by the AI in markdown format
4. **PDF Creation**: The markdown content is converted to formatted PDF files
5. **Assembly**: All chapters, table of contents, and copyright information are combined into a single PDF
6. **Cover Generation**: A cover is created and converted to PNG and JPG formats

**Important: The process is not fully automated.** You will be prompted to press Enter between generating each eBook. This allows you to review the output of each eBook before proceeding to the next one.

## Customizing Prompts

The default prompts are stored in the `prompts` list in `app.py`. You can modify this list to include your own prompts:

```python
prompts = [
    "Write a book about 'Your Topic 1' under 25 pages",
    "Write a book about 'Your Topic 2'",
    # Add more prompts here
]
```

### Prompt Format

The recommended prompt format is:

```
Write a book about 'Topic' [under X pages]
```

The "under X pages" part is optional and helps control the length of the generated eBook.

## Output Files

For each eBook, the following files are generated in the `book/[Title]` directory:

- **[Title].pdf**: The final eBook as a single PDF
- **cover.jpg**: The eBook cover image
- **data.json**: JSON file containing the eBook structure and metadata

## Batch Processing

To process a batch of eBooks:

1. Add your prompts to the `prompts` list in `app.py`
2. Run the application
3. Press Enter when prompted to generate each eBook

## Advanced Usage

### Customizing the eBook Generation

You can customize various aspects of the eBook generation by modifying the parameters in the function calls:

```python
from PDF import generate_ebook_idea, generate_ebook_content, generate_pdf

# Custom eBook idea generation
data = generate_ebook_idea("Write a book about 'Advanced Topic'")

# Custom author name
book_content = generate_ebook_content("Your Name", data)

# Custom font size
generate_pdf(content, output_path, font_size=24)
```

### Working with Generated Content

The generated content is returned as structured data that you can manipulate:

```python
# Get the generated content
book_content = generate_ebook_content("Author Name", data)

# Access specific chapters
first_chapter = book_content[0]

# Access specific pages
first_page = first_chapter[0]['page_markdown']

# Modify content before PDF generation
modified_content = first_page.replace("Original Text", "Modified Text")
```

## Tips for Best Results

1. **Be Specific**: The more specific your prompt, the better the results
2. **Specify Length**: Include "under X pages" in your prompt to control length
3. **Topic Expertise**: The AI performs best on educational and informational topics
4. **Review Output**: Always review the generated content for accuracy
5. **Iterative Approach**: Use the output as a starting point and refine as needed 