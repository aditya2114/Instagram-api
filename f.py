import requests
import json
from time import sleep
from gtts import gTTS 
import os 

def speak(name):
    mytext = name+"Followed you"
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3") 
    os.system("welcome.mp3")
    return 0

def request():
    url = "https://instagram-data1.p.rapidapi.com/followers"
    querystring = {"username":"test__usernme"}  
    headers = {
        'x-rapidapi-key': "<getyourskey>",
        'x-rapidapi-host': "<getyourskey>"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    followers = data["count"]
    followers_list = []
    print(followers)
    for i in range(followers):
        followers_list.append(data['collector'][i]['username'])
    return followers_list

def start(data):
    first_followers_count = len(data)
    while True:
        print(first_followers_count)
        sleep(5)
        new_data = request()
        new_follower_count = len(new_data)
        if(new_follower_count > first_followers_count):
            print("Incresed")
            speak(new_data[0])
            first_followers_count = new_follower_count

if __name__ == '__main__':
    followers_list = request()
    start(followers_list)
