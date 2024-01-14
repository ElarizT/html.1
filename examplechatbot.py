import requests
from bs4 import BeautifulSoup

# Specify the URL of the website you want to scrape
url = ['https://en.wikipedia.org/wiki/Turritopsis_dohrnii']
url2 = ['https://en.wikipedia.org/wiki/Poland']

# Send an HTTP request to the URL
response = requests.get(url + url2)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract information by finding HTML elements using tags, classes, or other attributes
    # Example: Extracting all the text from paragraphs
    paragraphs = soup.find_all('p')
    website_text = '\n'.join(paragraph.text for paragraph in paragraphs)
    print(website_text)
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)

# Capture user input
question = input('Enter your question: ')

# Define a function to generate answers
def generate_answers_chatbot(user_question):
    if 'jellyfish' in user_question.lower():
        answer1 = website_text.lower().find(question[0])
        if answer1 != -1:
            sub = website_text[answer1:]
            return sub
        else:
            return "The term was not found in the scraped text."
    else:
        return "I don't have an answer for that question."

# Call the function with the user's question
answer = generate_answers_chatbot(question)
print("Chatbot's Answer:")
print(answer)