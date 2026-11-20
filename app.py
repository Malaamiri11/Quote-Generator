
#This project is to send motivational quotes to my phone
import random
#python random library wer need for the quotes to randomize to send to my phone

import requests
#this library sends http requests goign to ntlfy
#ntfy is on a server
#created a list  with all the motivational quotes
motivational_quotes = [
    "keep going, you got this!.",
    "Do not quit on your dreams and what you want to be.",
    "Believe in yourself. Have a positive mindset.",
    "You can accomplish whatever you want",
    "Have confidence in yourself",
    "Always try your hardest.",
]

random_quotes = random.choice(motivational_quotes)
#prints random quote freom the array
#Also stores it inside random_quotes variabele

#this is my topic i subscribed and made on my phone ntfy
topic = "-38Interstoic-38"

# URL: https://ntfy.sh/YOUR_TOPIC_HERE
#https://ntfy.sh/-38Interstoic-38


#this sends as the post request
#requests.post is a method 
#used to send a HTTP POST request to a specified URL 
#Which is our subscribed topic
#allows me to submit data to a server
#via data, json file








response = requests.post(
    f"https://ntfy.sh/{topic}", 
    data=random_quotes,

    ) 




#we need to make it run at diff periods of time 
#task scheduler. 



















