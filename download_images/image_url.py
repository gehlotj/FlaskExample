from bs4 import BeautifulSoup
import requests

class GetImageURL:

    def __init__(self,url):
        self.url = url
        self.approve_extensions = ['jpg','jpeg','png']

    def get_images_from_url(self):
        html_text = requests.get(self.url).text
        soup = BeautifulSoup(html_text,"html.parser")
        images=[]
        for s in soup.findAll('img'):
            img = s.get('src')
            #check for the src extensions
            if img != None and img[-3:].lower() in self.approve_extensions:
                images.append(s.get('src'))
            else: continue
            #check if the subdomain is not appended
            if images[-1] != None and images[-1].find("://") == -1:
                temp = self.url.find('.')+4
                if images[-1][0] != '/':
                        images[-1] = '/'+images[-1]
                images[-1] = self.url[:temp]+images[-1]
                #adding www. Google would not pull data if www is not appended
                if images[-1].find('www') == -1:
                    images[-1] = images[-1].replace('http://','http://www.')
        return images
