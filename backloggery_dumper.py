import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

username = 'ludek_cortex'
url = 'https://backloggery.com/ajax_moregames.php?user={}&console=&rating=&status=&unplayed=&own=&search=&comments=&region=&region_u=2&wish=&alpha=&temp_sys=&total=0&aid=1'.format(username)

r = requests.get(url)
payload = r.text
soup = BeautifulSoup(payload, 'html.parser')

games = soup.find_all('section', class_='gamebox')

games_list = []

for game in games:
    game_entry = {}
    try:
        gra = game.h2.img
        title = game.h2.b.text
        # platform = game.h2.b.text
        if '▼' in title:
            title = title.replace('▼', '').strip()
            platform = 'COLLECTION'

        print(gra)
    except AttributeError:
        continue