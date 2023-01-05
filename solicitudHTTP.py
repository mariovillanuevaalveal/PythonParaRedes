import requests

def make_request(url):
    response = requests.get(url)
    return response.text

url = "https://portales.inacap.cl"
response_text = make_request(url)
print(response_text)