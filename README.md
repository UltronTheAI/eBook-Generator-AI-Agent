<!-- Copyright (c) 2025 Swaraj Puppalwar (UltronTheAI) -->
<!-- Licensed under the MIT License. See LICENSE file in the project root for full license information. -->
<!-- Project: https://github.com/UltronTheAI/eBook-Generator-AI-Agent -->

# eBook Generator AI Agent

![eBook Generator](https://img.shields.io/badge/eBook-Generator-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![Gemini AI](https://img.shields.io/badge/Gemini-AI-orange)

An AI-powered system for generating complete eBooks from simple prompts. This tool uses Google's Gemini AI models to create professional-quality eBooks with minimal human input.

## Features

- 📚 **Complete eBook Generation**: Creates full eBooks including content, covers, and formatting
- 🤖 **AI-Powered Content**: Uses Google's Gemini AI models for high-quality content
- 🎨 **Automated Cover Design**: Generates custom covers for each eBook
- 📄 **PDF Output**: Produces professionally formatted PDF eBooks
- ⚙️ **Customizable**: Adjust prompts, templates, and formatting to your needs

## Quick Start

1. Clone the repository
2. Install dependencies: `pip install -r PDF/requirements.txt`
3. Set up your Gemini API key in `.env`
4. Run the generator: `python -m PDF.run`

## Example Output

The system generates complete eBooks on topics like:
- Productivity guides
- Technical manuals
- Self-help books
- Fiction stories
- Educational content

Each eBook includes:
- Professional cover
- Table of contents
- Multiple chapters
- Consistent formatting

## Documentation

Detailed documentation is available in the `PDF/docs` directory:

- [Installation Guide](docs/installation.md)
- [Usage Guide](docs/usage.md)
- [Architecture](docs/architecture.md)
- [Module Reference](docs/module_reference.md)
- [AI Models](docs/ai_models.md)
- [Customization](docs/customization.md)
- [Troubleshooting](docs/troubleshooting.md)

## Requirements

- Python 3.8+
- Google Gemini API key
- wkhtmltopdf (for PDF generation)
- Dependencies listed in `PDF/requirements.txt`

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Gemini AI for providing the AI models
- The open-source community for various libraries used in this project 
