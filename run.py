# Copyright (c) 2025 Swaraj Puppalwar (UltronTheAI)
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
# Project: https://github.com/UltronTheAI/eBook-Generator-AI-Agent
#!/usr/bin/env python
"""
PDF Creator - Entry point for the application.

This script serves as the entry point for the PDF Creator application.
It allows users to generate eBooks with AI-generated content.
"""

import sys
import os

# Add the parent directory to the path so we can import the PDF package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PDF.main import main

if __name__ == "__main__":
    main() 