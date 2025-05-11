<!-- Copyright (c) 2025 Swaraj Puppalwar (UltronTheAI) -->
<!-- Licensed under the MIT License. See LICENSE file in the project root for full license information. -->
<!-- Project: https://github.com/UltronTheAI/eBook-Generator-AI-Agent -->

# Architecture

This document describes the architecture of the eBook Generator AI Agent, explaining how the different components work together.

## High-Level Architecture

The eBook Generator is built with a modular architecture that separates concerns into distinct components:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│  Content        │────▶│  PDF            │────▶│  Assembly       │
│  Generation     │     │  Generation     │     │  & Output       │
│                 │     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
        ▲                        ▲                      ▲
        │                        │                      │
        │                        │                      │
        │                        │                      │
┌───────┴────────────────────────┴──────────────────────┴───────┐
│                                                               │
│                       Utility Functions                       │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

## Component Breakdown

### 1. Entry Points

- **app.py**: Main application entry point that orchestrates the entire eBook generation process
- **run.py**: Alternative entry point that imports from the main module

### 2. Core Modules

#### Content Generation (`content_generator.py`)

This module handles all AI-powered content generation using Google's Gemini models:

- **generate_ebook_idea()**: Creates the initial eBook concept, title, and structure
- **generate_ebook_content()**: Generates the actual content for each chapter
- **generate_content_page()**: Creates the table of contents
- **generate_cover_svg()**: Generates the eBook cover design

#### PDF Generation (`pdf_generator.py`)

This module handles the conversion from markdown to PDF:

- **generate_pdf()**: Converts markdown content to formatted PDF
- **create_book_pdf()**: Merges individual PDF files into a complete eBook
- **delete_source_pdfs()**: Cleans up intermediate PDF files

#### Utilities (`utils.py`)

This module provides helper functions:

- **convert_svg_to_png()**: Converts SVG covers to PNG format
- **convert_png_to_jpg()**: Converts PNG images to JPG format
- **create_valid_folder()**: Creates folders with sanitized names
- **copy_copyright_file()**: Handles copyright page inclusion
- **delete_file()**: Manages file deletion

#### Data Models (`models.py`)

This module defines the data structures used throughout the application:

- **Chapter**: Represents a book chapter with title, content, and page count
- **FinalRecipe**: Represents the complete eBook structure
- **Various AI response models**: Define the expected response formats from the AI

### 3. Main Workflow (`main.py`)

This module implements the core workflow:

- **create_ebook()**: Orchestrates the entire eBook creation process
- **main()**: Entry point that processes a list of prompts

## Data Flow

1. **Prompt Input**: The process begins with a text prompt describing the desired eBook
2. **Idea Generation**: The prompt is sent to the Gemini AI to generate an eBook concept
3. **Content Generation**: The AI generates detailed content for each chapter
4. **Markdown to PDF**: The markdown content is converted to formatted PDF files
5. **PDF Assembly**: Individual PDFs are merged into a complete eBook
6. **Cover Generation**: A cover is created and converted to image formats
7. **Output**: The final eBook and associated files are saved to the output directory

## AI Collaboration Pattern

The system uses a unique "collaborative AI" pattern where multiple AI agents work together:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│  Head           │────▶│  Thinkers       │────▶│  Final          │
│  (Coordinator)  │     │  (Collaborators)│     │  Decision       │
│                 │     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

1. A "Head" AI agent coordinates the process
2. Multiple "Thinker" agents collaborate on ideas
3. For content generation, specialized roles (Writer, Fact Checker, Suggester) work together
4. The Head makes final decisions based on the collaborative input

## Key Design Principles

1. **Modularity**: The system is divided into focused modules with clear responsibilities
2. **Separation of Concerns**: Content generation, PDF creation, and utilities are separated
3. **Data-Driven**: Structured data models define the flow between components
4. **AI Collaboration**: Multiple AI agents collaborate to improve quality
5. **Error Handling**: Each component includes error handling to ensure robustness

## Dependencies

- **Google Generative AI**: For AI content generation
- **Pydantic**: For data validation and settings management
- **pdfkit/wkhtmltopdf**: For PDF generation
- **PyPDF2**: For PDF manipulation
- **cairosvg/Pillow**: For image processing 