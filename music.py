import requests
import json
import time

while True:
    url = 'https://zenoplay.zenomedia.com/api/zenofm/nowplaying/2cgy8mzvsy8uv'
    response = requests.get(url)
    data = json.loads(response.text)
    title = data['title']

    with open("index.html", "w") as file:
        file.write("<html lang='pt-br'><meta http-equiv='Content-Type' content='text/html; charset=UTF-8'>")
        file.write("<body><h1>")
        file.write("" + title)
        file.write("</h1></body></html>")

    time.sleep(60)
