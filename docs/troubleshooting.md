<!-- Copyright (c) 2025 Swaraj Puppalwar (UltronTheAI) -->
<!-- Licensed under the MIT License. See LICENSE file in the project root for full license information. -->
<!-- Project: https://github.com/UltronTheAI/eBook-Generator-AI-Agent -->

# Troubleshooting Guide

This guide provides solutions for common issues you might encounter when using the eBook Generator AI Agent.

## API and Authentication Issues

### API Key Not Working

**Symptoms:**
- Error messages about invalid API key
- Authentication failures

**Solutions:**
1. Verify your API key in the `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
2. Ensure the `.env` file is in the correct location (root directory)
3. Check that your API key is still valid in the Google AI Studio
4. Try generating a new API key if the issue persists

### API Rate Limits

**Symptoms:**
- Error messages about rate limits
- Generation stopping unexpectedly

**Solutions:**
1. Add delays between API calls:
   ```python
   import time
   time.sleep(2)  # Add a 2-second delay
   ```
2. Reduce the number of concurrent API calls
3. Consider upgrading to a higher API tier if available

## PDF Generation Issues

### PDF Not Generated

**Symptoms:**
- No PDF files created
- Error messages about PDF generation

**Solutions:**
1. Verify wkhtmltopdf is installed correctly:
   ```bash
   wkhtmltopdf --version
   ```
2. Check that the output directory exists and has write permissions
3. Try generating a simple test PDF:
   ```python
   from PDF.pdf_generator import generate_pdf
   generate_pdf("# Test\nThis is a test.", "test.pdf")
   ```

### PDF Formatting Issues

**Symptoms:**
- Text overflowing pages
- Incorrect fonts or styling
- Images not displaying correctly

**Solutions:**
1. Adjust the font size:
   ```python
   generate_pdf(content, output_path, font_size=18)  # Try smaller font
   ```
2. Check the markdown content for syntax errors
3. Verify the HTML template in the `generate_pdf` function
4. Ensure any referenced images exist and are accessible

### PDF Merging Errors

**Symptoms:**
- Error when creating the final book PDF
- Missing chapters in the final PDF

**Solutions:**
1. Check that all individual chapter PDFs exist
2. Verify the PyPDF2 library is installed correctly
3. Try merging PDFs manually for testing:
   ```python
   from PyPDF2 import PdfMerger
   merger = PdfMerger()
   merger.append("chapter1.pdf")
   merger.append("chapter2.pdf")
   merger.write("merged.pdf")
   merger.close()
   ```

## Content Generation Issues

### AI Generating Poor Content

**Symptoms:**
- Low-quality or irrelevant content
- Content not matching the prompt

**Solutions:**
1. Make your prompts more specific:
   ```
   "Write a detailed book about 'Advanced Python Programming Techniques' focusing on performance optimization and design patterns"
   ```
2. Try different AI models by modifying the model names in `content_generator.py`
3. Adjust the AI instructions for better guidance
4. Break down complex topics into smaller chapters

### Content Length Issues

**Symptoms:**
- Content too short or too long
- Uneven chapter lengths

**Solutions:**
1. Specify page count in your prompt:
   ```
   "Write a book about 'Topic' under 20 pages with 4 chapters of equal length"
   ```
2. Modify the AI instructions to emphasize length requirements
3. Post-process the content to adjust length:
   ```python
   # Check content length and request more if needed
   if len(chapter_content) < min_length:
       additional_content = generate_additional_content(...)
       chapter_content += additional_content
   ```

### AI Hallucinations or Factual Errors

**Symptoms:**
- Incorrect information in the content
- Made-up references or statistics

**Solutions:**
1. Emphasize factual accuracy in the prompt:
   ```
   "Write a factually accurate book about 'History of Computing' with verified information only"
   ```
2. Modify the fact checker instructions to be more stringent
3. Implement a post-generation fact verification step
4. Consider using a different AI model with better factual grounding

## Image and Cover Issues

### SVG to PNG Conversion Errors

**Symptoms:**
- Error messages about SVG conversion
- Missing cover images

**Solutions:**
1. Verify cairosvg is installed correctly:
   ```bash
   pip install cairosvg
   ```
2. Check that the SVG templates are valid and accessible
3. Try converting a simple SVG for testing:
   ```python
   from cairosvg import svg2png
   svg2png(url="simple.svg", write_to="test.png")
   ```

### Image Quality Issues

**Symptoms:**
- Blurry or pixelated cover images
- Incorrect image dimensions

**Solutions:**
1. Adjust the image size in `convert_png_to_jpg`:
   ```python
   convert_png_to_jpg(png_path, output_path, size=(800, 1200))  # Higher resolution
   ```
2. Increase the quality parameter:
   ```python
   img.save(output_path, 'JPEG', quality=100)  # Maximum quality
   ```
3. Use higher quality SVG templates

## File and Directory Issues

### Permission Errors

**Symptoms:**
- Access denied errors
- Unable to write to output directory

**Solutions:**
1. Check directory permissions:
   ```bash
   # On Windows
   icacls book
   
   # On macOS/Linux
   ls -la book
   ```
2. Run the application with appropriate permissions
3. Use a different output directory that you have write access to

### Missing Files

**Symptoms:**
- File not found errors
- Missing templates or resources

**Solutions:**
1. Verify all required files exist:
   ```python
   import os
   required_files = ["copyright.pdf", "Templates/1.svg"]
   for file in required_files:
       if not os.path.exists(file):
           print(f"Missing: {file}")
   ```
2. Check file paths and directory structure
3. Restore missing files from backup or repository

## Performance Issues

### Slow Generation

**Symptoms:**
- eBook generation takes too long
- System becomes unresponsive

**Solutions:**
1. Reduce the number of pages or chapters
2. Use faster AI models where appropriate
3. Implement caching for repeated operations
4. Run resource-intensive operations in parallel:
   ```python
   import concurrent.futures
   
   with concurrent.futures.ThreadPoolExecutor() as executor:
       futures = [executor.submit(generate_chapter, i) for i in range(num_chapters)]
       chapters = [future.result() for future in futures]
   ```

### Memory Usage

**Symptoms:**
- Out of memory errors
- System slowdown during generation

**Solutions:**
1. Process chapters one at a time instead of all at once
2. Clear variables that are no longer needed:
   ```python
   import gc
   del large_variable
   gc.collect()
   ```
3. Use streaming responses where possible
4. Monitor memory usage and optimize accordingly

## Miscellaneous Issues

### Dependencies Conflicts

**Symptoms:**
- Import errors
- Version incompatibilities

**Solutions:**
1. Create a dedicated virtual environment
2. Install exact versions of dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Check for conflicting packages:
   ```bash
   pip check
   ```

### Unicode and Encoding Issues

**Symptoms:**
- Strange characters in output
- Encoding errors

**Solutions:**
1. Ensure files are saved with UTF-8 encoding
2. Add explicit encoding when reading/writing files:
   ```python
   with open(file_path, 'w', encoding='utf-8') as f:
       f.write(content)
   ```
3. Handle special characters properly in templates and content

### Unexpected Crashes

**Symptoms:**
- Application crashes without clear error messages
- Inconsistent behavior

**Solutions:**
1. Add comprehensive error handling:
   ```python
   try:
       # Operation that might fail
   except Exception as e:
       print(f"Error: {str(e)}")
       # Graceful fallback
   ```
2. Implement logging for better diagnostics:
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG, filename='ebook_generator.log')
   logging.debug("Detailed information")
   ```
3. Run the application with debug flags enabled 