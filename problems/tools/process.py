from bs4 import BeautifulSoup
import re

def process(input):
    def replace_(match):
        return match.group(0).replace("\t", "\\t")

    input_html = re.sub(r'\$(.*?)\$', replace_, input)
    soup = BeautifulSoup(input, 'html.parser')
    for img in soup.find_all('img'):
        img.replace_with("[IMAGE]")

    cleaned_text = soup.get_text(separator=' ', strip=True)    
    return cleaned_text
