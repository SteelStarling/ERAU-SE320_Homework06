from requests import get
from json import dump, load

x = get("https://api.nasa.gov/DONKI/FLR?api_key=DEMO_KEY").json()

for y in x:
    print(y)