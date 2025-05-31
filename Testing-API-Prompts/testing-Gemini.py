from google import genai
from getpass import getpass
geminiKey = getpass("Enter your api key: ")
client = genai.Client(api_key=geminiKey)
prompt = input("Enter your prompt: ")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents=prompt
)

print(response.text)