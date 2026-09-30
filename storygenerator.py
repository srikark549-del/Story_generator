import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    print("Error: GEMINI_API_KEY not found in .env file.")
    exit()
client = genai.Client(api_key=API_KEY)
MODEL = "gemini-2.5-flash"
def generate_story(topic, genre, length):
    prompt = f"""
You are a creative story generator.
Generate an original story based on the following details:
Topic: {topic}
Genre: {genre}
Length: {length}
Requirements:
- Give the story a suitable title.
- Make the story creative and engaging.
- Keep the story coherent from beginning to end.
- Use simple and understandable language.
- Do not explain the story or provide analysis.
- Output only the title and the story.
"""
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text
print("\n======================================")
print("          STORY GENERATOR")
print("======================================")
print("Create your own AI-generated story!")
print("Type 'quit' to exit.")
print("======================================\n")
while True:
    topic = input("Enter a story topic: ").strip()
    if topic.lower() in ["quit", "exit", "bye"]:
        print("\nThanks for using Story Generator!")
        break
    if not topic:
        print("Please enter a topic.\n")
        continue
    genre = input(
        "Enter the genre (Adventure, Mystery, Fantasy, Sci-Fi, Horror, etc.): "
    ).strip()
    if not genre:
        genre = "Adventure"
    length = input(
        "Enter story length (Short, Medium, or Long): "
    ).strip()
    if not length:
        length = "Medium"
    print("\nGenerating your story...\n")
    try:
        story = generate_story(topic, genre, length)

        print("======================================")
        print(story)
        print("======================================\n")
    except Exception as e:
        print("\nError generating story:", e)
        print("Please check your API key and internet connection.\n")