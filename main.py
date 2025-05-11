# Copyright (c) 2025 Swaraj Puppalwar (UltronTheAI)
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
# Project: https://github.com/UltronTheAI/eBook-Generator-AI-Agent
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import modules
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

# List of book prompts
prompts = [
    "Write a book about 'Mastering ChatGPT for Productivity' under 25 pages",
    "Write a book about 'AI Tools for Small Business Owners' under 25 pages",
    "Write a book about 'Beginner's Guide to Midjourney and AI Art' under 25 pages",
    "Write a book about 'How to Use AI for Job Searching' under 25 pages",
    "Write a book about 'Automating Your Life with AI' under 25 pages",
    "Write a book about 'Creating a Chatbot Without Coding' under 25 pages",
    "Write a book about 'Tech Basics for Seniors' under 25 pages",
    "Write a book about 'Safe Internet Habits in the Age of AI' under 25 pages",
    "Write a book about 'AI in Education: Tools for Teachers' under 25 pages",
    "Write a book about 'Build a No-Code App in One Day' under 25 pages",
    
    "Write a book about '30-Day Budget Fix'",
    "Write a book about 'Side Hustles That Actually Work in 2025'",
    "Write a book about 'Passive Income Through Print-on-Demand'",
    "Write a book about 'Beginner's Guide to Stock Market Investing'",
    "Write a book about 'How to Escape Debt Fast'",
    "Write a book about 'Freelancing for Teens & Students'",
    "Write a book about 'Saving for a Home: A Practical Roadmap'",
    "Write a book about 'AI-Powered Investing Strategies'",
    "Write a book about 'Turning Hobbies Into Income'",
    "Write a book about 'The Psychology of Money for Gen Z'",
    
    "Write a book about 'Atomic Habits in Action: 30 Days of Habit Building'",
    "Write a book about 'Digital Minimalism for the Overwhelmed'",
    "Write a book about 'Deep Focus: Beating Distraction in the AI Age'",
    "Write a book about 'The 5AM Routine Blueprint'",
    "Write a book about 'Dopamine Detox Guide'",
    "Write a book about 'Journaling for Mental Clarity'",
    "Write a book about 'Overcoming Procrastination Step by Step'",
    "Write a book about 'The One-Task Method'",
    "Write a book about 'Self-Discipline for Freelancers'",
    "Write a book about 'Designing a Life You Love (Life Planning Workbook)'",
    
    "Write a book about 'The Anti-Inflammatory Diet Guide'",
    "Write a book about 'Gut Reset in 21 Days'",
    "Write a book about 'Hormone Health for Women 30+'",
    "Write a book about 'Sleep Optimization Hacks'",
    "Write a book about 'Intermittent Fasting Made Simple'",
    "Write a book about 'Natural Anxiety Relief'",
    "Write a book about 'Fitness at Home: No-Equipment Routines'",
    "Write a book about 'Clean Eating on a Budget'",
    "Write a book about 'Longevity Habits from Blue Zones'",
    "Write a book about 'Breathwork for Beginners'",
    
    "Write a book about 'Start Your Freelance Writing Career'",
    "Write a book about '100 Online Jobs You Can Do From Home'",
    "Write a book about 'Digital Nomad Startup Guide'",
    "Write a book about 'Pitching Clients That Pay'",
    "Write a book about 'Upwork Success Blueprint'",
    "Write a book about 'Build Your Personal Brand Online'",
    "Write a book about 'Canva for Freelancers'",
    "Write a book about 'The 4-Hour Workday Routine'",
    "Write a book about 'Creating and Selling Online Courses'",
    "Write a book about 'Time Management for Remote Workers'",
    
    "Write a book about 'Murder at the Tea Shop'",
    "Write a book about 'A Witch's Brew and a Corpse'",
    "Write a book about 'The Knitting Club Killer'",
    "Write a book about 'Paws and Claws: A Pet Detective Mystery'",
    "Write a book about 'Death at the Book Festival'",
    "Write a book about 'Haunted House Homicide'",
    "Write a book about 'A Garden Gnome Whodunit'",
    "Write a book about 'Bakery Secrets & Bloodshed'",
    "Write a book about 'Christmas Crimes in a Small Town'",
    "Write a book about 'Ghosts and Gossip: A Paranormal Cozy Mystery'",
    
    "Write a book about 'Love in the Shadow of the Throne'",
    "Write a book about 'The Cursed Prince's Bride'",
    "Write a book about 'Fated Mates and Forbidden Magic'",
    "Write a book about 'Blood Bond: A Vampire Romance'",
    "Write a book about 'The Dragon's Secret Heiress'",
    "Write a book about 'Ice Queen & Fire King'",
    "Write a book about 'A Court of Hearts and Shadows'",
    "Write a book about 'The Rebellion and the Royal'",
    "Write a book about 'Enchanted Realms: A Love Story'",
    "Write a book about 'Prophecy of the Moon & Star'"
]

def create_ebook(prompt):
    """
    Create an eBook based on the given prompt.
    
    Args:
        prompt (str): Prompt for the eBook idea.
        
    Returns:
        str: Path to the created eBook folder.
    """
    # Generate eBook idea
    data = generate_ebook_idea(prompt)
    
    # Create folder for the eBook
    path_folder = create_valid_folder(data['title'])
    
    # Save eBook data
    with open(f"{path_folder}/data.json", "w") as f:
        json.dump(data, f)
    
    # Generate eBook content
    book_content = generate_ebook_content("eBookAura", data)
    
    # Generate chapter PDFs
    chapter_count = 0
    for chapter in book_content:
        chapter_count += 1
        chapter_content = ""
        for page in chapter:
            chapter_content += page['page_markdown']
        generate_pdf(chapter_content, f"{path_folder}/{chapter_count}.pdf")
    
    # Generate content page
    content_page = generate_content_page(str(book_content), 24)
    generate_pdf(content_page, f"{path_folder}/contents.pdf", 22)
    
    # Copy copyright file
    copy_copyright_file(path_folder)
    
    # Create merged book PDF
    success, pdf_files = create_book_pdf(path_folder)
    if success:
        delete_source_pdfs(path_folder, pdf_files)
    
    # Generate cover
    cover_page_svg_code = generate_cover_svg(data['title'], "eBookAura", str(data))
    with open(f"{path_folder}/cover.svg", "w") as f:
        f.write(cover_page_svg_code)
    
    # Convert cover to PNG and JPG
    convert_svg_to_png(f"{path_folder}/cover.svg", f"{path_folder}/cover.png")
    convert_png_to_jpg(f"{path_folder}/cover.png", f"{path_folder}/cover.jpg")
    
    # Delete intermediate files
    delete_file(f"{path_folder}/cover.svg")
    delete_file(f"{path_folder}/cover.png")
    
    return path_folder

def main():
    """
    Main function to run the eBook creation process.
    """
    for prompt in prompts:
        input("Press Enter to continue...")
        print(f"Creating eBook for prompt: {prompt}")
        path_folder = create_ebook(prompt)
        print(f"eBook created successfully in: {path_folder}")

if __name__ == "__main__":
    main() 