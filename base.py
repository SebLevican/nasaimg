import requests
import json
from string import Template


def build_web_page(URLS):
    

    img_template = Template('<img src="$url">')
    imagen = ''
    for i in URLS:
        
        imagen += img_template.substitute(url = i[0])
#print(imagen)

    html_template = Template('''<!DOCTYPE html>
                                <html>
                                <head>
                                </head>
                                <body>
                                <ul>
                                <li> $body </li>
                                
                                </ul>
                                </body>
                                </head>
                                </html>
                            ''')
    
    print(html_template.substitute(body = imagen))

    #lista_url = [elemento['url'] for elemento in URLS]
    texto_img = ''

    for url in URLS:
        texto_img += img_template.substitute(url = url) +'\n'

    print(texto_img)

    html = html_template.substitute(body = texto_img)
    print(html)

    with open('output.html', 'w') as f:
        f.write(html)

api_key = 'fVc1ve6ValusZPFy96kJmapDfqJjCJN9PITkInIQ'
sol =25
url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?&api_key={api_key}'

response = requests.request('get', url).json()
total_image = len(response['latest_photos'][:25])
url_l = [response['latest_photos'][i]['img_src'] for i in range(0, total_image)]

build_web_page(url_l)

