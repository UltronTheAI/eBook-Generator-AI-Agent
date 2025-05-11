# Copyright (c) 2025 Swaraj Puppalwar (UltronTheAI)
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
# Project: https://github.com/UltronTheAI/eBook-Generator-AI-Agent
from pydantic import BaseModel
from typing import List

# Models for ebook idea generation
class Chapter(BaseModel):
    title: str
    content: str
    pages: int

class FinalRecipe(BaseModel):
    title: str
    contents: List[Chapter]
    Totalpages: int

class HeadRecipe(BaseModel):
    response: str
    isBookIdeaConformed: bool = False

class ThinkerRecipe(BaseModel):
    response: str

# Models for cover generation
class CoverHeadRecipe(BaseModel):
    response: str
    selected_template: str

class ConfigRecipe(BaseModel):
    title: str
    author: str

class CoverPageRecipe(BaseModel):
    svg_content: str

# Models for ebook content generation
class eBookRecipe(BaseModel):
    response: str

class eBookRecipPages(BaseModel):
    page_markdown: str

class eBookRecipPage(BaseModel):
    chapter_markdown: List[eBookRecipPages]
    response: str

# Model for content page generation
class ContentPageSchema(BaseModel):
    markdown: str 