# Copyright (c) 2025 Swaraj Puppalwar (UltronTheAI)
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
# Project: https://github.com/UltronTheAI/eBook-Generator-AI-Agent
import os
import json
from google import genai
from dotenv import load_dotenv

from .models import (
    HeadRecipe, ThinkerRecipe, FinalRecipe, 
    CoverHeadRecipe, ConfigRecipe, 
    eBookRecipe, eBookRecipPages, eBookRecipPage,
    ContentPageSchema
)

# Load environment variables
load_dotenv()

def generate_ebook_idea(Custom_Prompt=""):
    """
    Generate an eBook idea with title, content, and page distribution.
    
    Args:
        Custom_Prompt (str, optional): Custom prompt for the eBook idea. Default is empty string.
        
    Returns:
        dict: The final eBook idea with title, contents, and total pages.
    """
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    head = client.chats.create(model="gemini-1.5-flash")
    thinker1 = client.chats.create(model="gemini-1.5-flash")
    thinker2 = client.chats.create(model="gemini-1.5-flash")
    thinker3 = client.chats.create(model="gemini-1.5-flash")

    thinks = 0
    isBookIdeaConformed = False
    history = []
    final_response_ = {}

    # Instructions
    head.send_message("You are the head of a thinkers group, working on creating an eBook. Your team will decide the title, content, and page distribution. Once finalized, confirm the details.")
    thinker1.send_message("You are thinker 1, follow the orders of your HEAD.")
    thinker2.send_message("You are thinker 2, follow the orders of your HEAD.")
    thinker3.send_message("You are thinker 3, follow the orders of your HEAD.")

    # Start Task
    head_response = json.loads(head.send_message(f"Now command your thinkers to decide on an eBook topic. {Custom_Prompt}", config={
        "response_mime_type": "application/json",
        "response_schema": HeadRecipe,
    }).text)

    history.append(f"HEAD: {head_response['response']}")
    print(f"HEAD: {head_response['response']}")

    while not isBookIdeaConformed and thinks <= 10:
        thinks += 1
        for thinker in [thinker1, thinker2, thinker3]:
            response = json.loads(thinker.send_message(f'Thinks Remaining: {thinks}/10\nHistory: {history}', config={
                "response_mime_type": "application/json",
                "response_schema": ThinkerRecipe,
            }).text)
            history.append(f"{thinker}: {response['response']}")
            print(f"{thinker}: {response['response']}")

        head_response = json.loads(head.send_message(f'Thinks Remaining: {thinks}/10\nHistory: {history}\n\nConfirm the eBook details if ready, otherwise guide the thinkers further.', config={
            "response_mime_type": "application/json",
            "response_schema": HeadRecipe,
        }).text)

        history.append(f"HEAD: {head_response['response']}")
        print(f"HEAD: {head_response['response']}")
        isBookIdeaConformed = head_response['isBookIdeaConformed']

        if isBookIdeaConformed:
            final_response_ = json.loads(head.send_message(f'Thinks Remaining: {thinks}/10\nHistory: {history}\n\nProvide the final eBook details in JSON format.', config={
                "response_mime_type": "application/json",
                "response_schema": FinalRecipe,
            }).text)
            print(f"Final Response: {final_response_}")
            return final_response_

    final_response_ = json.loads(head.send_message(f'Thinks Remaining: {thinks}/10\nHistory: {history}\n\nForcefully generate the final eBook details.', config={
        "response_mime_type": "application/json",
        "response_schema": FinalRecipe,
    }).text)
    print(f"Final Response: {final_response_}")

    return final_response_

def generate_cover_svg(title, author, Custom_Prompt=""):
    """
    Generate an SVG cover for the eBook.
    
    Args:
        title (str): Title of the eBook.
        author (str): Author of the eBook.
        Custom_Prompt (str, optional): Custom prompt for cover generation. Default is empty string.
        
    Returns:
        str: SVG content for the cover.
    """
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    head = client.chats.create(model="gemini-2.0-flash")

    # Load SVG templates
    templates_dir = "./Templates"
    svg_templates = {str(i): open(os.path.join(templates_dir, f"{i}.svg")).read() for i in range(1, 11)}

    # Instructions
    head.send_message("You are the head of an editorial team, selecting a cover design for a PDF. "
                      "Choose one from the available templates and update it with the given title under 30 characters and author name under 20 characters.")

    # Provide available templates
    head_response = json.loads(head.send_message(
        f"Here are the available SVG cover templates:\n{list(svg_templates.keys())}\n"
        f"Choose one and update its title and author name. {Custom_Prompt}",
        config={"response_mime_type": "application/json", "response_schema": CoverHeadRecipe}
    ).text)

    selected_template = head_response["selected_template"]

    # Provide short title and author strings
    head_response = json.loads(head.send_message(
        f"Title: {title}\nAuthor: {author}\nMax Title Length: 20 characters\nMax Author Length: 15 characters\nProvide the short title and author name in JSON format.",
        config={"response_mime_type": "application/json", "response_schema": ConfigRecipe}
    ).text)

    title = head_response["title"]
    author = head_response["author"]

    # Update SVG template
    updated_svg = svg_templates[selected_template].replace("Your Title Here", title).replace("Author Name", author)

    # Return final SVG
    return updated_svg

