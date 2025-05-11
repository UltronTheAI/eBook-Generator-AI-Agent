<!-- Copyright (c) 2025 Swaraj Puppalwar (UltronTheAI) -->
<!-- Licensed under the MIT License. See LICENSE file in the project root for full license information. -->
<!-- Project: https://github.com/UltronTheAI/eBook-Generator-AI-Agent -->

# Installation Guide

This guide will walk you through the process of setting up the eBook Generator AI Agent on your system.

## Prerequisites

Before installing the eBook Generator, ensure you have the following prerequisites:

1. **Python 3.8+**: The application requires Python 3.8 or newer.
2. **Google Gemini API Key**: You'll need an API key from Google's AI Studio to access the Gemini models.
3. **wkhtmltopdf**: Required for PDF generation.

## Step 1: Clone the Repository

```bash
git clone <repository-url>
cd eBook-Generator-AI-Agent
```

## Step 2: Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Key Dependencies

- **google-generativeai**: Google's Generative AI client library
- **pydantic**: For data validation and settings management
- **pdfkit**: For PDF generation from HTML
- **markdown**: For converting markdown to HTML
- **PyPDF2**: For PDF manipulation
- **cairosvg**: For SVG to PNG conversion
- **Pillow**: For image processing

## Step 4: Install wkhtmltopdf

The PDF generation relies on wkhtmltopdf, which needs to be installed separately:

### Windows
1. Download the installer from [wkhtmltopdf downloads](https://wkhtmltopdf.org/downloads.html)
2. Run the installer and follow the instructions
3. Add the installation directory to your PATH environment variable

### macOS
```bash
brew install wkhtmltopdf
```

### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install wkhtmltopdf
```

## Step 5: Set Up Environment Variables

Create a `.env` file in the root directory with your Google Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

To obtain a Gemini API key:
1. Go to [Google AI Studio](https://makersuite.google.com/)
2. Sign in with your Google account
3. Navigate to the API Keys section
4. Create a new API key

## Step 6: Verify Installation

To verify that everything is set up correctly, run:

```bash
python app.py
```

You should see a prompt asking you to press Enter to continue with the first eBook generation.

## Troubleshooting

### PDF Generation Issues

If you encounter issues with PDF generation:
- Ensure wkhtmltopdf is properly installed and accessible in your PATH
- Check that you have write permissions in the output directory

### API Key Issues

If you see authentication errors:
- Verify your API key is correct in the .env file
- Ensure the .env file is in the correct location
- Check that your API key has not expired or been revoked

### Dependencies Issues

If you encounter errors related to dependencies:
```bash
pip install --upgrade -r requirements.txt
```

For more detailed troubleshooting, refer to the [Troubleshooting Guide](troubleshooting.md). 