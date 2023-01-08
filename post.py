import requests as r

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'Token 97058030d1b6e1e70b65a203a44a559351defc53'
}


page = r.post('http://localhost:8000/api/products/', data=open('db2.json', 'rb'), headers=headers)

print(page.text)
    