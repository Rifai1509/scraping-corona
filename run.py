from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from  selenium import webdriver
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/detik')
def detk():
    keyword = 'corona'
    html_source = requests.get('https://www.detik.com/search/searchall?', params={'query' : keyword, 'siteid' : 2})
    soup = BeautifulSoup(html_source.text, 'html.parser')
    search_area = soup.find(attrs={'class': 'list media_rows list-berita'})
    images = search_area.findAll(attrs={'class': 'ratiobox box_thumb'})
    return render_template('Detik.html', images=images)

@app.route('/kompas')
def kompas():
    cari = 'corona'
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument('--headless')
    options.add_argument('--disable-extensions')
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    browserdriver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Web Driver\chromedriver.exe')
    browserdriver.get('https://search.kompas.com/search/?q='+cari+'&submit=Submit')
    content = browserdriver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    area = soup.findAll('div', attrs={'class': 'gsc-webResult gsc-result'})
    return render_template('Kompas.html', area=area)

if __name__ == '__main__':
    app.run(debug=True)


