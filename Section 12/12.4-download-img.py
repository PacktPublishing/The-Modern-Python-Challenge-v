import requests

def get_image(url, filename):
    target = requests.get(url)
    ext = '.png'
    open(filename + ext, 'wb').write(target.content)
    print(f"{filename}{ext} downloaded")

url = "https://www.python.org/static/img/python-logo@2x.png"

get_image(url,'py-logo')
