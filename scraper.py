from bs4 import BeautifulSoup
import requests
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

headers = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_website_contents(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.title.string if soup.title else "No title found"

    if soup.body:
        for tag in soup.body(["script", "style", "img", "input"]):
            tag.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""

    return (title + "\n\n" + text)[:2000]


system_prompt = """
You are a web scraper assistant that analyzes website content and provides a detailed and informative text. Respond in clean markdown.
"""

user_prompt = """
Here is the url of the website. Provide a summary of the content, including key points, main topics, and any relevant information.
"""


def summarize(url):
    website = fetch_website_contents(url)

    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt + "\n\n" + website}
        ]
    )

    return response.choices[0].message.content