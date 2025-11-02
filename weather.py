import requests

city = input("Şehir adı: ")

# OpenWeather hesabından aldığın API anahtarını buraya yapıştır:
api_key = "YOUR_API_KEY"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=tr"
res = requests.get(url)
data = res.json()

if res.status_code == 200:
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print(f"{city} için hava durumu: {temp}°C, {desc}")
else:
    print("❌ Şehir bulunamadı.")