def generate_ebook_content(author, data, Custom_Prompt=""):
    """
    Generate the content for each chapter of the eBook.
    
    Args:
        author (str): Author of the eBook.
        data (dict): Data structure containing eBook details.
        Custom_Prompt (str, optional): Custom prompt for content generation. Default is empty string.
        
    Returns:
        list: List of chapter markdown content.
    """
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    head = client.chats.create(model="gemini-2.0-flash")
    
    head.send_message("Your Name is Head or Mr. Jake Thompson. You are the head of an editorial team, creating a PDF eBook. "
                      "You will be given a title, author, and a list of chapters with their titles and content. "
                      "You have a writer that will write the content of the eBook page. "
                      "You have a fact checker that will check the content of the eBook page. "
                      "You have a suggester that will suggest the content of the eBook page. "
                      "You have a 3 employee team that will help you to generate the eBook. You have to only give them tasks and they will do it. "
                      "Generate the entire eBook in Markdown format, ensuring it is well-structured and visually appealing.")
    
    history = []
    headHistory = []
    
    head_response = json.loads(head.send_message(
        f"""Title: {data['title']}\nAuthor: {author}\nChapters: {data['contents']}\nAnalyze the content. """
        , config={
        "response_mime_type": "application/json",
        "response_schema": eBookRecipe,
    }).text)
    print(f"Head Response: {head_response}\n\n")
    headHistory.append(f"HEAD: {head_response['response']}")

    history.append(f"HEAD: {head_response['response']}")
    chapters_markdown = []

    for chapter in data['contents']:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        head = client.chats.create(model="gemini-2.0-flash")
    
        head.send_message("Your Name is Head or Mr. Jake Thompson. You are the head of an editorial team, creating a PDF eBook. "
                        "You will be given a title, author, and a list of chapters with their titles and content. "
                        "You have a writer that will write the content of the eBook page. "
                        "You have a fact checker that will check the content of the eBook page. "
                        "You have a suggester that will suggest the content of the eBook page. "
                        "You have a 3 employee team that will help you to generate the eBook. You have to only give them tasks and they will do it. "
                        "Generate the entire eBook in Markdown format, ensuring it is well-structured and visually appealing.")
                        
        history.append(f"HEAD: {head_response['response']}")
        writer = client.chats.create(model="gemini-2.0-flash")
        fact_checker = client.chats.create(model="gemini-2.0-flash")
        suggester = client.chats.create(model="gemini-2.0-flash")
        
        writer.send_message("Your Name is eBookAura Writer or Mrs. Emily Carter.You are the writer of the eBook. You will be given a title, author, and a list of chapters with their titles and content. "
                      "You have to write the content of the eBook page. "
                      "You have to write the content of the eBook page in Markdown format, ensuring it is well-structured and visually appealing.")
    
        fact_checker.send_message("Your Name is eBookAura Fact Checker or Mr. Brandon Mitchell. You are the fact checker of the eBook. You will be given a title, author, and a list of chapters with their titles and content. "
                        "You have to check the content of the eBook page. "
                        "You have to check the content of the eBook page in Markdown format, ensuring it is well-structured and visually appealing.")
        
        suggester.send_message("Your Name is eBookAura Suggester or Mrs. Sophia Reynolds. You are the suggester of the eBook. You will be given a title, author, and a list of chapters with their titles and content. "
                        "You have to suggest the content of the eBook page. "
                        "You have to suggest the content of the eBook page in Markdown format, ensuring it is well-structured and visually appealing.")
                        
        head_response = json.loads(head.send_message(f"Page Size: A4 and Font Size: 22\nHead History: {headHistory}\nHistory: {history}\nChapter: {chapter['title']}\nContent: {chapter['content']}\nPages: {chapter['pages']}\nYou have to disscuss what to write for this chapter with fact checker and suggester. Now tell them what you think about this chapter, provide them with the content of the chapter to write. ", config={
            "response_mime_type": "application/json",
            "response_schema": eBookRecipPage,
        }).text)

        print(f"Head Response: {head_response}\n\n")
        headHistory.append(f"HEAD: {head_response['response']}")
        
        for i in range(chapter['pages'] + 1):
            suggester_response = json.loads(suggester.send_message(f"Page Size: A4 and Font Size: 22\nPage: {i}/{chapter['pages']}\nHistory: {history}\nChapter: {chapter['title']}\nContent: {chapter['content']}\nMAX_Pages: {chapter['pages']}\nYou have to suggest the content of the eBook page to the writer in Markdown format, ensuring it is well-structured and visually appealing. ", config={
                "response_mime_type": "application/json",
                "response_schema": eBookRecipe,
            }).text)
            print(f"Suggester Response: {suggester_response}\n\n")

            history.append(f"SUGGESTER: {suggester_response['response']}")

            fact_checker_response = json.loads(fact_checker.send_message(f"Page Size: A4 and Font Size: 22\nPage: {i}/{chapter['pages']}\nHistory: {history}\nChapter: {chapter['title']}\nContent: {chapter['content']}\nMAX_Pages: {chapter['pages']}\nYou have to check the content of the eBook page to the fact checker in Markdown format, ensuring it is well-structured and visually appealing. ", config={
                "response_mime_type": "application/json",
                "response_schema": eBookRecipe,
            }).text)
            print(f"Fact Checker Response: {fact_checker_response}\n\n")
            history.append(f"FACT_CHECKER: {fact_checker_response['response']}")
            
            writer_response = json.loads(writer.send_message(f"Page Size: A4 and Font Size: 22\nPage: {i}/{chapter['pages']}\nHistory: {history}\nChapter: {chapter['title']}\nContent: {chapter['content']}\nMAX_Pages: {chapter['pages']}\nYou have to write the content of the eBook page to the writer in Markdown format, ensuring it is well-structured and visually appealing. ", config={
                "response_mime_type": "application/json",
                "response_schema": eBookRecipe,
            }).text)
            print(f"Writer Response: {writer_response}\n\n")
            history.append(f"WRITER: {writer_response['response']}")
        
        head_response = json.loads(head.send_message(f"Page Size: A4 and Font Size: 22\nChapter: {chapter['title']}\nContent: {chapter['content']}\nPages: {chapter['pages']}\nThe writer has written the content of the eBook current chapter. Now you have to generate the Markdown format of the current chapter. Now generate the Markdown format content for each pages in the chapter as writer has written. Chapter Pages Used: {chapter['pages']} ", config={
            "response_mime_type": "application/json",
            "response_schema": eBookRecipPage,
        }).text)
        print(f"Head Response: {head_response}\n\n")
        chapters_markdown.append(head_response['chapter_markdown'])
        history = []

    return chapters_markdown

