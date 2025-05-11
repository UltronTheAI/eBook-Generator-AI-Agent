<!-- Copyright (c) 2025 Swaraj Puppalwar (UltronTheAI) -->
<!-- Licensed under the MIT License. See LICENSE file in the project root for full license information. -->
<!-- Project: https://github.com/UltronTheAI/eBook-Generator-AI-Agent -->

# eBook Generator AI Agent

## Overview

The eBook Generator AI Agent is an automated system for creating high-quality eBooks using AI. It leverages Google's Gemini AI models to generate eBook content, covers, and formatting, producing complete PDF eBooks based on simple prompts. While the content generation is automated, the process requires user interaction to proceed between each eBook.

## Features

- **AI-Powered Content Generation**: Uses Gemini AI models to create well-structured eBook content
- **Automated Cover Design**: Generates eBook covers using SVG templates
- **PDF Generation**: Converts markdown content to formatted PDF files
- **Complete eBook Assembly**: Combines chapters, table of contents, and copyright information into a single PDF
- **Customizable Prompts**: Create eBooks on any topic with simple text prompts
- **Interactive Process**: User confirms each eBook generation by pressing Enter

## Project Structure

```
PDF/
├── app.py                  # Main application entry point
├── run.py                  # Alternative entry point script
├── __init__.py             # Package initialization
├── main.py                 # Main workflow implementation
├── content_generator.py    # AI content generation functions
├── pdf_generator.py        # PDF creation and manipulation
├── utils.py                # Utility functions
├── models.py               # Data models
├── book/                   # Output directory for generated books
├── Templates/              # SVG templates for book covers
├── copyright.pdf           # Copyright page template
└── .env                    # Environment variables
```

## Getting Started

See the [Installation Guide](installation.md) for setup instructions and the [Usage Guide](usage.md) for how to use the application.

## Documentation

- [Installation Guide](installation.md)
- [Usage Guide](usage.md)
- [Architecture](architecture.md)
- [Module Reference](module_reference.md)
- [AI Models](ai_models.md)
- [Customization](customization.md)
- [Troubleshooting](troubleshooting.md)

## Requirements

- Python 3.8+
- Google Gemini API key
- pdfkit
- wkhtmltopdf
- Other dependencies listed in requirements.txt

## License

This project is licensed under the MIT License - see the LICENSE file for details. 