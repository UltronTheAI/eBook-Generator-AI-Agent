# Copyright (c) 2025 Swaraj Puppalwar (UltronTheAI)
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
# Project: https://github.com/UltronTheAI/eBook-Generator-AI-Agent
"""
PDF Creator Package - A tool for generating eBooks in PDF format.

This package provides functionality to generate eBooks with AI-generated content,
create PDF files from markdown, and manage the eBook creation process.
"""

from .utils import (
    convert_svg_to_png,
    convert_png_to_jpg,
    create_valid_folder,
    copy_copyright_file,
    delete_file
)

from .pdf_generator import (
    generate_pdf,
    create_book_pdf,
    delete_source_pdfs
)

from .content_generator import (
    generate_ebook_idea,
    generate_cover_svg,
    generate_ebook_content,
    generate_content_page
)

from .models import (
    Chapter, FinalRecipe,
    HeadRecipe, ThinkerRecipe,
    CoverHeadRecipe, ConfigRecipe, CoverPageRecipe,
    eBookRecipe, eBookRecipPages, eBookRecipPage,
    ContentPageSchema
)

from .main import create_ebook, main

__all__ = [
    'convert_svg_to_png', 'convert_png_to_jpg', 'create_valid_folder',
    'copy_copyright_file', 'delete_file',
    'generate_pdf', 'create_book_pdf', 'delete_source_pdfs',
    'generate_ebook_idea', 'generate_cover_svg', 'generate_ebook_content',
    'generate_content_page',
    'Chapter', 'FinalRecipe', 'HeadRecipe', 'ThinkerRecipe',
    'CoverHeadRecipe', 'ConfigRecipe', 'CoverPageRecipe',
    'eBookRecipe', 'eBookRecipPages', 'eBookRecipPage', 'ContentPageSchema',
    'create_ebook', 'main'
] 