def generate_content_page(prompt, font_size=20):
    """
    Generate the table of contents page in markdown format.
    
    Args:
        prompt (str): Prompt for content page generation.
        font_size (int, optional): Font size for the content page. Default is 20.
        
    Returns:
        str: Markdown content for the table of contents.
    """
    # Initialize the AI client
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    # Create Head agent
    head = client.chats.create(model="gemini-2.0-flash")

    # Define the Head's role
    head.send_message(
        "Your Name is Head or Mr. Jake Thompson. You are responsible for generating the content page "
        "of a PDF eBook. Your task is to create a well-structured contents in Markdown format, "
        "listing chapter names and corresponding page numbers."
        "You are provided with the number of pages used per chapter and you have to properly arrange the chapters in the content page by there page numbers."
    )

    # Request Markdown-formatted table of contents based on the prompt
    head_response = json.loads(head.send_message(
        f"Generate the contents page for the eBook based on the following prompt:\n\n{prompt}\n"
        f"Font Size Used: {font_size} and Page Size: A4\n"
        "Ensure the content page is structured properly in Markdown format, listing chapter names and "
        "use this format, for eg: Chapter 1: This is the chapter 1............... Pg. 1-2 "
        "don't use any table format or anything else, just use this format, this should be a markdown plain text not any link or anything else, just plain text but styled one.",
        config={
            "response_mime_type": "application/json",
            "response_schema": ContentPageSchema,
        }
    ).text)

    return head_response["markdown"] 