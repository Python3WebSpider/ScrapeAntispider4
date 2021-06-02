import re
import requests
url = 'https://antispider4.scrape.center/css/app.654ba59e.css'


response = requests.get(url)
pattern = re.compile('.icon-(.*?):before\{content:"(.*?)"\}')
results = re.findall(pattern, response.text)
icon_map = {item[0]: item[1] for item in results}
print(icon_map['789'])
print(icon_map['437'])
