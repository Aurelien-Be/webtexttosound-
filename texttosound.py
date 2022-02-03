
import gtts 
from playsound import playsound
from bs4 import BeautifulSoup
import requests

url = input('Url of the page where is the text you want to hear: ')
Language = input('Wich language do you want to hear ?: ')

# Make a GET request to fetch the raw HTML content
try:  
  html_content = requests.get(url).text
except Exception:
    print("Sorry, something went wrong. Have you verified you're URL ?")
    exit()


# Parse the html content
soup = BeautifulSoup(html_content, "lxml")
mytext = soup.body.text

# make request to google to get synthesis
try: 
  tts = gtts.gTTS(mytext, lang=Language, tld="com")
except ValueError: 
    print('It seems that this language is not supported. You have to enter the language code, as en for english, fr for french, ru for russian etc')
    exit()

# save the audio file
tts.save("exemple.mp3")

# play the audio file
playsound("exemple.mp3")