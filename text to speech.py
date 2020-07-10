import requests
url = "https://translate.google.com/translate_tts"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

text = "Hello தினேஷ்"

params = {
    "ie" : "UTF-8",
    "q" : text,
    "tl" : "ta",
    "client" : "gtx" 
}

r = requests.get(url,params = params,headers = headers)

with open("sample.mp3","wb") as f:
    f.write(r.content)





